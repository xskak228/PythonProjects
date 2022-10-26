
import os
import sqlite3
import sys
import datetime
now = datetime.datetime.now()

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
# flags
doFlags = True if lines[16] == "1" else False

# logs mod
log_file = open('Logs/' + str(now.strftime("%d-%m-%Y_%H-%M")) + ".txt", "w+")
log_file.close()
log_file_path = 'Logs/' + str(now.strftime("%d-%m-%Y_%H-%M")) + ".txt"
with open(log_file_path, "a") as log_file:
    print(str("Start program - " + str(now)), file=log_file)

# debug mod
DebugMod = True if lines[-1] == "1" else False
f.close()                           # cose file
print("DebugMod  -  True") if DebugMod else print("DebugMod  -  False")      # debug
with open(log_file_path, "a") as log_file:
    print("DebugMod  -  True", file=log_file) if DebugMod else print("DebugMod  -  False", file=log_file)   # log
    print("Main  -  file'standart DB' don't install", file=log_file)\
    if DebugMod and not os.path.exists(path_standartDB) else print()
if not os.path.exists(path_standartDB):

    try:
        f = open(r'DB/standart_DBWTR.db', "wb")  # create file
        ufr = requests.get("https://github.com/xskak228/cfg/blob/main/test_DB.db?raw=true")  # download file
        f.write(ufr.content)  # write to file
        f.close()

        # update path
        path_standartDB = 'DB/standart_DBWTR.db'

        print("Main  -  file'standart DB' success download!") if DebugMod else print()  # debug
        with open(log_file_path, "a") as log_file:
            print("Main  -  file'standart DB' success download!", file=log_file)     # log

        # change path
        file = open(path_settings, encoding="utf-8")
        lines = file.read().splitlines()
        file.close()

        # open settings
        file = open(path_settings, encoding="utf-8", mode="w")
        lines.pop(2)  # delate previous path
        lines.insert(2, path_standartDB)  # insert new path
        for i in lines:
            print(i, file=file)
        print("Main  -  settings changes") if DebugMod else print()  # debug
        with open(log_file_path, "a") as log_file:
            print("Main  -  settings changes", file=log_file)   # log
        file.close()
    except Exception:
        print("ERROR! Main  -  download Failed") if DebugMod else print()  # debug
        with open(log_file_path, "a") as log_file:
            print("ERROR! Main  -  download Failed", file=log_file)   # log



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
        global log_file


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
        global log_file     # take logFile

        print("class MainProgramm > def open_LoadDialog  -  load...") if DebugMod else print()      # debug
        with open(log_file_path, "a") as log_file:
            print("class MainProgramm > def open_LoadDialog  -  load...", file=log_file)   # log

        path_SetUP_file = QFileDialog.getOpenFileName(self, 'Выбрать SetUp', '',
                                                      'SetUp (*.db);;DataBase (*.db);;Все файлы (*)')[0]

        # check correction
        if path_SetUP_file[-9:] == "_DBWTR.db":
            # open settings
            file = open(path_settings, encoding="utf-8", mode="w")
            lines.pop(4)  # delete previous path
            lines.insert(4, path_SetUP_file)  # insert new path
            for i in lines:
                print(i, file=file)
            print("class MainProgramm > def open_LoadDialog  -  load success") if DebugMod else print()  # debug
            print("class MainProgramm > def open_LoadDialog  -  settings changes") if DebugMod else print()  # debug
            with open(log_file_path, "a") as log_file:
                print("class MainProgramm > def open_LoadDialog  -  load success", file=log_file)      # log
                print("class MainProgramm > def open_LoadDialog  -  settings changes", file=log_file)  # log
            file.close()
        else:
            # Failed message
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Укажите файл правильного формата \nПример: FirstSETUP_DBWTR.db")
            msg.setWindowTitle("Ошибка")
            msg.exec_()
            print("class MainProgramm > def open_LoadDialog  -  load failed(bed format)") if DebugMod else print()  # debug
            with open(log_file_path, "a") as log_file:
                print("class MainProgramm > def open_LoadDialog  -  load failed(bed format)", file=log_file)     # log


