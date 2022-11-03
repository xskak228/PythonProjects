# -*- coding: utf-8 -*-

import datetime
import json
import os
import random
import sqlite3
import sys

from pyqt5_plugins.examplebuttonplugin import QtGui

now = datetime.datetime.now()   # time

import requests
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QVBoxLayout, QCheckBox, \
    QRadioButton, QDialog, QMessageBox, QLabel
from PyQt5.QtWidgets import QMainWindow

# ______SETTINGS__________
# path of file "settings"
path_settings = 'settings.json'
# open settings.json
with open(path_settings) as f:
    data = json.load(f)
    # DB path
    path_standartDB = data["standartDB_path"]  # path of standartDB
    path_SetUP_file = data["SetUP_path"]  # path of SetUP
    # path of UI
    MainWindow_path = data["UI_MainWindow_path"]  # path MainWindow_path
    CreateSetup_path = data["UI_CreateSetup_path"]  # path CreateSetup_path
    SettingsForm_path = data["UI_SettingsForm_path"]  # path SettingsForm_path
    ResultForm_path = data["UI_ResultForm_path"]  # path ResultForm_path
    # other settings
    doFlags = True if data["Flags"] else False  # show flags?
    doMoreInf = True if data["MoreInf"] else False  # show MoreInformathion(create Setup)
    DebugMod = True if data["Debug"] else False  # debug mode
    # filters
    PrimeT = True if data["PrimeT"] else False  # RBTN Prime
    PolkT = True if data["PolkT"] else False  # RBTN Polk
    LVL_T = [True if i else False for i in data["LVL"]]  # all CHB LVL
    TYPE_T = [True if i else False for i in data["TYPE"]]  # all CHB TTPE
    KolT = int(data["Number"])  # number of techn
    Nath = data["Nation"]  # nation
    # theme
    DarkTheme = True if data["Theme"] else False    # do dark theme on?


# logs mod
log_file = open('Logs/' + str(now.strftime("%d-%m-%Y_%H-%M")) + ".txt", "w+")  # create logfile with TimeName
log_file.close()
log_file_path = 'Logs/' + str(now.strftime("%d-%m-%Y_%H-%M")) + ".txt"  # path of last log'a

# write in log
with open(log_file_path, "a", encoding="utf-8") as log_file:
    print(str("Start program - " + str(now)), file=log_file)

# debug
print("DebugMod  -  True") if DebugMod else print("DebugMod  -  False")

# write in log
with open(log_file_path, "a", encoding="utf-8") as log_file:  # write in log
    print("DebugMod  -  True", file=log_file) if DebugMod else print("DebugMod  -  False", file=log_file)  # log
    print("Main  -  file'standart DB' don't install", file=log_file) \
        if DebugMod and not os.path.exists(path_standartDB) else print()

# check file "StandartDB"
if not os.path.exists(path_standartDB):

    try:
        with open(path_settings) as f:
            data = json.load(f)
            f = open(r'DB/standart_DBWTR.db', "wb")  # create file
            ufr = requests.get(data["GitHubLink_standartDB"])  # download file
            f.write(ufr.content)  # write to file
            f.close()

        # update path
        path_standartDB = 'DB/standart_DBWTR.db'

        # debug
        print("Main  -  file'standart DB' success download!") if DebugMod else print()

        # write in log
        with open(log_file_path, "a", encoding="utf-8") as log_file:  # write in log
            print("Main  -  file'standart DB' success download!", file=log_file)  # log

        # debug
        print("Main  -  settings changes") if DebugMod else print()

        # write in log
        with open(log_file_path, "a", encoding="utf-8") as log_file:  # write in log
            print("Main  -  settings changes", file=log_file)  # log

        # update path of StandartDB in Settings
        with open(path_settings) as s:
            data = json.load(s)
            data["standartDB_path"] = path_standartDB
            with open(path_settings, "w") as s:
                json.dump(data, s, indent=4)

    except Exception:
        # debug
        print("ERROR! Main  -  download Failed") if DebugMod else print()

        # write in log
        with open(log_file_path, "a", encoding="utf-8") as log_file:  # write in log
            print("ERROR! Main  -  download Failed", file=log_file)  # log


