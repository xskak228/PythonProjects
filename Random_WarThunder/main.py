import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
from random import choices


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('WarThunder_random_2.0_test.ui', self)  # Загружаем дизайн
        self.initUI()
        self.p1_k = 0
        self.list_return = []
        self.out = ""

        # список списков для функции "enable_all", "check_enable"  _________ 0-t,ussr 1-t,usa 2-l,ussr 3-l,usr
        self.c_lvl_tech = [[self.p1_tech_ussr_t34, self.p1_tech_ussr_su100, self.p1_tech_ussr_is2,
                            self.p1_tech_ussr_is3, self.test1, self.test2, self.test3],
                           [self.p1_tech_usa_m24, self.p1_tech_usa_m48, self.p1_tech_usa_m4a3,
                            self.p1_tech_usa_m4a3e2, self.test1_2, self.test2_2, self.test3_2],
                           [self.p1_lvl_ussr_1, self.p1_lvl_ussr_2, self.p1_lvl_ussr_3, self.p1_lvl_ussr_4,
                            self.p1_lvl_ussr_5, self.p1_lvl_ussr_6, self.p1_lvl_ussr_7],
                           [self.p1_lvl_usa_1, self.p1_lvl_usa_2, self.p1_lvl_usa_3, self.p1_lvl_usa_4,
                           self.p1_lvl_usa_5, self.p1_lvl_usa_6, self.p1_lvl_usa_7]]


    def initUI(self):
        self.LVL.setEnabled(False)

        # ___________________переключатели________________________
        self.p1_play.stateChanged.connect(lambda state: self.enable_p1(state))          # пер. p1(on/off)
        self.p1_tr_tanks.toggled.connect(lambda state: self.enable_tanks(state))        # пер. тип подбора p1_lvl/tanks
        self.p1_n_ussr.toggled.connect(lambda state: self.enable_nation(state))         # пер. нации p1_ussr/usa

        # ___________________выбор всей(-х) техники/уровня________
        self.p1_tech_ussr_all.toggled.connect(lambda state: self.enable_all(state, "ussr", "tech"))
        self.p1_tech_usa_all.toggled.connect(lambda state: self.enable_all(state, "usa", "tech"))
        self.p1_lvl_ussr_all.toggled.connect(lambda state: self.enable_all(state, "ussr", "lvl"))
        self.p1_lvl_usa_all.toggled.connect(lambda state: self.enable_all(state, "usa", "lvl"))

        # ___________________кнопка генерации_____________________
        self.btn_random.clicked.connect(self.random)

    # ____________переключатели__________________________
    def enable_p1(self, state):
        self.p1_nickname.setEnabled(state)
        self.p1_n_usa.setEnabled(state)
        self.p1_n_ussr.setEnabled(state)
        self.p1_tr_lvl.setEnabled(state)
        self.p1_tr_tanks.setEnabled(state)
        self.p1_output.setEnabled(state)
        self.p1_numb_tech.setEnabled(state)
        self.label_k_p1.setEnabled(state)
        self.p1_tech_lvl_nathions.setEnabled(state)

    def enable_tanks(self, state):
        self.Tanks.setEnabled(state)
        self.LVL.setEnabled(not state)

    def enable_nation(self, state):
        self.tech_ussr.setEnabled(state)
        self.tech_usa.setEnabled(not state)
        self.lvl_ussr.setEnabled(state)
        self.lvl_usa.setEnabled(not state)

    # ____________проверка включенных в подбор техники___
    def check_enable(self, rt, n):
        self.list_return = []
        if rt == "tanks":
            if n == "ussr":
                for i in self.c_lvl_tech[0]:
                    if i.isChecked():
                        self.list_return.append(str(i.text()))
                return self.list_return
            elif n == "usa":
                for i in self.c_lvl_tech[1]:
                    if i.isChecked():
                        self.list_return.append(str(i.text()))
                return self.list_return
        elif rt == "lvl":
            if n == "ussr":
                for i in self.c_lvl_tech[2]:
                    if i.isChecked():
                        self.list_return.append(str(i.text()))
                return self.list_return
            elif n == "usa":
                for i in self.c_lvl_tech[3]:
                    if i.isChecked():
                        self.list_return.append(str(i.text()))
                return self.list_return

    # ____________рандомайзер____________________________
    def random(self):
        if self.p1_play.stateChanged:
            self.p1_k = int(self.p1_numb_tech.text())
            if self.p1_tr_tanks.isChecked():
                if self.p1_n_ussr.isChecked():
                    self.update_gen(choices(self.check_enable("tanks", "ussr"), k=self.p1_k), "USSR", "TANKS")
                elif self.p1_n_usa.isChecked():
                    self.update_gen(choices(self.check_enable("tanks", "usa"), k=self.p1_k), "USA", "TANKS")
            elif self.p1_tr_lvl.isChecked():
                if self.p1_n_ussr.isChecked():
                    self.update_gen(choices(self.check_enable("lvl", "ussr"), k=self.p1_k), "USSR", "LVL")
                elif self.p1_n_usa.isChecked():
                    self.update_gen(choices(self.check_enable("lvl", "usa"), k=self.p1_k), "USA", "LVL")

    # _________выбор всей(-х) техники/уровней_____________
    def enable_all(self, state, n, tr):
        if n == "ussr" and tr == "tech":
            for i in self.c_lvl_tech[0]:
                i.setChecked(state)
        elif n == "ussr" and tr == "lvl":
            for i in self.c_lvl_tech[2]:
                i.setChecked(state)

        if n == "usa" and tr == "tech":
            for i in self.c_lvl_tech[1]:
                i.setChecked(state)
        elif n == "usa" and tr == "lvl":
            for i in self.c_lvl_tech[3]:
                i.setChecked(state)

    # ________вывести на экранрезультат подбора__________
    def update_gen(self, list1, n, t):
        self.out = ""
        self.out += f"NickName: {str(self.p1_nickname.text())}\nНация: {n}\nТип подбора: {t}\n\n"
        for i, k in enumerate(list1, start=1):
            self.out += f"{i}) {k}\n"
        self.p1_output.setText(self.out)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())