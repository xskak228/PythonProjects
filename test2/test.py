
import sqlite3
import sys

import requests
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QVBoxLayout, QCheckBox, \
    QRadioButton, QDialog, QMessageBox
from PyQt5.QtWidgets import QMainWindow

# path of file "settings"
path_settings = 'settings.cfg'

# open settings
f = open(path_settings, encoding="utf-8")
lines = f.read().splitlines()

# path if DB
path_standartDB = lines[2]          # path of standart DB
path_SetUP_file = lines[4]          # path of SetUP fi
# path of UI
MainWindow_path = lines[8]          # path MainWindow_path
CreateSetup_path = lines[10]        # path CreateSetup_path
SettingsForm_path = lines[12]       # path SettingsForm_path

# debug mod
DebugMod = True if lines[-1] == "1" else False
f.close()                           # cose file
print("DebugMod - True") if DebugMod else print("DebugMod - False")      # debug




# Main
class MainProgramm(QMainWindow):
    def __init__(self):
        super().__init__()
        # mainwindow
        global MainWindow_path
        uic.loadUi(MainWindow_path, self)
        self.setWindowTitle('WarTunderRandom')

        # files
        global path_standartDB      # path of standart DB
        global path_SetUP_file           # path of SetUP fi


        # menu shortCut
        self.ach_save.setShortcut("Ctrl+S")
        self.ach_load.setShortcut("Ctrl+L")
        self.ach_create_setup.setShortcut("Shift+C")
        self.ach_load_setup.setShortcut("Shift+L")
        self.ach_exit.setShortcut("Alt+F4")
        self.ach_settings.setShortcut("Ctrl+Shift+S")   # settings
        self.ach_exit.triggered.connect(self.close)     # close programm

        # menu programm start
        self.ach_create_setup.triggered.connect(self.open_CreateForm)       # crate SetUP venichle
        self.ach_load_setup.triggered.connect(self.open_LoadDialog)         # load SetUP venichle
        self.ach_settings.triggered.connect(self.open_SettingsForm)         # settings form

    # func. open CreateForm "SetUP"
    def open_CreateForm(self):
        Create_SetUP().show()

    # func. open SettingsForm Dialog
    def open_SettingsForm(self):
        Settings_Form().exec()

    # func. load SetUP
    def open_LoadDialog(self):
        global path_SetUP_file  # take global path

        print("class MainProgramm > def open_LoadDialog  -  load...") if DebugMod else print()      # debug

        path_SetUP_file = QFileDialog.getOpenFileName(self, 'Выбрать SetUp', '',
                                                      'SetUp (*.db);;DataBase (*.db);;Все файлы (*)')[0]

        # check formatfile
        # ,,,

        # open settings
        file = open(path_settings, encoding="utf-8", mode="w")
        lines.pop(4)  # delete previous path
        lines.insert(4, path_SetUP_file)  # insert new path
        for i in lines:
            print(i, file=file)
        print("class MainProgramm > def open_LoadDialog  -  settings changes") if DebugMod else print()      # debug
        file.close()


# Create SetUP
class Create_SetUP(QDialog):
    def __init__(self):
        super().__init__()
        # global
        global path_standartDB
        global CreateSetup_path

        # Window
        uic.loadUi(CreateSetup_path, self)
        self.setWindowTitle('Создать SetUP')

        # staff
        self.all_chb = []  # all checkBox
        self.result = []   # result db
        self.c = False
        # ____
        self.ussr = []
        self.usa = []
        self.germ = []

        # functions
        self.create()   # func.
        self.nations.activated.connect(self.change_nationToCHB)                 # func. change nation
        self.rbtn_all.toggled.connect(lambda state: self.chaked_all(state))     # func. rbtn
        self.btn_N.clicked.connect(self.save_nationToSetup)        # func. save nation to SetUp

    # make all CHB chacked
    def chaked_all(self, state):
        for i in self.all_chb:
            if "chb_" not in i.text():
                i.setChecked(state)

    # create widget CHB
    def create(self):
        # create widget
        self.widget = QWidget()
        self.vbox = QVBoxLayout()

        # creat checkbox's
        self.rbtn_all = QRadioButton("ВСЕ", self)   # crate radioBatton "all"
        self.rbtn_all.setVisible(False)             # make rbtn anVisible
        self.vbox.addWidget(self.rbtn_all)          # add in widget rbtn
        self.all_chb.append(self.rbtn_all)          # add in list rbtn
        for i in range(1, 150):
            object = QCheckBox("chb_" + str(i))
            object.setVisible(False)
            self.vbox.addWidget(object)
            self.all_chb.append(object)
        self.widget.setLayout(self.vbox)

        # add widget to scrollArea
        self.scrollArea_3.setWidget(self.widget)

    # change nation on CHB and rename his
    def change_nationToCHB(self):
        # update all CHB
        for i in self.all_chb:
            i.setVisible(False)
            i.setChecked(False)

        # connect to DB
        con = sqlite3.connect(path_standartDB)
        cur = con.cursor()


        # choose nations
        if self.nations.currentText() == "Не выбрано":
            for i in self.all_chb:
                i.setVisible(False)
                i.setChecked(False)
            self.c = False
        elif self.nations.currentText() == "Германия":
            self.result = cur.execute("""SELECT name FROM GERMANY_tanks ORDER BY id;""").fetchall()  # take all "GERMANY tanks
            self.c = True
        elif self.nations.currentText() == "СССР":
            self.result = cur.execute("""SELECT name FROM USSR_tanks ORDER BY id;""").fetchall()  # take all "USSR" tanks
            self.c = True
        elif self.nations.currentText() == "США":
            self.result = cur.execute("""SELECT name FROM USA_tanks ORDER BY id;""").fetchall()  # take all "USA" tanks
            self.c = True

        # rename CHB
        if self.c:
            self.rbtn_all.setVisible(True)  # make rbtn Visible
            for key, i in enumerate(self.all_chb[1:len(self.result) + 1]):
                i.setVisible(True)  # make CHB Visible
                i.setText(str(self.result[key][0]))

    # save nation to 1/3 SetUp'a
    def save_nationToSetup(self):
        # ____
        self.ussr = []
        self.usa = []
        self.germ = []

        # add tanks
        if self.nations.currentText() == "СССР":
            for i in self.all_chb[1:]:
                if i.isChecked() == True:
                    self.ussr.append(i.text())
            print(self.ussr) if DebugMod else print()  # debug
        elif self.nations.currentText() == "Германия":
            for i in self.all_chb[1:]:
                if i.isChecked() == True:
                    self.germ.append(i.text())
            print(self.germ) if DebugMod else print()  # debug
        elif self.nations.currentText() == "США":
            for i in self.all_chb[1:]:
                if i.isChecked() == True:
                    self.usa.append(i.text())
            print(self.usa) if DebugMod else print()  # debug