# Main
class MainProgramm(QMainWindow):
    def __init__(self):
        super().__init__()
        # global
        global MainWindow_path
        global path_standartDB  # path of standart DB
        global path_SetUP_file  # path of SetUP fi
        global log_file
        global LVL_T
        global TYPE_T
        global PrimeT
        global PolkT
        global KolT
        global Nath

        # styleWindow
        # load logo
        with open(path_settings) as f:
            data = json.load(f)
            self.setWindowIcon(QtGui.QIcon(data["logo_path"]))
        # Ui
        uic.loadUi(MainWindow_path, self)
        self.setWindowTitle('WTR_2.1 AlfaTest')

        # theme
        if DarkTheme:
            self.menubar.setStyleSheet("QMenuBar::item:selected {background: #3500d3;}"
                                       "QMenu::item:selected {background: #3500d3;}"
                                       )
            self.setStyleSheet("background-color: rgb(25, 0, 97); color: rgb(255, 255, 255);")
            for i in [self.rbtn_lvl_all, self.chb_lvl_1, self.chb_lvl_2, self.chb_lvl_3,
                      self.chb_lvl_4, self.chb_lvl_5, self.chb_lvl_6, self.chb_lvl_7,
                      self.rbtn_type_all, self.chb_type_lt, self.chb_type_st, self.chb_type_tt,
                      self.chb_type_ptsay, self.chb_type_it, self.chb_type_zsu, self.chb_type_zprk_zrk,
                      self.chb_polkt, self.chb_primet]:
                i.setStyleSheet("background-color: rgb(36, 0, 144);"
                                " padding: 2px;"
                                " padding-left: 5px;")
            self.btn_random.setStyleSheet("background-color: rgb(53, 0, 211);" "border-width: 2px;" "border-radius: 10px;")
            self.nations.setStyleSheet(
                "background-color: rgb(53, 0, 211);" "border-radius: 3px;" "padding: 1px 18px 1px 3px;" "min-width: 6em;")
            self.numb.setStyleSheet("background-color:rgb(53, 0, 211);")
            for i in [self.line, self.line_2]: i.setStyleSheet("background-color: rgb(36, 0, 144)")

        # lists
        self.all_LVL = [self.rbtn_lvl_all, self.chb_lvl_1, self.chb_lvl_2, self.chb_lvl_3,
                        self.chb_lvl_4, self.chb_lvl_5, self.chb_lvl_6, self.chb_lvl_7]
        self.all_TYPE = [self.rbtn_type_all, self.chb_type_lt, self.chb_type_st, self.chb_type_tt,
                         self.chb_type_ptsay, self.chb_type_it, self.chb_type_zsu, self.chb_type_zprk_zrk]

        # menu shortCut
        self.ach_save.setShortcut("Ctrl+S")
        self.ach_load.setShortcut("Ctrl+L")
        self.ach_create_setup.setShortcut("Shift+C")
        self.ach_load_setup.setShortcut("Shift+L")
        self.ach_exit.setShortcut("Alt+F4")
        self.ach_settings.setShortcut("Ctrl+Shift+S")  # settings
        self.ach_exit.triggered.connect(self.close)  # close programm

        # menu programm start
        self.ach_create_setup.triggered.connect(self.open_CreateForm)  # crate SetUP venichle
        self.ach_load_setup.triggered.connect(self.open_LoadDialog)  # load SetUP venichle
        self.ach_settings.triggered.connect(self.open_SettingsForm)  # settings form
        self.rbtn_lvl_all.toggled.connect(lambda state: self.chacked_all(state, "LVL"))  # chacked all CHB(LVL)
        self.rbtn_type_all.toggled.connect(lambda state: self.chacked_all(state, "TYPE"))  # chacked all CHB(TYPE)
        self.btn_random.clicked.connect(self.Random)  # func random
        self.nations.activated.connect(self.changeNation)
        self.changeNation()  # change flag
        self.UpdateFilter()  # update filter

        # flag
        if doFlags:
            with open(path_settings) as f:
                data = json.load(f)
            path = data["flags_path"]
            if self.nations.currentText() == "СССР":
                path += "USSR_flag.png"
            elif self.nations.currentText() == "США":
                path += "USA_flag.png"
            elif self.nations.currentText() == "Германия":
                path += "GERM_flag.png"
            else:
                path = ""
                self.nation.setText("Нация")
            self.nation.setPixmap(QPixmap(path))

    # change nation
    def changeNation(self):
        # flag
        if doFlags:
            self.nation.setText("Нация")
            with open(path_settings) as f:
                data = json.load(f)
            path = data["flags_path"]
            if self.nations.currentText() == "СССР":
                path += "USSR_flag.png"
            elif self.nations.currentText() == "США":
                path += "USA_flag.png"
            elif self.nations.currentText() == "Германия":
                path += "GERM_flag.png"
            else:
                path = ""
            self.nation.setPixmap(QPixmap(path))

    # check all CHB
    def chacked_all(self, state, who):
        if who == "LVL":
            for i in self.all_LVL[1:]:
                i.setChecked(state)
        elif who == "TYPE":
            for i in self.all_TYPE[1:]:
                i.setChecked(state)

    # update all element in the filter
    def UpdateFilter(self):
        # all CHB
        self.all_LVL = [self.rbtn_lvl_all, self.chb_lvl_1, self.chb_lvl_2, self.chb_lvl_3,
                        self.chb_lvl_4, self.chb_lvl_5, self.chb_lvl_6, self.chb_lvl_7]
        self.all_TYPE = [self.rbtn_type_all, self.chb_type_lt, self.chb_type_st, self.chb_type_tt,
                         self.chb_type_ptsay, self.chb_type_it, self.chb_type_zsu, self.chb_type_zprk_zrk, ]

        # set Checked CHB (Prime/Polk)
        self.chb_primet.setChecked(PrimeT)
        self.chb_polkt.setChecked(PolkT)

        # change allCHB
        for index, name in enumerate(self.all_LVL[1:]):
            name.setChecked(LVL_T[index])
        for index, name in enumerate(self.all_TYPE[1:]):
            name.setChecked(TYPE_T[index])

        # checked RBTN
        self.all_LVL[0].setChecked(True) if all(LVL_T) else self.all_LVL[0].setChecked(False)
        self.all_TYPE[0].setChecked(True) if all(TYPE_T) else self.all_TYPE[0].setChecked(False)

        # Kol Tech
        self.numb.setValue(KolT)

        # Nathions
        self.nations.setCurrentText(Nath)

    # func. open CreateForm "SetUP"
    def open_CreateForm(self):
        Create_SetUP().show()

    # func. open SettingsForm Dialog
    def open_SettingsForm(self):
        Settings_Form().exec()

    # func. load SetUP
    def open_LoadDialog(self):
        # debug
        print("class MainProgramm > def open_LoadDialog  -  load...") if DebugMod else print()

        # write in log
        with open(log_file_path, "a", encoding="utf-8") as log_file:  # write in log
            print("class MainProgramm > def open_LoadDialog  -  load...", file=log_file)  # log

        # load file
        path_SetUP_file = QFileDialog.getOpenFileName(self, 'Выбрать SetUp', '',
                                                      'SetUp (*.db);;DataBase (*.db);;Все файлы (*)')[0]

        # check correction
        if path_SetUP_file[-9:] == "_DBWTR.db":
            with open(path_settings) as s:
                data = json.load(s)
                data["SetUP_path"] = path_SetUP_file
                with open(path_settings, "w") as s:
                    json.dump(data, s, indent=4)

            # debug
            print("class MainProgramm > def open_LoadDialog  -  load success") if DebugMod else print()  # debug
            print("class MainProgramm > def open_LoadDialog  -  settings changes") if DebugMod else print()  # debug

            # write in log
            with open(log_file_path, "a", encoding="utf-8") as log_file:  # write in log as log_file:
                print("class MainProgramm > def open_LoadDialog  -  load success", file=log_file)  # log
                print("class MainProgramm > def open_LoadDialog  -  settings changes", file=log_file)  # log

        else:
            # Failed message
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            if DarkTheme:
                msg.setStyleSheet("background-color: rgb(25, 0, 97);" "color: rgb(255, 255, 255);")
            msg.setText("Укажите файл правильного формата \nПример: FirstSETUP_DBWTR.db")
            msg.setWindowTitle("Ошибка")
            msg.exec_()

            # debug
            print("class MainProgramm > def open_LoadDialog  -  load failed(bed format)") if DebugMod else print()

            # write in log
            with open(log_file_path, "a", encoding="utf-8") as log_file:  # write in log as log_file:
                print("class MainProgramm > def open_LoadDialog  -  load failed(bed format)", file=log_file)  # log

    # close Event
    def closeEvent(self, event):
        # save Filter to Settings.json
        with open(path_settings) as s:
            data = json.load(s)
            data["Nation"] = self.nations.currentText()
            data['PrimeT'] = True if self.chb_primet.isChecked() else False
            data['PolkT'] = True if self.chb_polkt.isChecked() else False
            data["LVL"] = [True if i.isChecked() else False for i in self.all_LVL[1:]]
            data["TYPE"] = [True if i.isChecked() else False for i in self.all_TYPE[1:]]
            data["Number"] = int(self.numb.value())
            with open(path_settings, "w") as s:
                json.dump(data, s, indent=4)

        # debug
        print("class MainProgramm > def closeEvent  -  settings changes") if DebugMod else print()

        # write in log
        with open(log_file_path, "a", encoding="utf-8") as log_file:  # write in log
            print("Close programm - " + str(datetime.datetime.now()), file=log_file)  # log

    # Func. Random
    def Random(self):
        # staff list
        all_lvl = [i2 if i.isChecked() else None for i2, i in enumerate(self.all_LVL[1:], start=1)]
        all_type = [i2 if i.isChecked() else None for i2, i in enumerate(self.all_TYPE[1:], start=1)]
        chb_prime = True if self.chb_primet.isChecked() else False
        chb_polk = True if self.chb_polkt.isChecked() else False
        nation = self.nations.currentText()
        numb = self.numb.value()
        on = var = True
        self.res = []

        # check any parameter filter on
        if not (any(all_lvl) and any(all_type)):
            on = False
            # Messege
            msg = QMessageBox()
            if DarkTheme:
                msg.setStyleSheet("background-color: rgb(25, 0, 97);" "color: rgb(255, 255, 255);")
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Пожалуйста!\nУкажите хотя бы один параметр(LVL, Тип техники)")
            msg.setWindowTitle("Ошибка!")
            msg.exec_()

            # debug
            print("WARNING class Main > def Random  -  note parameter") if DebugMod else print()

            # write in log
            with open(log_file_path, "a", encoding="utf-8") as log_file:  # write in log
                print("WARNING class Main > def Random  -  note parameter", file=log_file)  # log

        # connect to DB
        con = sqlite3.connect(path_SetUP_file)
        cur = con.cursor()

        # execute all tanks were parameter on
        if nation == "СССР" and on:
            for i in all_type:
                for i2 in all_lvl:
                    # take result in DB
                    self.res.extend(cur.execute(
                        """SELECT * FROM USSR_tanks WHERE type == ? AND lvl == ?;""", (i, i2)).fetchall())

            # check correcthin random
            if len(self.res) != 0 and numb <= len(self.res):
                Result_Form(chb_prime, chb_polk, numb, self.res).exec()
            else:
                # error message
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                if DarkTheme:
                    msg.setStyleSheet("background-color: rgb(25, 0, 97);" "color: rgb(255, 255, 255);")
                msg.setText(
                    "В выбранной нации этого SetUp'a нет технкики \nИЛИ\nВ выбранном SetUp'e нехватает технкики для подбора")
                msg.setWindowTitle("Ошибка!")
                msg.exec_()

                # debug
                print(
                    "WARNING class Main > def Random  -  not tech in SetUp or deficit tech for random") if DebugMod else print()

                # write in log
                with open(log_file_path, "a", encoding="utf-8") as log_file:  # write in log
                    print("WARNING class Main > def Random  -  not tech in SetUp or deficit tech for random",
                          file=log_file)  # log

        elif nation == "США" and on:
            for i in all_type:
                for i2 in all_lvl:
                    # take result in DB
                    self.res.extend(cur.execute(
                        """SELECT * FROM USA_tanks WHERE type == ? AND lvl == ?;""", (i, i2)).fetchall())
            # check correcthin random
            if len(self.res) != 0 and numb <= len(self.res):
                Result_Form(chb_prime, chb_polk, numb, self.res).exec()
            else:
                # error message
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                if DarkTheme:
                    msg.setStyleSheet("background-color: rgb(25, 0, 97);" "color: rgb(255, 255, 255);")
                msg.setText(
                    "В выбранной нации этого SetUp'a нет технкики \nИЛИ\nВ выбранном SetUp'e нехватает технкики для подбора")
                msg.setWindowTitle("Ошибка!")
                msg.exec_()

                # debug
                print(
                    "WARNING class Main > def Random  -  not tech in SetUp or deficit tech for random") if DebugMod else print()

                # write in log
                with open(log_file_path, "a", encoding="utf-8") as log_file:  # write in log
                    print("WARNING class Main > def Random  -  not tech in SetUp or deficit tech for random",
                          file=log_file)  # log

        elif nation == "Германия" and on:
            for i in all_type:
                for i2 in all_lvl:
                    # take result in DB
                    self.res.extend(cur.execute(
                        """SELECT * FROM GERMANY_tanks WHERE type == ? AND lvl == ?;""", (i, i2)).fetchall())
            # check correcthin random

            if len(self.res) != 0 and numb <= len(self.res):
                Result_Form(chb_prime, chb_polk, numb, self.res).exec()
            else:
                # error message
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                if DarkTheme:
                    msg.setStyleSheet("background-color: rgb(25, 0, 97);" "color: rgb(255, 255, 255);")
                msg.setText(
                    "В выбранной нации этого SetUp'a нет технкики \nИЛИ\nВ выбранном SetUp'e нехватает технкики для подбора")
                msg.setWindowTitle("Ошибка!")
                msg.exec_()

                # debug
                print(
                    "WARNING class Main > def Random  -  not tech in SetUp or deficit tech for random") if DebugMod else print()

                # write in log
                with open(log_file_path, "a", encoding="utf-8") as log_file:  # write in log
                    print("WARNING class Main > def Random  -  not tech in SetUp or deficit tech for random",
                          file=log_file)  # log

        elif nation == "Не выбрано":
            # error message
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            if DarkTheme:
                msg.setStyleSheet("background-color: rgb(25, 0, 97);" "color: rgb(255, 255, 255);")
            msg.setText("Пожалуйста, укажите нацию ")
            msg.setWindowTitle("Ошибка!")
            msg.exec_()

            # debug
            print("WARNING class Main > def Random  -  note choose nation") if DebugMod else print()

            # write in log
            with open(log_file_path, "a", encoding="utf-8") as log_file:  # write in log
                print("WARNING class Main > def Random  -  note choose nation", file=log_file)  # log

        # debug
        print("class Main > def Random  -  result > " + str(self.res)) if DebugMod else print()

        # write in log
        with open(log_file_path, "a", encoding="utf-8") as log_file:  # write in log
            print("class Main > def Random  -  result > " + str(self.res), file=log_file)  # log


