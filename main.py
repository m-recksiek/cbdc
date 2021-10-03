from PyQt6 import QtCore, QtGui, QtWidgets, Qt
import numpy as np
import sys
import random
import time
import math
import importlib
import json

#Calculator
import calculator
calculator = calculator.Calculator
#GlobalLists
import lists
settingsList = lists.settingsList
monsterList = lists.monsterList
weaponList = lists.weaponList
sharpnessList = lists.sharpnessList
elementList = lists.elementList

bg_color = QtGui.QColor(191, 191, 191)

class AllSettings(object):

    def initalize(self):
        self.settings = {
            "Weapon": "Charge Blade",
            "Raw": 198,
            "Attackboost": 7,
            "Challenger": 0,
            "Resuscitate": 0,
            "Resentment": 0,
            "Peak Performance": 0,
            "Offensive Guard": 0,
            "Fortify": 0,
            "Counterstrike": 0,
            "Heroics": 0,
            "Element": 0,
            "Elementtype": 0,
            "Elementlevel": 5,
            "Sharpness": "White",
            "Critical Boost": 3,
            "Artillery": 0,
            "Bludgeoner": 0,
            "Mind's Eye": 0,
            "Rapid Morph": 2,
            "Rampage Skill": 0,
            "useinputraw": False,
            "displayBaseHZOnly": False,
            "displayRawTable": False
        }

    def load_settings(self):
        import_settings = json.load(open("global_settings.json", 'r'))
        print(import_settings)
        for key, value in import_settings.items():
            self.settings[key] = value



my_settings = AllSettings()
my_settings.initalize()
my_settings.load_settings()
calculator. calculateRaw(calculator, my_settings.settings)

# print(dir())