# Create SetUP
class Create_SetUP(QDialog):
    def __init__(self):
        super().__init__()
        # global
        global path_standartDB
        global CreateSetup_path
        global path_SetUP_file

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
        self.btn_N.clicked.connect(self.save_nationToSetup)                     # func. save nation to SetUp
        self.btn_saveAll.clicked.connect(self.save_all)                         # save all tanks

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
            print("Ussr tanks - " + str(self.ussr)) if DebugMod else print()  # debug
            with open(log_file_path, "a") as log_file:
                print("Ussr tanks - " + str(self.ussr), file=log_file)
        elif self.nations.currentText() == "Германия":
            for i in self.all_chb[1:]:
                if i.isChecked() == True:
                    self.germ.append(i.text())
            print("Germany tanks - " + str(self.germ)) if DebugMod else print()  # debug
            with open(log_file_path, "a") as log_file:
                print("Usa tanks - " + str(self.usa), file=log_file)
        elif self.nations.currentText() == "США":
            for i in self.all_chb[1:]:
                if i.isChecked() == True:
                    self.usa.append(i.text())
            with open(log_file_path, "a") as log_file:
                print("Usa tanks - " + str(self.usa), file=log_file)
            print("Usa tanks - " + str(self.usa)) if DebugMod else print()  # debug

    # func. save all
    def save_all(self):
        global path_SetUP_file
        global log_file_path

        print("class Create_SetUP > def save_all  -  download...") if DebugMod else print()  # debug
        with open(log_file_path, "a") as log_file:
            print("class Create_SetUP > def save_all  -  download...", file=log_file)       # log

        # try downLoad file
        try:
            f = open(r'DB/' + str(self.takeName.text()) + '_DBWTR.db', "wb")  # create file
            ufr = requests.get("https://github.com/xskak228/cfg/blob/main/clean_DBWTR.db?raw=true")  # download file
            f.write(ufr.content)  # write to file
            f.close()

            print("class Create_SetUP > def save_all  -  success download!") if DebugMod else print()  # debug
            with open(log_file_path, "a") as log_file:
                print("class Create_SetUP > def save_all  -  success download!", file=log_file)       # log

            # success message
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Успешное скачивание!")
            msg.setWindowTitle("Успех")
            msg.exec_()

            path_SetUP_file = 'DB/' + str(self.takeName.text()) + '_DBWTR.db'

            # change path
            file = open(path_settings, encoding="utf-8")
            lines = file.read().splitlines()
            file.close()

            # open settings
            file = open(path_settings, encoding="utf-8", mode="w")
            lines.pop(4)  # delate previous path
            lines.insert(4, path_SetUP_file)  # insert new path
            for i in lines:
                print(i, file=file)
            print("class Create_SetUP > def save_all  -  settings changes") if DebugMod else print()  # debug
            with open(log_file_path, "a") as log_file:
                print("class Create_SetUP > def save_all  -  settings changes", file=log_file)  # log
            file.close()
        except Exception:
            print("ERROR! class Create_SetUP > def save_all  -  download Failed") if DebugMod else print()  # debug
            with open(log_file_path, "a") as log_file:
                print("ERROR! class Create_SetUP > def save_all  -  download Failed", file=log_file)  # log
            # failed message
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Непредвиденная ошибка!")
            msg.setInformativeText('Проверьте подключение к Интернету')
            msg.setWindowTitle("Ошибка")
            msg.exec_()


        # save...
        # connect to DB
        con1 = sqlite3.connect(path_SetUP_file)
        cur1 = con1.cursor()
        con2 = sqlite3.connect(path_standartDB)
        cur2 = con2.cursor()

        # addtanks
        if len(self.ussr) != 0:
            for i in self.ussr:
                result = cur2.execute("""SELECT * FROM USSR_tanks WHERE name == ?;""", (i,)).fetchall()  # take all "GERMANY tanks
                result = list(result[0]) if len(result) != 0 else []
                cur1.execute("""INSERT INTO USSR_tanks(id,name,type,lvl) VALUES(?,?,?,?)""",
                             (result[0], result[1], result[2], result[3],))

        if len(self.usa) != 0:
            for i in self.usa:
                result = cur2.execute("""SELECT * FROM USA_tanks WHERE name == ?;""", (i,)).fetchall()  # take all "GERMANY tanks
                result = list(result[0]) if len(result) != 0 else []
                cur1.execute("""INSERT INTO USA_tanks(id,name,type,lvl) VALUES(?,?,?,?)""",
                             (result[0], result[1], result[2], result[3],))

        if len(self.germ) != 0:
            for i in self.germ:
                result = cur2.execute("""SELECT * FROM GERMANY_tanks WHERE name == ?;""", (i,)).fetchall()  # take all "GERMANY tanks
                result = list(result[0]) if len(result) != 0 else []
                cur1.execute("""INSERT INTO GERMANY_tanks(id,name,type,lvl) VALUES(?,?,?,?)""",
                             (result[0], result[1], result[2], result[3],))

        # disconect DB
        con1.commit()
        con1.close()
        con2.commit()
        con2.close()