# Create SetUP
class Create_SetUP(QDialog):
    def __init__(self):
        super().__init__()
        # global
        global path_standartDB
        global CreateSetup_path
        global path_SetUP_file
        global doMoreInf
        global doFlags

        # style Window
        #logo
        with open(path_settings) as f:
            data = json.load(f)
            self.setWindowIcon(QtGui.QIcon(data["logo_path"]))
        # Ui
        uic.loadUi(CreateSetup_path, self)
        self.setWindowTitle('Создать SetUP')

        # theme
        if DarkTheme:
            self.setStyleSheet("background-color: rgb(25, 0, 97); color: rgb(255, 255, 255);")
            self.btn_saveAll.setStyleSheet(
                "background-color: rgb(53, 0, 211);" "border-width: 2px;" "border-radius: 10px;")
            self.nations.setStyleSheet(
                "background-color: rgb(53, 0, 211);" "border-radius: 3px;" "padding: 1px 18px 1px 3px;" "min-width: 6em;")

        # staff
        self.all_chb = []  # all checkBox
        self.result = []  # result db
        self.c = False
        self.ussr = []
        self.usa = []
        self.germ = []

        # functions
        self.create()  # func.
        self.nations.activated.connect(self.change_nationToCHB)  # func. change nation
        self.rbtn_all.toggled.connect(lambda state: self.chaked_all(state))  # func. rbtn
        self.btn_saveAll.clicked.connect(self.save_all)  # save all tanks

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
        self.rbtn_all = QRadioButton("ВСЕ", self)  # crate radioBatton "all"

        # theme
        if DarkTheme:
            self.rbtn_all.setStyleSheet("background-color: rgb(36, 0, 144);" "padding: 2px;" "padding-left: 5px;")

        # Create allaCHB
        self.rbtn_all.setVisible(False)  # make rbtn anVisible
        self.vbox.addWidget(self.rbtn_all)  # add in widget rbtn
        self.all_chb.append(self.rbtn_all)  # add in list rbtn
        # CHB
        for i in range(1, 150):
            object = QCheckBox("chb_" + str(i))
            object.setVisible(False)
            # theme
            if DarkTheme:
                object.setStyleSheet("background-color: rgb(36, 0, 144);" "padding: 2px;" "padding-left: 5px;")
            object.toggled.connect(self.save_nationToSetup)
            self.vbox.addWidget(object)
            self.all_chb.append(object)
        self.widget.setLayout(self.vbox)
        # add widget to scrollArea
        self.scrollArea_3.setWidget(self.widget)

    # change nation on CHB and rename his
    def change_nationToCHB(self):
        # flag
        if doFlags:
            with open(path_settings) as f:
                data = json.load(f)
            path = data["flags_path"]
            if self.nations.currentText() == "СССР":
                path += "USSR_flag.png"
            elif self.nations.currentText() == "США":
                path += "USA_flag.png"
            elif self.nations.currentText() == "Германия":
                path += "GERM_flag.png"
            else:
                path = ""
                self.nation.setText("Нация")
            self.nation.setPixmap(QPixmap(path))

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
            self.result = cur.execute("""SELECT
             GERMANY_tanks.id, GERMANY_tanks.name, type.title, GERMANY_tanks.BR, GERMANY_tanks.lvl
              FROM GERMANY_tanks INNER JOIN type ON type.id = GERMANY_tanks.type 
              ORDER BY GERMANY_tanks.id;""").fetchall()  # take all "GERMANY tanks
            self.c = True
        elif self.nations.currentText() == "СССР":
            self.result = cur.execute("""SELECT
             USSR_tanks.id, USSR_tanks.name, type.title, USSR_tanks.BR, USSR_tanks.lvl
              FROM USSR_tanks INNER JOIN type ON type.id = USSR_tanks.type 
              ORDER BY USSR_tanks.id;""").fetchall()  # take all "USSR" tanks
            self.c = True
        elif self.nations.currentText() == "США":
            self.result = cur.execute("""SELECT
             USA_tanks.id, USA_tanks.name, type.title, USA_tanks.BR, USA_tanks.lvl
              FROM USA_tanks INNER JOIN type ON type.id = USA_tanks.type 
              ORDER BY USA_tanks.id;""").fetchall()  # take all "USA" tanks
            self.c = True

        # rename CHB
        if self.c:
            self.rbtn_all.setVisible(True)  # make rbtn Visible
            for key, i in enumerate(self.all_chb[1:len(self.result) + 1]):
                i.setVisible(True)  # make CHB Visible
                if doMoreInf:  # if MoreInformathion include:
                    i.setText(f"{self.result[key][1]}"
                              f"\nТип - {self.result[key][2]} \t\tБр - {self.result[key][3]} \t\tЛВЛ - {self.result[key][4]}\n")
                else:
                    i.setText(str(self.result[key][1]))  # if MoreInformathion not include:
        self.all_chb[1].setChecked(True)

    # save nation to 1/3 SetUp'a
    def save_nationToSetup(self):
        # add tanks
        if self.nations.currentText() == "СССР":
            self.ussr = []
            for i in self.all_chb[1:]:
                if i.isChecked() == True:
                    self.ussr.append(i.text().split("\n")[0])

            # debug
            print("Ussr tanks - " + str(self.ussr)) if DebugMod else print()

            # write in log
            with open(log_file_path, "a", encoding="utf-8") as log_file:  # write in log as log_file:
                print("Ussr tanks - " + str(self.ussr), file=log_file)

        elif self.nations.currentText() == "Германия":
            self.germ = []
            for i in self.all_chb[1:]:
                if i.isChecked() == True:
                    self.germ.append(i.text().split("\n")[0])

            # debug
            print("Germany tanks - " + str(self.germ)) if DebugMod else print()

            # write in log
            with open(log_file_path, "a", encoding="utf-8") as log_file:  # write in log as log_file:
                print("Germany tanks - " + str(self.germ), file=log_file)

        elif self.nations.currentText() == "США":
            self.usa = []
            for i in self.all_chb[1:]:
                if i.isChecked() == True:
                    self.usa.append(i.text().split("\n")[0])

            # debug
            print("Usa tanks - " + str(self.usa)) if DebugMod else print()

            # write in log
            with open(log_file_path, "a", encoding="utf-8") as log_file:  # write in log as log_file:
                print("Usa tanks - " + str(self.usa), file=log_file)

    # func. save all
    def save_all(self):
        # debug
        print("class Create_SetUP > def save_all  -  download...") if DebugMod else print()

        # write in log
        with open(log_file_path, "a", encoding="utf-8") as log_file:  # write in log as log_file:
            print("class Create_SetUP > def save_all  -  download...", file=log_file)  # log

        # try downLoad file
        try:
            f = open(r'DB/' + str(self.takeName.text()) + '_DBWTR.db', "wb")  # create file

            # open settings,json
            with open(path_settings) as file:
                data = json.load(file)
            ufr = requests.get(data["GitHubLink_clearDB"])  # download file
            f.write(ufr.content)  # write to file
            f.close()

            # debug
            print("class Create_SetUP > def save_all  -  success download!") if DebugMod else print()

            # write in log
            with open(log_file_path, "a", encoding="utf-8") as log_file:  # write in log as log_file:
                print("class Create_SetUP > def save_all  -  success download!", file=log_file)  # log

            # success message
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            if DarkTheme:
                msg.setStyleSheet("background-color: rgb(25, 0, 97);" "color: rgb(255, 255, 255);")
            msg.setText("Успешное создание SetUP'a !")
            msg.setWindowTitle("Успех")
            msg.exec_()

            path_SetUP_file = 'DB/' + str(self.takeName.text()) + '_DBWTR.db'  # name of "newDB"

            # change path in Settings.json
            with open(path_settings) as f:
                data = json.load(f)
                data["SetUP_path"] = path_SetUP_file
                with open(path_settings, "w") as f:
                    json.dump(data, f, indent=4)

            # debug
            print("class Create_SetUP > def save_all  -  settings changes") if DebugMod else print()

            # write in log
            with open(log_file_path, "a", encoding="utf-8") as log_file:  # write in log as log_file:
                print("class Create_SetUP > def save_all  -  settings changes", file=log_file)  # log

        except Exception:
            # debug
            print("ERROR! class Create_SetUP > def save_all  -  download Failed") if DebugMod else print()

            # write in log
            with open(log_file_path, "a", encoding="utf-8") as log_file:  # write in log as log_file:
                print("ERROR! class Create_SetUP > def save_all  -  download Failed", file=log_file)  # log

            # failed message
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            if DarkTheme:
                msg.setStyleSheet("background-color: rgb(25, 0, 97);" "color: rgb(255, 255, 255);")
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
        with open(path_settings) as f:
            data = json.load(f)
        if len(self.ussr) != 0:
            for i in self.ussr:
                result = cur2.execute("""SELECT * FROM USSR_tanks WHERE name == ?;""",
                                      (i,)).fetchall()  # take all USSR tanks
                result = list(result[0]) if len(result) != 0 else []
                cur1.execute("""INSERT INTO USSR_tanks(id,name,type,lvl,BR,link) VALUES(?,?,?,?,?,?)""",
                             (result[0], result[1], result[2], result[3], result[4], result[5]),)

        if len(self.usa) != 0:
            for i in self.usa:
                result = cur2.execute("""SELECT * FROM USA_tanks WHERE name == ?;""",
                                      (i,)).fetchall()  # take all USA tanks
                result = list(result[0]) if len(result) != 0 else []
                cur1.execute("""INSERT INTO USA_tanks(id,name,type,lvl,BR,link) VALUES(?,?,?,?,?,?)""",
                             (result[0], result[1], result[2], result[3], result[4], result[5]),)
        if len(self.germ) != 0:
            for i in self.germ:
                result = cur2.execute("""SELECT * FROM GERMANY_tanks WHERE name == ?;""",
                                      (i,)).fetchall()  # take all GERMANY tanks
                result = list(result[0]) if len(result) != 0 else []
                cur1.execute("""INSERT INTO GERMANY_tanks(id,name,type,lvl,BR,link) VALUES(?,?,?,?,?,?)""",
                             (result[0], result[1], result[2], result[3], result[4], result[5]),)

        # disconect DB
        con1.commit()
        con1.close()
        con2.commit()
        con2.close()