class UI_SettingsWindow(object):

    def openSettingsWindow(self):
        print(my_settings.settings)
        self.window = QtWidgets.QMainWindow()
        settings_window.setupUI(self.window)
        self.window.show()

    def setupUI(self, s_window: object) -> object:
        self.widget_list = []
        # temp_settings = my_settings.settings
        s_window.setObjectName("s_window")
        s_window.resize(450, 400)
        self.centralwidget = QtWidgets.QWidget(s_window)
        self.centralwidget.setObjectName("centralwidget")
        s_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(s_window)
        self.statusbar.setObjectName("statusbar")
        s_window.setStatusBar(self.statusbar)
        self.retranslateUi(s_window)
        QtCore.QMetaObject.connectSlotsByName(s_window)

        self.applyBut = QtWidgets.QPushButton(self.centralwidget)
        self.applyBut.setGeometry(QtCore.QRect(10, 350, 120, 30))
        self.applyBut.clicked.connect(self.apply_settings)
        self.applyBut.setText("Apply")
        self.applyBut.setObjectName("apply")

        self.saveBut = QtWidgets.QPushButton(self.centralwidget)
        self.saveBut.setGeometry(QtCore.QRect(140, 350, 120, 30))
        self.saveBut.clicked.connect(self.save_settings)
        self.saveBut.setText("Save & Apply")
        self.saveBut.setObjectName("save")

        xcoord = 10
        ycoord = 45

        for key, value in my_settings.settings.items():

            if key == "Element":
                xcoord += 225
                ycoord = 65
            if key == "useinputraw":
                xcoord = 10
                ycoord = 300

            if not key == "Weapon":
                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(xcoord, ycoord, 100, 15))
                self.label.setObjectName("label")
                self.label.setText(str(key))

            if settingsList[key] == "I":
                self.input = QtWidgets.QLineEdit(self.centralwidget)
                self.input.setGeometry(QtCore.QRect(xcoord + 100, ycoord, 80, 15))
                self.input.setObjectName(key)
                self.input.setText(str(value))
                self.widget_list.append(self.input)
            elif settingsList[key] == "B":
                self.box = QtWidgets.QCheckBox(self.centralwidget)
                self.box.setGeometry(QtCore.QRect(xcoord + 190, ycoord, 15, 15))
                self.box.setObjectName(key)
                self.box.setChecked(bool(value))
                self.widget_list.append(self.box)
                #self.box.isChecked(value)
            elif settingsList[key] == "C":
                self.box = QtWidgets.QComboBox(self.centralwidget)
                self.box.setGeometry(QtCore.QRect(xcoord + 100, ycoord, 80, 15))
                self.box.setObjectName(key)
                self.widget_list.append(self.box)
                if key == "Weapon":
                    self.label = QtWidgets.QLabel(self.centralwidget)
                    self.label.setGeometry(QtCore.QRect(125, 10, 161, 20))
                    self.label.setObjectName("label")
                    self.label.setText(key)
                    for i in range(len(weaponList)):
                        self.box.addItem(weaponList[i])
                    self.box.setCurrentText(value)
                    self.box.setGeometry(QtCore.QRect(173, 10, 161, 20))
                elif key == "Sharpness":
                    for i in range(len(sharpnessList)):
                        sharpness = sharpnessList[i]
                        self.box.addItem(sharpness[0])
                    self.box.setCurrentText(str(value))
                elif key == "Elementtype":
                    for i in range(len(elementList)):
                        self.box.addItem(elementList[i])
                    self.box.setCurrentText(str(value))
                elif key == "Rampageeffect":
                    pass
                elif key == "Silbind":
                    pass
                else:
                    pass
            elif settingsList[key] > 0:
                self.box = QtWidgets.QComboBox(self.centralwidget)
                self.box.setGeometry(QtCore.QRect(xcoord + 120, ycoord, 60, 15))
                self.box.setObjectName(key)
                self.widget_list.append(self.box)
                i = 0
                while i < int(settingsList[key]) + 1:
                    self.box.addItem(str(i))
                    i += 1
                self.box.setCurrentText(str(value))

            ycoord += 20

    def closewindow(self):
        self.window.close()

    def apply_settings(self):

        for item in self.widget_list:
            print(item.objectName())
            if isinstance(item, QtWidgets.QLineEdit):
                my_settings.settings[item.objectName()] = item.text()
                print(my_settings.settings[item.objectName()])
            if isinstance(item, QtWidgets.QComboBox):
                my_settings.settings[item.objectName()] = item.currentText()
                print(my_settings.settings[item.objectName()])
            if isinstance(item, QtWidgets.QCheckBox):
                my_settings.settings[item.objectName()] = item.isChecked()
                print(my_settings.settings[item.objectName()])
        self.closewindow()

    def save_settings(self):
        for item in self.widget_list:
            print(item.objectName())
            if isinstance(item, QtWidgets.QLineEdit):
                my_settings.settings[item.objectName()] = item.text()
            if isinstance(item, QtWidgets.QComboBox):
                my_settings.settings[item.objectName()] = item.currentText()
            if isinstance(item, QtWidgets.QCheckBox):
                my_settings.settings[item.objectName()] = item.isChecked()
        with open('global_settings.json', 'w') as outfile:
            json.dump(my_settings.settings, outfile)
        self.closewindow()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

settings_window = UI_SettingsWindow()

