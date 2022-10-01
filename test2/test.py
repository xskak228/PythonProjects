import sys

from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from random import sample


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('test.ui', self)  # Загружаем дизайн
        self.initUI()

        self.k = 0
        self.p1_out = []


        # список всех кнопок
        self.p1_btns = [self.checkBox_0001, self.checkBox_0002, self.checkBox_0003, self.checkBox_0004,
                        self.checkBox_0005, self.checkBox_0006, self.checkBox_0007, self.checkBox_0008,
                        self.checkBox_0009, self.checkBox_0010, self.checkBox_0011, self.checkBox_0012,
                        self.checkBox_0013, self.checkBox_0014, self.checkBox_0015, self.checkBox_0016,
                        self.checkBox_0017, self.checkBox_0018, self.checkBox_0019, self.checkBox_0020,
                        self.checkBox_0021, self.checkBox_0022, self.checkBox_0023, self.checkBox_0024,
                        self.checkBox_0025, self.checkBox_0026, self.checkBox_0027, self.checkBox_0028,
                        self.checkBox_0029, self.checkBox_0030, self.checkBox_0031, self.checkBox_0032,
                        self.checkBox_0033, self.checkBox_0034, self.checkBox_0035, self.checkBox_0036,
                        self.checkBox_0037, self.checkBox_0038, self.checkBox_0039, self.checkBox_0040,
                        self.checkBox_0041, self.checkBox_0042, self.checkBox_0043, self.checkBox_0044,
                        self.checkBox_0045, self.checkBox_0046, self.checkBox_0047, self.checkBox_0048,
                        self.checkBox_0049, self.checkBox_0050, self.checkBox_0051, self.checkBox_0052,
                        self.checkBox_0053, self.checkBox_0054, self.checkBox_0055, self.checkBox_0056,
                        self.checkBox_0057, self.checkBox_0058, self.checkBox_0059, self.checkBox_0060,
                        self.checkBox_0061, self.checkBox_0062, self.checkBox_0063, self.checkBox_0064,
                        self.checkBox_0065, self.checkBox_0066, self.checkBox_0067, self.checkBox_0068,
                        self.checkBox_0069, self.checkBox_0070, self.checkBox_0071, self.checkBox_0072,
                        self.checkBox_0073, self.checkBox_0074, self.checkBox_0075, self.checkBox_0076,
                        self.checkBox_0077, self.checkBox_0078, self.checkBox_0079, self.checkBox_0080,
                        self.checkBox_0081, self.checkBox_0082, self.checkBox_0083, self.checkBox_0084,
                        self.checkBox_0085, self.checkBox_0086, self.checkBox_0087, self.checkBox_0088,
                        self.checkBox_0089, self.checkBox_0090, self.checkBox_0091, self.checkBox_0092,
                        self.checkBox_0093, self.checkBox_0094, self.checkBox_0095, self.checkBox_0096,
                        self.checkBox_0097, self.checkBox_0098, self.checkBox_0099, self.checkBox_0100,
                        self.checkBox_0101, self.checkBox_0102, self.checkBox_0103, self.checkBox_0104,
                        self.checkBox_0105, self.checkBox_0106, self.checkBox_0107, self.checkBox_0108,
                        self.checkBox_0109, self.checkBox_0110, self.checkBox_0111, self.checkBox_0112,
                        self.checkBox_0113, self.checkBox_0114, self.checkBox_0115, self.checkBox_0116,
                        self.checkBox_0117, self.checkBox_0118, self.checkBox_0119, self.checkBox_0120,
                        self.checkBox_0121, self.checkBox_0122, self.checkBox_0123, self.checkBox_0124,
                        self.checkBox_0125, self.checkBox_0126, self.checkBox_0127, self.checkBox_0128,
                        self.checkBox_0129, self.checkBox_0130, self.checkBox_0131, self.checkBox_0132,
                        self.checkBox_0133, self.checkBox_0134, self.checkBox_0135, self.checkBox_0136,
                        self.checkBox_0137, self.checkBox_0138, self.checkBox_0139, self.checkBox_0140,
                        self.checkBox_0141, self.checkBox_0142, self.checkBox_0143, self.checkBox_0144,
                        self.checkBox_0145, self.checkBox_0146, self.checkBox_0147, self.checkBox_0148,
                        self.checkBox_0149, self.checkBox_0150,]

        self.usa = ["M2A4 - (I)", "M2 - (I)", "LVT(A)(1) - (I)", "M13 MGMC - (I)", "*M2A4(ist Arm.Div.) - (I)",
                    "*M8 LAC", "M3 Stuart - (I)", "M3A1 Stuart - (I)", "M22 - (I)", "M8 HMC - (I)", "*LVT(A)(4) - (I)",
                    "*M8A1 GMC - (I)", "M3 GMC - (I)", "*M3A1 (USMC) - (I)",
                    "M5A1 - (II)", "M3 Lee - (II)", "M4A3(105) - (II)", "M15 CGMC - (II)", "M10 GMC - (II)",
                    "*Stuart 6(5th CAD) - (II)", "M24 - (II)", "M4A1 - (II)", "M16 MGMC - (II)", "*Grant 1 - (II)",
                    "M4 - (II)", "*M4A5 - (II)", "*T18E2 - (II)",
                    "M4A2 - (III)", "M6A1 - (III)", "M19A1 - (III)", "M18 GMC - (III)", "*T14 - (III)",
                    "*T55E1 - (III)", "M4A1(76) W - (III)", "M4A3E2 - (III)", "*M18 'Black Cat' - (III)",
                    "*Cobra King - (III)", "M4A2(76) W", "*Calliope - (III)", "*T20 - (III)",
                    "M41A1 - (IV)", "M4A3(76) W - (IV)", "M4A3E2(76) W - (IV)", "M42 - (IV)", "M36 GMC - (IV)",
                    "*Super Hellcat - (IV)", "*T28 - (IV)", "M56 - (IV)", "T25 - (IV)", "T26E5 - (IV)", "M36B2 - (IV)",
                    "*M26 T99 - (IV)", "*T29 - (IV)", "T92 - (IV)", "M26 - (IV)", "T26E1-1 - (IV)", "*M26E1 - (IV)",
                    "*T30 - (IV)", "T34 - (IV)", "*M26 'Tiger' - (IV)", "*M6A2E1 - (IV)",
                    "M50 - (V)", "M46 - (V)", "M47 - (V)", "T32 - (V)", "T32E1 - (V)", "M163 - (V)", "T95 - (V)",
                    "*T114", "*Magach 3 (ERA) - (V)", "M48 - (V)", "M60 - (V)", "M103 - (V)", "*T54E1 - (V)",
                    "M551 - (VI)", "M60A1 (AOS) - (VI)", "T95E1 - (VI)", "M247 - (VI)", "M60A2 - (VI)",
                    "*XM-1 (GM) - (VI)", "M3 Bradley - (VI)", "M60A1 RISE (P) - (VI)", "XM-803 - (VI)", "MBT-70 - (VI)",
                    "LAV-AD - (VI)", "*XM-1(Chrysler) - (VI)", "M3A3 Bradley - (VI)", "M60A3 TTS - (VI)",
                    "M1 Abrams - (VI)", "@M901 - (VI)", "M1A1 - (VI)",
                    "HSTV-L - (VII)", "IPM1 - (VII)", "XM975 - (VII)", "M1128 - (VII)", "@M1A1 AIM - (VII)",
                    "M1A1 HC - (VII)", "ADATS - (VII)", "M1A2 Abrams - (VII)"]
        self.ussr = ["БТ-5 - (I)", "Т-26 - (I)", "Т-60 - (I)", "СУ-5-1 - (I)", "ГАЗ-ААА(4М) - (I)", "*Т-26 - (I)",
                     "БТ-7 - (I)", "Т-26-4 - (I)", "Т-70 - (I)", "СУ-76М - (I)", "ГАЗ-ААА(ДШК) - (I)", "*Т-35 - (I)",
                     "БТ-7М - (I)", "Т-28(1938) - (I)", "*Т-3 - (I)", "*СУ-57 - (I)",
                     "Т-50 - (II)", "Т-28 - (II)", "Т-28Э - (II)", "Т-80 - (II)", "СУ-122 - (II)",
                     "ГАЗ-ММ(72-К) - (II)", "*Т-126 - (II)", "Т-34(1940) - (II)", "Т-34(1941) - (II)", "КВ-1(Л-11) - (II)",
                     "Зис-30 - (II)", "БТР-152А - (II)", "Т-34(1942) - (II)", "КВ-2(1939) - (II)", "СУ-57Б - (II)",
                     "Зис-12(95-км) - (II)", "Т-34Э СТЗ - (II)", "КВ-1С - (II)", "ЯГ-10(29-К) - (II)",
                     "*Т-34(1 Гв.Т.Бр.) - (II)", "*Т-34Э - (II)", "*Т-34(Прототип) - (II)",
                     "Т-34-57 - (III)", "КВ-1(ЗиС-5) - (III)", "АСУ-57 - (III)", "СУ-152 - (III)", "ИСУ-152 - (III)",
                     "ЗиС-43 - (III)", "*Т-34-57(1943) - (III)", "*КВ-2(1940) - (III)", "Т-34-85(Д-5Т) - (III)",
                     "КВ-85 - (III)", "ПТ-76Б - (III)", "СУ-85 - (III)", "СУ-85М - (III)", "ЗСУ-37 - (III)",
                     "*СУ-100Y - (III)", "*КВ-1Э - (III)", "ИС-1 - (III)", "ИСУ-122 - (III)", "*M4A2 - (III)",
                     "*Pho'ng kho'ng T-34 - (III)",
                     "Т-34-85 - (IV)", "ИС-2 - (IV)", "АСУ-85 - (IV)", "ИСУ-122С - (IV)", "БТР-3Д - (IV)",
                     "*Т-34-85Э - (IV)", "*КВ-122 - (IV)", "Т-44 - (IV)", "ИС-2(1944) - (IV)", "ИС-2 №321 - (IV)",
                     "СУ-100П - (IV)", "СУ-100 - (IV)", "*СУ-122П - (IV)", "*ИС-2 'Месть' - (IV)", "Т-44-100 - (IV)",
                     "2С3М - (IV)", "*Т-44-122 - (IV)", "*Объект 248 - (IV)", "*Т-34-100 - (IV)", "*ИС-6 - (IV)",
                     "*ПТ-76-57 - (IV)",
                     "Т-54(1949) - (V)", "ИС-3 - (V)", "БМП-1 - (V)", "СУ-122-54 - (V)", "ЗСУ-57-2 - (V)",
                     "*Объект 120 - (V)", "*Т10А - (V)", "Т-54(1947) - (V)", "Т-54(1951) - (V)", "ИС-4М - (V)",
                     "Объект 906 - (V)", "Объект 268 - (V)",
                     "Т-55А - (VI)", "Т-10М - (VI)", "БМП-2 - (VI)", "ИТ-1 - (VI)", "ЗСУ-37-2 - (VI)",
                     "*Т-55АМ-1 - (VI)", "Т-55АМД-1 - (VI)", "Т-64(1971) - (VI)", "БМП-3 - (VI)", "Штурм-С - (VI)",
                     "ЗСУ-23-4 - (VI)", "*T-72AB(TURMS-T) - (VI)", "Т-62 - (VI)", "Т-62-1 - (VI)", "Т-64Б - (VI)",
                     "Объект 685 - (VI)", "@БМП-2М - (VI)", "Т-72А - (VI)", "Т-80Б - (VII)", "Т-72Б - (VII)",
                     "Т-90А - (VII)", "Т-80У - (VII)", "2С25 - (VII)", "Хризантема-С - (VII)", "2С6 - (VII)",
                     "@Т-80УК - (VII)", "Т-72Б3 - (VII)", "Т-80БВМ - (VII)", "2С25М - (VII)"]
        self.germ = ["sd.Kfz.221 - (I)", "Pz.III E - (I)", "pz.III B - (I)", "Pz.II C - (I)", "Pz.II F - (I)",
                     "Flakpanzer 1 - (I)", "Pz.35(t) - (I)", "*Sd.Kfz.251/10 - (I)", "15cm sIG 33 B Sfi - (I)",
                     "Pz.III F - (I)", "Pz.III J - (I)", "Pz.IV C - (I)", "Flakpanzer 38 - (I)", "Pz.38(t) A - (I)",
                     "Pz.38(t) F - (I)", "*Pz.II C (DAK) - (I)", "*Sd.Kfz.234/1 - (I)", "PanzerJager I - (I)",
                     "Pz.4 E - (I)", "StuG III A - (I)", "*Sd.Kfz. 140/1 - (I)", "*Sd.Kfz.234/3 - (I)", "*Nb.Fz. - (I)",
                     "Sd.Kfz.234/2 - (II)", "Pz.III J1 - (II)", "Pz.IV F1 - (II)", "Sd.Kfz. 6/2 - (II)", "StuH 42 G - (II)",
                     "Marder III - (II)", "Marder III H - (II)", "Pz.III L - (II)", "Pz.III M - (II)",
                     "Pz.IV F2 - (II)", "Pz.IV G - (II)", "Sd.Kfz.251/21 - (II)", "StuG III F - (II)",
                     "*Pz.III N - (II)", "*Pz.Sfl.Ic - (II)", "Dicker Max - (II)", "Pz.IV H - (II)", "Pz.IV J - (II)",
                     "StuG III G - (II)", "*15 cm Pz.W.42 - (II)", "*Sd.Kfz.251/22 - (II)", "*T 34 747 (r) - (II)",
                     "8,8 cm Flak 37 Sfl - (III)", "Tiger H1 - (III)", "VK 3002 (M) - (III)", "Wirdelwind - (III)",
                     "Jagpanzer 38(t) - (III)", "*KW II 754 (r) - (III)", "*Sd.Kfz.234/4 - (III)",
                     "Sturer Emil - (III)", "Tiger E - (III)", "Panther D - (III)", "Ostwind - (III)",
                     "Jagpanzer IV - (III)", "*Pz.Bef.Wg.IV J - (III)", "*M4 748(a) - (III)", "Nashorn - (III)",
                     "PanzerIV/70(5) - (III)", "*Pz.Kpfw. Churchill - (III)", "*KV-IB - (III)", "*Brummbar - (III)",
                     "*VFW - (III)", "*Panzer IV/70(A) - (III)", "*Ersatz M10 - (III)", "*KW I C 756 (r) - (III)",
                     "*Tiger - (III)", "VK 45.01 (P) - (III)",
                     "Waffentrager - (IV)", "Tiger II(P) - (IV)", "Panther A - (IV)", "Ostwind II - (IV)",
                     "Jagpanther - (IV)", "*Pz.Bef.Wg.VI P - (IV)", "*Tiher II(H) Sla.16 - (IV)", "leKPz M41 - (IV)",
                     "Tiger II(H) - (IV)", "Panther G - (IV)", "JPz 4-5 - (IV)", "*Bfw.Jaqdpanther - (IV)",
                     "*Ru 251 - (IV)", "Ferdinand - (IV)", "*Elefant - (IV)",
                     "Marder A1 - (V)", "M48A2 C - (V)", "Leopard I - (V)", "Kugelblitz - (V)", "Jagdtiger - (V)",
                     "*mKPz M47 G", "SPz BMP-1 - (V)", "Wiesel 1A4 - (V)", "DF105 - (V)", "*Turm II - (V)",
                     "Marder 1A3 - (V)", "RakJPz 2 - (V)", "*Maus - (V)",
                     "TAM - (VI)", "M48A2 G A2 - (VI)", "Leopard A1A1 - (VI)", "Leopard A1A5 - (VI)", "Gepard - (VI)",
                     "RakJPz 2(HOT) - (VI)", "*TAN 2IP - (VI)", "PUMA - (VI)", "M48 Super - (VI)", "Leopadr 2K - (VI)",
                     "Ozelot - (VI)", "JaPz.K A2 - (VI)", "*Leopard A1A1 (L/44) - (VI)", "Begleitpanzer 57 - (VI)",
                     "KPz-70 - (VI)", "Leopard 2A4 - (VI)", "Wiesel 1A2 - (VI)", "*Leopard 2 (PzBtl 123) - (VI)",
                     "Radkampfwagen 90 - (VI)", "TAM 2C - (VII)", "Leopard 2A5 - (VII)", "FlaRakPz 1 - (VII)",
                     "@Leopard 2 PL - (VII)", "Leopard 2A6 - (VII)", "FlaRakRad - (VII)"]
        self.brit = ["A13 Mk.I - (I)", "Stuart I - (I)", "Tetrarch I - (I)", "Light AA Mk I - (I)",
                     "*A13 MkI(3rd R.T.R) - (I)", "*Alecto I - (I)", "A13 Mk.II - (I)", "Stuart III - (I)",
                     "Diamler Mk II - (I)", "Staghound AA - (I)", "*Independent - (I)", "*A13 MKk.II 1939 - (I)",
                     "Crusader II - (II)", "Crusader III - (II)", "Valentine I - (II)", "Valentine XI - (II)",
                     "Valentine IX - (II)", "Archer - (II)", "AEC AA - (II)", "SARC MkVI (2pdr) - (II)",
                     "*Crusader 'TheSaint' - (II)", "*A.C.I - (II)", "Cromwell V - (II)", "Cromwell I - (II)",
                     "Matilda III - (II)", "Gun Carrier (3-in) - (II)", "Crusader AAMk.I - (II)",
                     "SARG.MkVI (6pdr) - (II)", "*Cromwell V(RP-3) - (II)", "*Matilda Hedgehog - (II)",
                     "Sherman II - (II)", "Churchill I - (II)", "Achilles - (II)", "*Grant I - (II)", "*AECMk II - (II)",
                     "Sherman Firefly - (III)", "Churchill III - (III)", "Avenger - (III)", "Crusader AA Mk.II - (III)",
                     "Concept - (III)", "*Achilles (65 Rg.) - (III)", "*Excelsior - (III)", "Chalenger - (III)",
                     "Churchill VII - (III)", "Ystervark - (III)", "*Sherman IC 'Tzyniek' - (III)",
                     "*Comet I 'Iron Duke IV' - (III)", "Comet I - (III)", "*A.C.IV - (III)", "*QF 3.7 Ram - (III)",
                     "Centurion Mk.1 - (IV)", "Charioteer Mk.VII - (IV)", "Tortoise - (IV)", "Skink - (IV)",
                     "Ratel 90 - (IV)", "*Black Prince - (IV)", "Centurion Mk.3 - (IV)", "FV4202 - (IV)",
                     "FV4005 - (IV)", "G6 - (IV)", "*Str 81 (RB 52) - (IV)", "Caernarvon - (IV)", "Conway - (IV)",
                     "Eland 90 Mk.7 - (IV)", "*Centurion Action X - (IV)",
                     "Centurion Mk.10 - (V)", "Vickers Mk.1 - (V)", "Swingfire - (V)", "Falcon - (V)", "Ratel 20 - (V)",
                     "*Centurion Mk.5 AVRE - (V)", "*Centurion Mk.5/1 - (V)", "Conqueror - (V)", "Vickers Mk.3 - (V)",
                     "Striker - (V)", "Chieftain Mk.3 - (VI)", "Chieftain Mk.5 - (VI)", "VFM5 - (VI)", "Warrior - (VI)",
                     "Chieftain Marksman - (VI)", "Roikat Mk.1D - (VI)", "*Sho't Kal Dalet - (VI)",
                     "Rooikat 105 - (VI)", "Chieftain Mk.10 - (VI)", "Vickers Mk.7 - (VI)", "ZT3A2 - (VI)",
                     "ZA-35 - (VI)", "Olifant Mk.1A - (VI)", "*Challenger DS - (VI)", "Challenger Mk.2 - (VI)",
                     "Rooikat MTTD - (VI)", "Challenger Mk.3 - (VI)", "Olifant Mk.2 - (VI)",
                     "Challenger 2 - (VII)", "Stormer HVM - (VII)", "TTD - (VII)", "Challenger 2 (2F) - (VII)",
                     "ADATS (M113) - (VII)", "Challenger 2 TES - (VII)", "Black Night - (VII)"]
        self.jap = ["Ha-Go - (I)", "STB-1 - (V)", "Type10 - (VII)"]
        self.chin = ["*T-26 - (I)", "*IS-2 - (IV)", "ZTZ99A - (VII)"]
        self.ital = ["AB41 - (I)", "C13 T90 - (V)", "Ariete - (VII)"]
        self.franc = ["FCM.36 - (I)", "Leclerc - (VII)"]
        self.swhib = ["Strv m/31 - (I)", "CV 90120 - (VII)"]
        self.lvl = ["I", "II", "III", "IV", "V", "VI", "VII"]

        # вспомогательный цикл
        for i in self.p1_btns:
            i.setEnabled(False)
            i.setVisible(False)
        self.p1_rbtn_all.setEnabled(False)
        self.p1_rbtn_all.setVisible(False)

    def initUI(self):
        self.p1_nations.activated.connect(self.update_tech)                         # переключение наций
        self.p1_btn_tech.toggled.connect(self.update_tech)                          # преключение лвл/тех.
        self.p1_btn_lvl.toggled.connect(self.update_tech)                           # преключение лвл/тех.
        self.p1_play.stateChanged.connect(lambda state: self.enable_p1(state))      # пер. p1(on/off)
        self.p1_rbtn_all.toggled.connect(lambda state: self.enable_all(state))      # вкл все checkBox
        self.btn_random.clicked.connect(self.update_random)                         # случайная техника

    # _______вкл/выкл игрока1________
    def enable_p1(self, state):
        self.label_p1.setEnabled(state)
        self.p1_nickname.setEnabled(state)
        self.p1_btn_lvl.setEnabled(state)
        self.p1_btn_tech.setEnabled(state)
        self.p1_label_n.setEnabled(state)
        self.p1_nations.setEnabled(state)
        self.p1_label_numb.setEnabled(state)
        self.p1_numb.setEnabled(state)
        self.p1_area.setEnabled(state)
        self.p1_output.setEnabled(state)

    # _______выбор всех checkBox_____
    def enable_all(self, state):
        if self.p1_btn_lvl.isChecked():
            for i in self.p1_btns:
                i.setChecked(state)
        if self.p1_nations.currentText() == "США":
            for i in self.p1_btns:
                if self.p1_btns.index(i) == len(self.usa):
                    break
                i.setChecked(state)
        elif self.p1_nations.currentText() == "СССР":
            for i in self.p1_btns:
                if self.p1_btns.index(i) == len(self.ussr):
                    break
                i.setChecked(state)
        elif self.p1_nations.currentText() == "Германия":
            for i in self.p1_btns:
                if self.p1_btns.index(i) == len(self.germ):
                    break
                i.setChecked(state)

        elif self.p1_nations.currentText() == "Великобритания":
            for i in self.p1_btns:
                if self.p1_btns.index(i) == len(self.brit):
                    break
                i.setChecked(state)

        elif self.p1_nations.currentText() == "Япония":
            for i in self.p1_btns:
                if self.p1_btns.index(i) == len(self.jap):
                    break
                i.setChecked(state)

        elif self.p1_nations.currentText() == "Китай":
            for i in self.p1_btns:
                if self.p1_btns.index(i) == len(self.chin):
                    break
                i.setChecked(state)

        elif self.p1_nations.currentText() == "Италия":
            for i in self.p1_btns:
                if self.p1_btns.index(i) == len(self.ital):
                    break
                i.setChecked(state)

        elif self.p1_nations.currentText() == "Франция":
            for i in self.p1_btns:
                if self.p1_btns.index(i) == len(self.franc):
                    break
                i.setChecked(state)

        elif self.p1_nations.currentText() == "Швеция":
            for i in self.p1_btns:
                if self.p1_btns.index(i) == len(self.swhib):
                    break
                i.setChecked(state)

    # _______обновить список кнопок__
    def update_tech(self):
        for i in self.p1_btns:
            i.setChecked(False)
            i.setEnabled(False)
            i.setVisible(False)
        self.p1_rbtn_all.setChecked(False)
        if self.p1_nations.currentText() == "Не выбрано":
            self.label_nat.setText("Нация")
            for i in self.p1_btns:
                i.setChecked(False)
                i.setEnabled(False)
                i.setVisible(False)
            self.p1_rbtn_all.setEnabled(False)
            self.p1_rbtn_all.setVisible(False)

        if self.p1_btn_tech.isChecked():

            if self.p1_nations.currentText() == "США":
                # pixmap = QPixmap('usa2_flag.png')
                self.label_nat.setPixmap(QPixmap("flags/usa_flag.png"))
                for i in self.p1_btns:
                    if self.p1_btns.index(i) == len(self.usa):
                        break
                    i.setEnabled(True)
                    i.setVisible(True)
                self.p1_rbtn_all.setEnabled(True)
                self.p1_rbtn_all.setVisible(True)
                for k, i in enumerate(self.p1_btns):
                    if self.p1_btns.index(i) == len(self.usa):
                        break
                    i.setText(self.usa[k])

            elif self.p1_nations.currentText() == "СССР":
                # pixmap = QPixmap('ussr2_flag.png')
                self.label_nat.setPixmap(QPixmap("flags/ussr_flag.png"))
                for i in self.p1_btns:
                    if self.p1_btns.index(i) == len(self.ussr):
                        break
                    i.setEnabled(True)
                    i.setVisible(True)
                self.p1_rbtn_all.setEnabled(True)
                self.p1_rbtn_all.setVisible(True)
                for k, i in enumerate(self.p1_btns):
                    if self.p1_btns.index(i) == len(self.ussr):
                        break
                    i.setText(self.ussr[k])

            elif self.p1_nations.currentText() == "Германия":
                self.label_nat.setPixmap(QPixmap("flags/germ_flag.png"))
                for i in self.p1_btns:
                    if self.p1_btns.index(i) == len(self.germ):
                        break
                    i.setEnabled(True)
                    i.setVisible(True)
                self.p1_rbtn_all.setEnabled(True)
                self.p1_rbtn_all.setVisible(True)
                for k, i in enumerate(self.p1_btns):
                    if self.p1_btns.index(i) == len(self.germ):
                        break
                    i.setText(self.germ[k])

            elif self.p1_nations.currentText() == "Великобритания":
                self.label_nat.setPixmap(QPixmap("flags/britn_flag.png"))
                for i in self.p1_btns:
                    if self.p1_btns.index(i) == len(self.brit):
                        break
                    i.setEnabled(True)
                    i.setVisible(True)
                self.p1_rbtn_all.setEnabled(True)
                self.p1_rbtn_all.setVisible(True)
                for k, i in enumerate(self.p1_btns):
                    if self.p1_btns.index(i) == len(self.brit):
                        break
                    i.setText(self.brit[k])

            elif self.p1_nations.currentText() == "Япония":
                self.label_nat.setPixmap(QPixmap("flags/jap_flag.png"))
                for i in self.p1_btns:
                    if self.p1_btns.index(i) == len(self.jap):
                        break
                    i.setEnabled(True)
                    i.setVisible(True)
                self.p1_rbtn_all.setEnabled(True)
                self.p1_rbtn_all.setVisible(True)
                for k, i in enumerate(self.p1_btns):
                    if self.p1_btns.index(i) == len(self.jap):
                        break
                    i.setText(self.jap[k])

            elif self.p1_nations.currentText() == "Китай":
                self.label_nat.setPixmap(QPixmap("flags/chine_flag.png"))
                for i in self.p1_btns:
                    if self.p1_btns.index(i) == len(self.chin):
                        break
                    i.setEnabled(True)
                    i.setVisible(True)
                self.p1_rbtn_all.setEnabled(True)
                self.p1_rbtn_all.setVisible(True)
                for k, i in enumerate(self.p1_btns):
                    if self.p1_btns.index(i) == len(self.chin):
                        break
                    i.setText(self.chin[k])

            elif self.p1_nations.currentText() == "Италия":
                self.label_nat.setPixmap(QPixmap("flags/ital_flag.png"))
                for i in self.p1_btns:
                    if self.p1_btns.index(i) == len(self.ital):
                        break
                    i.setEnabled(True)
                    i.setVisible(True)
                self.p1_rbtn_all.setEnabled(True)
                self.p1_rbtn_all.setVisible(True)
                for k, i in enumerate(self.p1_btns):
                    if self.p1_btns.index(i) == len(self.ital):
                        break
                    i.setText(self.ital[k])
            elif self.p1_nations.currentText() == "Франция":
                self.label_nat.setPixmap(QPixmap("flags/franc_flag.png"))
                for i in self.p1_btns:
                    if self.p1_btns.index(i) == len(self.franc):
                        break
                    i.setEnabled(True)
                    i.setVisible(True)
                self.p1_rbtn_all.setEnabled(True)
                self.p1_rbtn_all.setVisible(True)
                for k, i in enumerate(self.p1_btns):
                    if self.p1_btns.index(i) == len(self.franc):
                        break
                    i.setText(self.franc[k])

            elif self.p1_nations.currentText() == "Швеция":
                self.label_nat.setPixmap(QPixmap("flags/swib_flag.png"))
                for i in self.p1_btns:
                    if self.p1_btns.index(i) == len(self.swhib):
                        break
                    i.setEnabled(True)
                    i.setVisible(True)
                self.p1_rbtn_all.setEnabled(True)
                self.p1_rbtn_all.setVisible(True)
                for k, i in enumerate(self.p1_btns):
                    if self.p1_btns.index(i) == len(self.swhib):
                        break
                    i.setText(self.swhib[k])

        if self.p1_btn_lvl.isChecked():
            for i in self.p1_btns:
                if self.p1_btns.index(i) == len(self.lvl):
                    break
                i.setEnabled(True)
                i.setVisible(True)
            self.p1_rbtn_all.setEnabled(True)
            self.p1_rbtn_all.setVisible(True)
            for k, i in enumerate(self.p1_btns):
                if self.p1_btns.index(i) == len(self.lvl):
                    break
                i.setText(self.lvl[k])

    # ___вывод случаной техники______
    def update_random(self):
        # ________p1__________________________
        if self.p1_play.isChecked():
            self.p1_out = []
            self.k = int(self.p1_numb.text())
            if self.p1_btn_tech.isChecked():
                for i in self.p1_btns:
                    if i.isChecked():
                        if "B_" not in i.text():
                            self.p1_out.append(str(i.text()))
                self.update_out(self.p1_out, self.p1_output, self.k)

            elif self.p1_btn_lvl.isChecked():
                for i in self.p1_btns:
                    if i.isChecked():
                        if self.p1_nations.currentText() == "США":
                            for b in self.usa:
                                if "(" + i.text() + ")" in b and b not in self.p1_out:
                                    self.p1_out.append(str(b))
                        if self.p1_nations.currentText() == "СССР":
                            for b in self.ussr:
                                if "(" + i.text() + ")" in b and b not in self.p1_out:
                                    self.p1_out.append(str(b))
                        if self.p1_nations.currentText() == "Германия":
                            for b in self.germ:
                                if "(" + i.text() + ")" in b and b not in self.p1_out:
                                    self.p1_out.append(str(b))
                        if self.p1_nations.currentText() == "Великобритания":
                            for b in self.brit:
                                if "(" + i.text() + ")" in b and b not in self.p1_out:
                                    self.p1_out.append(str(b))
                        if self.p1_nations.currentText() == "Япония":
                            for b in self.jap:
                                if "(" + i.text() + ")" in b and b not in self.p1_out:
                                    self.p1_out.append(str(b))
                        if self.p1_nations.currentText() == "Китай":
                            for b in self.chin:
                                if "(" + i.text() + ")" in b and b not in self.p1_out:
                                    self.p1_out.append(str(b))
                        if self.p1_nations.currentText() == "Италия":
                            for b in self.ital:
                                if "(" + i.text() + ")" in b and b not in self.p1_out:
                                    self.p1_out.append(str(b))
                        if self.p1_nations.currentText() == "Франция":
                            for b in self.franc:
                                if "(" + i.text() + ")" in b and b not in self.p1_out:
                                    self.p1_out.append(str(b))
                        if self.p1_nations.currentText() == "Швеция":
                            for b in self.swhib:
                                if "(" + i.text() + ")" in b and b not in self.p1_out:
                                    self.p1_out.append(str(b))
                self.update_out(self.p1_out, self.p1_output, self.k)

    # ___вывод на экран информации___
    def update_out(self, sp, where, k):
        t = "ЛВЛ'А" if not self.p1_btn_tech.isChecked() else "Техника"
        a = sample(sp, k=k)
        b = f"Ник - {str(self.p1_nickname.text())}\nНация - {str(self.p1_nations.currentText())}\n" \
            f"Тип подбора - {t}\n\n"
        for k, i in enumerate(a, start=1):
            b += f"{k}) {i}\n"
        where.setText(b)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())