# Settings
class Settings_Form(QDialog):
    def __init__(self):
        super().__init__()
        # global
        global SettingsForm_path
        global log_file_path
        global path_settings
        global doFlags

        # stye Window
        # load logo
        with open(path_settings) as f:
            data = json.load(f)
            self.setWindowIcon(QtGui.QIcon(data["logo_path"]))
        # UI
        uic.loadUi(SettingsForm_path, self)
        self.setWindowTitle('Настройки')

        # Theme
        if DarkTheme:
            self.setStyleSheet("background-color: rgb(25, 0, 97); color: rgb(255, 255, 255);")
            for i in [self.btn_dloud, self.tBtn_SetUP, self.tBtn_StandartDB]:
                i.setStyleSheet(
                    "background-color: rgb(53, 0, 211);" "border-width: 2px;" "border-radius: 10px;")
            for i in [self.chb_FlagVisible, self.chb_doMoreInf, self.chb_theme]: i.setStyleSheet("background-color:rgb(36, 0, 144)")

        # options
        self.tBtn_StandartDB.clicked.connect(self.Update_StandartDB)
        self.tBtn_SetUP.clicked.connect(self.Update_SetUP)
        self.chb_FlagVisible.toggled.connect(lambda state: self.Flags(state))
        self.chb_doMoreInf.toggled.connect(lambda state: self.MoreINF(state))
        self.chb_theme.setChecked(DarkTheme)
        self.chb_theme.toggled.connect(lambda state: self.SwichTheme(state))

        # download DB
        self.btn_dloud.clicked.connect(self.Download_DB)

        # update inf.
        self.Path_standartBD.setText(str(path_standartDB))
        self.Path_SetUP.setText(str(path_SetUP_file))
        self.chb_FlagVisible.setChecked(doFlags)
        self.chb_doMoreInf.setChecked(doMoreInf)

    # SwichTheme
    def SwichTheme(self, state):
        global DarkTheme

        # success message
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        if DarkTheme:
            msg.setStyleSheet("background-color: rgb(25, 0, 97);" "color: rgb(255, 255, 255);")
        msg.setText("Успех")
        msg.setInformativeText('Настройки Темы вступят в силу после перезапуска программы или ее окон')
        msg.setWindowTitle("Успех")
        msg.exec_()

        DarkTheme = state
        with open(path_settings) as f:
            data = json.load(f)
            data["Theme"] = state
            with open(path_settings, "w") as f:
                json.dump(data, f, indent=4)

        # debug
        print("Theme State  -  " + str(state)) if DebugMod else print()
        print("class Settings_Form > def SwichTheme  -  settings changes") if DebugMod else print()

        # write in log
        with open(log_file_path, "a", encoding="utf-8") as log_file:  # write in log as log_file:
            print("Theme State  -  " + str(state), file=log_file)
            print("class Settings_Form > def SwichTheme  -  settings changes", file=log_file)  # log

    # flags
    def Flags(self, state):
        # debug
        print("Flag State  -  " + str(state)) if DebugMod else print()

        # write in log
        with open(log_file_path, "a", encoding="utf-8") as log_file:  # write in log as log_file:
            print("Flag State  -  " + str(state), file=log_file)

        doFlags = state

        # cahnge flagState in Setting.json
        with open(path_settings) as f:
            data = json.load(f)
            data["Flags"] = doFlags
            with open(path_settings, "w") as f:
                json.dump(data, f, indent=4)

        # debug
        print("class Settings_Form > def Flags  -  settings changes") if DebugMod else print()

        # write in log
        with open(log_file_path, "a", encoding="utf-8") as log_file:  # write in log as log_file:
            print("class Settings_Form > def Flags  -  settings changes", file=log_file)  # log

    # More Informathion SetUP
    def MoreINF(self, state):
        global doMoreInf
        global log_file_path

        # debug
        print("MoreInf State  -  " + str(state)) if DebugMod else print()

        # write in log
        with open(log_file_path, "a", encoding="utf-8") as log_file:  # write in log as log_file:
            print("MoreInf State  -  " + str(state), file=log_file)

        doMoreInf = state

        # change MoreInf State in settings.json
        with open(path_settings) as f:
            data = json.load(f)
            data["MoreInf"] = doMoreInf
            with open(path_settings, "w") as f:
                json.dump(data, f, indent=4)

        # debug
        print("class Settings_Form > def MoreINF  -  settings changes") if DebugMod else print()

        # write in log
        with open(log_file_path, "a", encoding="utf-8") as log_file:  # write in log as log_file:
            print("class Settings_Form > def MoreINF  -  settings changes", file=log_file)  # log

    # update path of StandartDB
    def Update_StandartDB(self):
        # load file
        path_standartDB = QFileDialog.getOpenFileName(self, 'Выбрать SetUp', '',
                                                      'SetUp (*.db);;DataBase (*.db);;Все файлы (*)')[0]
        self.Path_standartBD.setText(str(path_standartDB))  # change path

        # change path in setting.json
        with open(path_settings) as f:
            data = json.load(f)
            data["standartDB_path"] = path_standartDB
            with open(path_settings, "w") as f:
                json.dump(data, f, indent=4)

        # debug
        print("class Settings_Form > def Update_StandartDB  -  settings changes") if DebugMod else print()

        # write in log
        with open(log_file_path, "a", encoding="utf-8") as log_file:  # write in log as log_file:
            print("class Settings_Form > def Update_StandartDB  -  settings changes", file=log_file)  # log

    # update path of StandartDB
    def Update_SetUP(self):
        global log_file  # take logFile

        # laod file
        path_SetUP_file = QFileDialog.getOpenFileName(self, 'Выбрать SetUp', "",
                                                      'SetUp (*.db);;DataBase (*.db);;Все файлы (*)')[0]
        self.Path_SetUP.setText(str(path_SetUP_file))  # change path

        # change path in setting.json
        with open(path_settings) as f:
            data = json.load(f)
            data["SetUP_path"] = path_standartDB
            with open(path_settings, "w") as f:
                json.dump(data, f, indent=4)

        # debug
        print("class Settings_Form > def Update_SetUP  -  settings changes") if DebugMod else print()

        # write in log
        with open(log_file_path, "a", encoding="utf-8") as log_file:  # write in log as log_file:
            print("class Settings_Form > def Update_SetUP  -  settings changes", file=log_file)  # log

    # download StandartDataBase
    def Download_DB(self):
        # debug
        print("class Settings_Form > def Download_DB  -  download...") if DebugMod else print()

        # write in log
        with open(log_file_path, "a", encoding="utf-8") as log_file:  # write in log as log_file:
            print("class Settings_Form > def Download_DB  -  download...", file=log_file)  # log

        # try downLoad file
        try:
            f = open(r'DB/standart_DBWTR.db', "wb")  # create file

            # take GH link to downLoad file
            with open(path_settings) as file:
                data = json.load(file)
            ufr = requests.get(data["GitHubLink_standartDB"])  # download file
            f.write(ufr.content)  # write to file
            f.close()

            # update path
            path_standartDB = 'DB/standart_DBWTR.db'

            # debug
            print("class Settings_Form > def Download_DB  -  success download!") if DebugMod else print()

            # write in log
            with open(log_file_path, "a", encoding="utf-8") as log_file:  # write in log as log_file:
                print("class Settings_Form > def Download_DB  -  success download!", file=log_file)  # log

            # success message
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            # theme
            if DarkTheme:
                msg.setStyleSheet("background-color: rgb(25, 0, 97);" "color: rgb(255, 255, 255);")
            msg.setText("Успешное скачивание!")
            msg.setWindowTitle("Успех")
            msg.exec_()

            # change path in setting.json
            with open(path_settings) as f:
                data = json.load(f)
                data["standartDB_path"] = path_standartDB
                with open(path_settings, "w") as f:
                    json.dump(data, f, indent=4)

            self.Path_standartBD.setText(str(path_standartDB))  # change path

            # debug
            print("class Settings_Form > def Download_DB  -  settings changes") if DebugMod else print()

            # write in log
            with open(log_file_path, "a", encoding="utf-8") as log_file:  # write in log as log_file:
                print("class Settings_Form > def Download_DB  -  settings changes", file=log_file)  # log

        except Exception:
            # debug
            print("ERROR! class Settings > def Download_DB  -  download Failed") if DebugMod else print()

            # write in log
            with open(log_file_path, "a", encoding="utf-8") as log_file:  # write in log as log_file:
                print("ERROR! class Settings > def Download_DB  -  download Failed", file=log_file)  # log

            # failed message
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Непредвиденная ошибка!")
            # theme
            if DarkTheme:
                msg.setStyleSheet("background-color: rgb(25, 0, 97);" "color: rgb(255, 255, 255);")
            msg.setInformativeText('Проверьте подключение к Интернету')
            msg.setWindowTitle("Ошибка")
            msg.exec_()