class Ui_MainWindow(object):

    def resizeEvent(self, event):
        print("Window has been resized")
        QtWidgets.QMainWindow.resizeEvent(self.centralwidget, event)

    def setupUi(self, MainWindow):
        self.list_of_scrollbars = []
        self.list_of_damagetables = []
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(940, 600)
        # window_width = MainWindow.frameGeometry().width()  -- for later
        # window_height = MainWindow.frameGeometry().height()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # Combobox Monster
        self.cb_monster = QtWidgets.QComboBox(self.centralwidget)
        self.cb_monster.setGeometry(QtCore.QRect(10, 10, 181, 21))
        self.cb_monster.setObjectName("cb_monster")
        for i in range(len(monsterList)):
            self.cb_monster.addItem(monsterList[i])
        # Combobox Weapon
        self.cb_weapons = QtWidgets.QComboBox(self.centralwidget)
        self.cb_weapons.setGeometry(QtCore.QRect(200, 10, 161, 21))
        self.cb_weapons.setObjectName("cb_weapons")
        for i in range(len(weaponList)):
            self.cb_weapons.addItem(weaponList[i])
        # calcButton
        self.calcButton = QtWidgets.QPushButton(self.centralwidget)
        self.calcButton.setGeometry(QtCore.QRect(700, 10, 71, 31))
        self.calcButton.clicked.connect(self.pressCalc)
        self.calcButton.setObjectName("calcButton")
        # opensettingsbutton
        self.optsButton = QtWidgets.QPushButton(self.centralwidget)
        self.optsButton.setGeometry(QtCore.QRect(590, 10, 101, 31))
        self.optsButton.setObjectName("optsButton")
        self.optsButton.clicked.connect(settings_window.openSettingsWindow)
        MainWindow.setCentralWidget(self.centralwidget)
        # redundant for now
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.show_tables = False

    def pressCalc(self):
        self.efr = calculator.calculateRaw(calculator, my_settings.settings)
        self.fillDamageTables()
        pass

    def fillMoveNames(self):
        # Import MVs & Names
        w_mv = 'motion_values'
        wep_module = importlib.import_module(w_mv)
        weapon = wep_module.ChargeBlade
        # Create left table
        self.mn_table = QtWidgets.QTableWidget(self.centralwidget)
        self.mn_table.setGeometry(QtCore.QRect(10, 100, 292, 476))
        table_font = QtGui.QFont()
        table_font.setBold(True)
        self.mn_table.setFont(table_font)
        self.mn_table.setRowCount(len(weapon.mn))
        self.mn_table.setColumnCount(2)
        self.mn_table.setObjectName("mn_table")
        self.mn_table.verticalHeader().setVisible(False)

        #primary scrollbar

        self.list_of_scrollbars.append(self.mn_table.verticalScrollBar())
        self.mn_table.setHorizontalHeaderLabels([str("Move"), str("MV")])
        self.mn_table.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.mn_table.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)

        bg_color = QtGui.QColor(191, 191, 191)
        bgc_switch = True

        for i in range(len(weapon.mn)):
            if bgc_switch == True:
                self.mn_table.setItem(i, 0, QtWidgets.QTableWidgetItem(weapon.mn[i]))
                #self.mn_table.item(i, 0)
                self.mn_table.setItem(i, 1, QtWidgets.QTableWidgetItem(str(weapon.mv[i])))
                #self.mn_table.item(i, 1)
                bgc_switch = False
            else:
                self.mn_table.setItem(i, 0, QtWidgets.QTableWidgetItem(weapon.mn[i]))
                self.mn_table.item(i, 0).setBackground(bg_color)
                self.mn_table.setItem(i, 1, QtWidgets.QTableWidgetItem(str(weapon.mv[i])))
                self.mn_table.item(i, 1).setBackground(bg_color)
                bgc_switch = True


    def moveAllScrollbars(self, idx, bar):
        for bar in self.list_of_scrollbars:
            bar.setValue(idx)

    def fillDamageTables(self):
        self.fillMoveNames()
        # import monster hzs

        if self.show_tables == True:
            self.show_tables = False

            for tbl in self.list_of_damagetables:
                tbl.deleteLater()
            for i in range(len(self.list_of_scrollbars) -1):
                self.list_of_scrollbars.pop()
            self.frame.deleteLater()
            self.scrollarea.deleteLater()
            self.list_of_damagetables = []

        elif self.show_tables == False:
            self.show_tables = True

            #import tables
            w_mv = 'motion_values'
            wep_module = importlib.import_module(w_mv)
            weapon = wep_module.ChargeBlade
            m_hzv = "monsters"
            mon_module = importlib.import_module(m_hzv)
            monster = mon_module.Anjanath

            self.scrollarea = QtWidgets.QScrollArea(MainWindow)
            self.scrollarea.setVerticalScrollBarPolicy(
                QtWidgets.QScrollArea().verticalScrollBarPolicy().ScrollBarAsNeeded)
            self.scrollarea.setGeometry(329, 100, 600, 495)
            self.scrollarea.setObjectName("scrollarea")
            self.scrollarea.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
            self.scrollarea.show()

            #create frame - why?
            self.frame = QtWidgets.QFrame(self.scrollarea)
            self.frame.setGeometry(QtCore.QRect(0, 0, 900, 476))
            self.frame.setObjectName("frame")
            self.frame.show()
            self.scrollarea.setWidget(self.frame)
            #self.scrollarea.setWidget(self.frame)
            #self.layout.show()
            xs = 0
            ls = 0
            self.scrollarea_length = 0
            self.tablewidg = ""
            last_hzv = ""
            counter = 0
            # Create the MonsterHZVxDamageTables
            for i in range(len(monster.hzv)):
                #save current hzv for table breaks
                hzv_list = monster.hzv[i]
                hz = hzv_list[0]
                print(str(last_hzv), str(hz))


                #compare for table breaks
                if not str(last_hzv) == str(hz):
                    #new hz-table
                    xs += (counter * 80) + 5
                    table_width = 80
                    counter = 1
                    self.tablewidg = QtWidgets.QTableWidget(self.frame)
                    self.tablewidg.setGeometry(QtCore.QRect(xs, 0, table_width, 476))
                    self.tablewidg.setRowCount(len(weapon.mn))
                    self.tablewidg.setColumnCount(2 * counter)
                    self.tablewidg.verticalHeader().setVisible(False)
                    self.tablewidg.setHorizontalHeaderLabels([str("Base"), str("Crit")])

                    self.tablewidg.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
                    self.tablewidg.horizontalHeader().setSectionResizeMode(0,
                                                                           QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                    self.tablewidg.horizontalHeader().setSectionResizeMode(1,
                                                                           QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                    self.tablewidg.show()

                    self.list_of_scrollbars.append(self.tablewidg.verticalScrollBar())
                    self.list_of_damagetables.append(self.tablewidg)
                    self.scrollarea_length += 85
                else:
                    #modify current table
                    counter += 1
                    table_width = 80 * counter
                    self.tablewidg.setGeometry(QtCore.QRect(xs, 0, table_width, 476))
                    self.tablewidg.setColumnCount(2 * counter)
                    self.scrollarea_length += 80

                last_hzv = hz
                ls += 120
                # (self.tablewidg)


                #fill table with calculated value
                bgc_switch = True
                for j in range(len(weapon.mn)):

                    value = hzv_list[2]
                    damagev = int(value * weapon.mv[j])
                    critv = int((damagev * 1.4))

                    self.tablewidg.setItem(j, 0 + (2 * (counter - 1)), QtWidgets.QTableWidgetItem(str(damagev)))
                    self.tablewidg.setItem(j, 1 + (2 * (counter - 1)), QtWidgets.QTableWidgetItem(str(critv)))
                    self.tablewidg.horizontalHeader().setSectionResizeMode(0 + (2 * (counter - 1)),
                                                                           QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                    self.tablewidg.horizontalHeader().setSectionResizeMode(1 + (2 * (counter - 1)),
                                                                           QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                    self.tablewidg.show()

                    if bgc_switch == True:
                        bgc_switch = False
                    else:
                        bgc_switch = True
                        self.tablewidg.item(j, 1 + (2 * (counter - 1))).setBackground(bg_color)
                        self.tablewidg.item(j, 0 + (2 * (counter - 1))).setBackground(bg_color)



            for scrollbar in self.list_of_scrollbars:
                scrollbar.valueChanged.connect(lambda idx, bar=scrollbar: self.moveAllScrollbars(idx, bar))

            #self.scrollarea.setGeometry()
            print(self.scrollarea_length)

            self.frame.setGeometry(325, 100, self.scrollarea_length, 495)
            #self.scrollarea.setGeometry(325, 100, MainWindow.frameGeometry().width() - 15, 495)
            self.scrollarea.setGeometry(325, 100, 600, 495)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Charge Blade Damage Calculator"))
        self.calcButton.setText(_translate("MainWindow", "Calculate!"))
        self.optsButton.setText(_translate("MainWindow", "options"))



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.fillMoveNames()
    # attrs = vars(ui)
    # print(', '.join("%s: %s" % item for item in attrs.items()))

    MainWindow.show()
    sys.exit(app.exec())