# Settings
class Settings_Form(QDialog):
    def __init__(self):
        super().__init__()
        # Window
        global SettingsForm_path
        uic.loadUi(SettingsForm_path, self)
        self.setWindowTitle('Настройки')

        # options
        self.tBtn_StandartDB.clicked.connect(self.Update_StandartDB)
        self.tBtn_SetUP.clicked.connect(self.Update_SetUP)

        # download BD
        self.btn_dloud.clicked.connect(self.Download_DB)

        # update inf.
        self.Path_standartBD.setText(str(path_standartDB))
        self.Path_SetUP.setText(str(path_SetUP_file))

    # update path of StandartDB
    def Update_StandartDB(self):
        # open settings
        global path_settings
        file = open(path_settings, encoding="utf-8")
        lines = file.read().splitlines()
        file.close()

        global path_standartDB      # take global path
        path_standartDB = QFileDialog.getOpenFileName(self, 'Выбрать SetUp', '',
                                                      'SetUp (*.db);;DataBase (*.db);;Все файлы (*)')[0]
        self.Path_standartBD.setText(str(path_standartDB))      # change path

        # open settings
        file = open(path_settings, encoding="utf-8", mode="w")
        lines.pop(2)                        # delate previous path
        lines.insert(2, path_standartDB)    # insert new path
        for i in lines:
            print(i, file=file)
        print("class Settings_Form > def Update_StandartDB  -  settings changes") if DebugMod else print()  # debug
        file.close()

    # update path of StandartDB
    def Update_SetUP(self):
        # open settings
        global path_settings
        file = open(path_settings, encoding="utf-8")
        lines = file.read().splitlines()
        file.close()

        global path_SetUP_file      # take global path
        path_SetUP_file = QFileDialog.getOpenFileName(self, 'Выбрать SetUp', "",
                                                      'SetUp (*.db);;DataBase (*.db);;Все файлы (*)')[0]
        self.Path_SetUP.setText(str(path_SetUP_file))           # change path

        # open settings
        file = open(path_settings, encoding="utf-8", mode="w")
        lines.pop(4)  # delete previous path
        lines.insert(4, path_SetUP_file)  # insert new path
        for i in lines:
            print(i, file=file)
        print("class Settings_Form > def Update_SetUP  -  settings changes") if DebugMod else print()  # debug
        file.close()

    def Download_DB(self):
        global path_standartDB
        global path_settings

        print("class Settings > def Download_DB  -  download...") if DebugMod else print()              # debug

        # try downLoad file
        try:
            f = open(r'DB/standart_DBWTR.db', "wb")     # create file
            ufr = requests.get("https://github.com/xskak228/cfg/blob/main/test_DB.db?raw=true")     # download file
            f.write(ufr.content)    # write to file
            f.close()

            # update path
            path_standartDB = 'DB/standart_DBWTR.db'

            print("class Settings > def Download_DB  -  success download!") if DebugMod else print()  # debug

            # success message
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Успешное скачивание!")
            msg.setWindowTitle("Успех")
            msg.exec_()

            # change path
            file = open(path_settings, encoding="utf-8")
            lines = file.read().splitlines()
            file.close()

            self.Path_standartBD.setText(str(path_standartDB))  # change path

            # open settings
            file = open(path_settings, encoding="utf-8", mode="w")
            lines.pop(2)  # delate previous path
            lines.insert(2, path_standartDB)  # insert new path
            for i in lines:
                print(i, file=file)
            print("class Settings_Form > def Download_DB  -  settings changes") if DebugMod else print()  # debug
            file.close()
        except Exception:
            print("ERROR! class Settings > def Download_DB  -  download Failed")
            # failed message
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Непредвиденная ошибка!")
            msg.setInformativeText('Проверьте подключение к Интернету')
            msg.setWindowTitle("Ошибка")
            msg.exec_()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainProgramm()
    ex.show()
    sys.exit(app.exec())