# result
class Result_Form(QDialog):
    def __init__(self, chb_prime, chb_polk, numb, res):
        super().__init__()
        # global
        global ResultForm_path

        # style Window
        # load logo
        with open(path_settings) as f:
            data = json.load(f)
            self.setWindowIcon(QtGui.QIcon(data["logo_path"]))
        #UI
        uic.loadUi(ResultForm_path, self)
        self.windowTitle('Результаты')
        # theme
        if DarkTheme:
            self.setStyleSheet("background-color:rgb(36, 0, 144)")

        # import filters an all tanks
        self.chb_prime = chb_prime
        self.chb_polk = chb_polk
        self.numb = numb
        self.res = res

        # import all tanks for filters(polk, prime
        self.links = [i[-1] for i in self.res]
        for i in self.links:
            if i[:2] == "@_" and not self.chb_polk:
                self.links.remove(i)
            elif i[:2] == "$_" and not self.chb_prime:
                self.links.remove(i)

        # debug
        print("class Result_Form > def Random  -  result links > " + str(self.res)) if DebugMod else print()

        # write in log
        with open(log_file_path, "a", encoding="utf-8") as log_file:  # write in log
            print("class Result_Form > def Random  -  result links > " + str(self.res), file=log_file)  # log

        a = []
        n = []

        # create label*9 and make anVisible
        for i in range(1, 4):
            for i2 in range(1, 4):
                object = QLabel("label")
                object.resize(300, 70)
                object.setVisible(False)
                a.append(object)
                self.test.addWidget(object, i, i2)
                self.setLayout(self.test)

        # random links
        while len(n) != self.numb:
            r = random.randrange(1, len(self.links) + 1)
            if r not in n:
                n.append(r)

        # loadpath
        with open(path_settings) as f:
            data = json.load(f)

        # SetPixmap for label
        for i in range(0, self.numb):
            link = n[i]
            a[i].setPixmap(QPixmap(str(data["ImageTank_path"]) + str(self.links[link - 1])))
            a[i].setVisible(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainProgramm()
    ex.show()
    sys.exit(app.exec())