# Settings
class Settings_Form(QDialog):
    def __init__(self):
        super().__init__()
        # Window
        global SettingsForm_path
        global log_file_path
        uic.loadUi(SettingsForm_path, self)
        self.setWindowTitle('Настройки')

        # options
        self.tBtn_StandartDB.clicked.connect(self.Update_StandartDB)
        self.tBtn_SetUP.clicked.connect(self.Update_SetUP)
        self.chb_FlagVisible.toggled.connect(lambda state: self.Flags(state))

        # download DB
        self.btn_dloud.clicked.connect(self.Download_DB)

        # update inf.
        self.Path_standartBD.setText(str(path_standartDB))
        self.Path_SetUP.setText(str(path_SetUP_file))
        self.chb_FlagVisible.setChecked(doFlags)

    #flags
    def Flags(self, state):
        global doFlags
        global log_file_path

        print("Flag State  -  " + str(state)) if DebugMod else print()  # debug
        with open(log_file_path, "a") as log_file:
            print("Flag State  -  " + str(state), file=log_file)
        doFlags = state

        # open settings
        file = open(path_settings, encoding="utf-8", mode="w")
        lines.pop(16)  # delete previous path
        lines.insert(16, "1" if doFlags else "0")  # insert new path
        for i in lines:
            print(i, file=file)
        print("class Settings_Form > def Flags  -  settings changes") if DebugMod else print()  # debug
        with open(log_file_path, "a") as log_file:
            print("class Settings_Form > def Flags  -  settings changes", file=log_file)  # log
        file.close()


    # update path of StandartDB
    def Update_StandartDB(self):
        # open setting
        global path_settings
        global log_file_path

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
        with open(log_file_path, "a") as log_file:
            print("class Settings_Form > def Update_StandartDB  -  settings changes", file=log_file)  # log
        file.close()

    # update path of StandartDB
    def Update_SetUP(self):
        global log_file  # take logFile
        global log_file_path

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
        with open(log_file_path, "a") as log_file:
            print("class Settings_Form > def Update_SetUP  -  settings changes", file=log_file)  # log
        file.close()

    def Download_DB(self):
        global path_standartDB
        global path_settings
        global log_file_path

        print("class Settings_Form > def Download_DB  -  download...") if DebugMod else print()              # debug
        with open(log_file_path, "a") as log_file:
            print("class Settings_Form > def Download_DB  -  download...", file=log_file)  # log

        # try downLoad file
        try:
            f = open(r'DB/standart_DBWTR.db', "wb")     # create file
            ufr = requests.get("https://github.com/xskak228/cfg/blob/main/test_DB.db?raw=true")     # download file
            f.write(ufr.content)    # write to file
            f.close()

            # update path
            path_standartDB = 'DB/standart_DBWTR.db'

            print("class Settings_Form > def Download_DB  -  success download!") if DebugMod else print()  # debug
            with open(log_file_path, "a") as log_file:
                print("class Settings_Form > def Download_DB  -  success download!", file=log_file)  # log

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
            with open(log_file_path, "a") as log_file:
                print("class Settings_Form > def Download_DB  -  settings changes", file=log_file)  # log
            file.close()
        except Exception:
            print("ERROR! class Settings > def Download_DB  -  download Failed") if DebugMod else print()  # debug
            with open(log_file_path, "a") as log_file:
                print("ERROR! class Settings > def Download_DB  -  download Failed", file=log_file)  # log
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
