import sys
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTableWidgetItem, QMainWindow, QFileDialog, QButtonGroup, QDialog
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5 import QtCore, QtWidgets


class Ui_Function_approximation(object):
    def setupUi(self, Function_approximation):
        Function_approximation.setObjectName("Function_approximation")
        Function_approximation.resize(932, 671)
        Function_approximation.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(Function_approximation)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("background-color: rgb(207, 207, 207);\n"
                                     "border-color: rgb(207, 207, 207);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "border-radius: 10px;\n"
                                       "font-size: 15px;\n"
                                       "color: #0d7907;\n"
                                       "font: 1.2rem \"Fira Sans\", sans-serif;\n"
                                       "border:0.5px solid black;")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.spin = QtWidgets.QSpinBox(self.tab)
        self.spin.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                "border-radius: 10px;\n"
                                "font-size: 12px;\n"
                                "color: #0d7907;\n"
                                "font: 1.2rem \"Fira Sans\", sans-serif;\n"
                                "border:0.5px solid black;")
        self.spin.setObjectName("spin")
        self.verticalLayout_2.addWidget(self.spin)
        self.button_file = QtWidgets.QPushButton(self.tab)
        self.button_file.setStyleSheet("QPushButton {\n"
                                       "    background-color: rgb(255, 255, 255);\n"
                                       "    border-radius: 10px;\n"
                                       "    font-size: 15px;\n"
                                       "    color: #0d7907;\n"
                                       "    font: 1.2rem \"Fira Sans\", sans-serif;\n"
                                       "    border:0.5px solid black;\n"
                                       "}\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: lightgreen;\n"
                                       "}")
        self.button_file.setObjectName("button_file")
        self.verticalLayout_2.addWidget(self.button_file)
        self.clear_button_table = QtWidgets.QPushButton(self.tab)
        self.clear_button_table.setStyleSheet("QPushButton {\n"
                                              "    background-color: rgb(255, 255, 255);\n"
                                              "    border-radius: 10px;\n"
                                              "    font-size: 15px;\n"
                                              "    color: #0d7907;\n"
                                              "    font: 1.2rem \"Fira Sans\", sans-serif;\n"
                                              "    border:0.5px solid black;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "    background-color: lightgreen;\n"
                                              "}")
        self.clear_button_table.setObjectName("clear_button_table")
        self.verticalLayout_2.addWidget(self.clear_button_table)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setStyleSheet("border-radius: 10px;\n"
                                 "font-size: 12px;\n"
                                 "font: 1.2rem \"Fira Sans\", sans-serif;")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.linear_radioButton = QtWidgets.QRadioButton(self.tab)
        self.linear_radioButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                              "border-radius: 10px;\n"
                                              "font-size: 15px;\n"
                                              "color: #0d7907;\n"
                                              "font: 1.2rem \"Fira Sans\", sans-serif;\n"
                                              "border:0.5px solid black;")
        self.linear_radioButton.setObjectName("linear_radioButton")
        self.verticalLayout_3.addWidget(self.linear_radioButton)
        self.nonlinear_radioButton = QtWidgets.QRadioButton(self.tab)
        self.nonlinear_radioButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                 "border-radius: 10px;\n"
                                                 "font-size: 15px;\n"
                                                 "color: #0d7907;\n"
                                                 "font: 1.2rem \"Fira Sans\", sans-serif;\n"
                                                 "border:0.5px solid black;")
        self.nonlinear_radioButton.setObjectName("nonlinear_radioButton")
        self.verticalLayout_3.addWidget(self.nonlinear_radioButton)
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border-radius: 10px;\n"
                                    "font-size: 12px;\n"
                                    "color: #0d7907;\n"
                                    "font: 1.2rem \"Fira Sans\", sans-serif;\n"
                                    "border:0.5px solid black;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox)
        self.compare_checkBox = QtWidgets.QCheckBox(self.tab)
        self.compare_checkBox.setStyleSheet("font-size: 15px;\n"
                                            "border-radius: 20px;\n"
                                            "color: #0d7907;\n"
                                            "font: 1.2rem \"Fira Sans\", sans-serif;")
        self.compare_checkBox.setObjectName("compare_checkBox")
        self.verticalLayout_3.addWidget(self.compare_checkBox)
        self.run_button = QtWidgets.QPushButton(self.tab)
        self.run_button.setStyleSheet("QPushButton {\n"
                                      "    background-color: rgb(255, 255, 255);\n"
                                      "    border-radius: 10px;\n"
                                      "    font-size: 25px;\n"
                                      "    color: #D2691E;\n"
                                      "    font: 1.2rem \"Fira Sans\", sans-serif;\n"
                                      "    border:0.5px solid black;\n"
                                      "}\n"
                                      "QPushButton::hover{\n"
                                      "    background-color : lightgreen;\n"
                                      "}\n"
                                      "")
        self.run_button.setObjectName("run_button")
        self.verticalLayout_3.addWidget(self.run_button)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 3, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "border-radius: 10px;\n"
                                       "font-size: 12px;\n"
                                       "color: #0d7907;\n"
                                       "font: 1.2rem \"Fira Sans\", sans-serif;\n"
                                       "border:0.5px solid black;")
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 1, 1, 1)
        self.clear_button_browser = QtWidgets.QPushButton(self.tab)
        self.clear_button_browser.setStyleSheet("QPushButton {\n"
                                                "    background-color: rgb(255, 255, 255);\n"
                                                "    border-radius: 10px;\n"
                                                "    font-size: 15px;\n"
                                                "    color: #0d7907;\n"
                                                "    font: 1.2rem \"Fira Sans\", sans-serif;\n"
                                                "    border:0.5px solid black;\n"
                                                "}\n"
                                                "QPushButton:hover {\n"
                                                "    background-color: lightgreen;\n"
                                                "}")
        self.clear_button_browser.setObjectName("clear_button_browser")
        self.gridLayout.addWidget(self.clear_button_browser, 1, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout.addLayout(self.verticalLayout, 2, 1, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.view = QtWidgets.QTableView(self.tab_2)
        self.view.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                "border-radius: 10px;\n"
                                "color: #0d7907;\n"
                                "font: 1.2rem \"Fira Sans\", sans-serif;\n"
                                "border:0.5px solid black;")
        self.view.setObjectName("view")
        self.gridLayout_2.addWidget(self.view, 0, 0, 5, 1)
        self.id_spin = QtWidgets.QSpinBox(self.tab_2)
        self.id_spin.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "border-radius: 10px;\n"
                                   "font-size: 20px;\n"
                                   "color: #0d7907;\n"
                                   "font: 1.2rem \"Fira Sans\", sans-serif;\n"
                                   "border:0.5px solid black;")
        self.id_spin.setObjectName("id_spin")
        self.gridLayout_2.addWidget(self.id_spin, 0, 1, 1, 1)
        self.del_button = QtWidgets.QPushButton(self.tab_2)
        self.del_button.setStyleSheet("QPushButton {\n"
                                      "    background-color: rgb(255, 255, 255);\n"
                                      "    border-radius: 10px;\n"
                                      "    font-size: 20px;\n"
                                      "    color: #0d7907;\n"
                                      "    font: 1.2rem \"Fira Sans\", sans-serif;\n"
                                      "    border:0.5px solid black;\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: lightgreen;\n"
                                      "}")
        self.del_button.setObjectName("del_button")
        self.gridLayout_2.addWidget(self.del_button, 1, 1, 1, 1)
        self.save_button = QtWidgets.QPushButton(self.tab_2)
        self.save_button.setStyleSheet("QPushButton {\n"
                                       "    background-color: rgb(255, 255, 255);\n"
                                       "    border-radius: 10px;\n"
                                       "    font-size: 20px;\n"
                                       "    color: #0d7907;\n"
                                       "    font: 1.2rem \"Fira Sans\", sans-serif;\n"
                                       "    border:0.5px solid black;\n"
                                       "}\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: lightgreen;\n"
                                       "}")
        self.save_button.setObjectName("save_button")
        self.gridLayout_2.addWidget(self.save_button, 2, 1, 1, 1)
        self.change_button = QtWidgets.QPushButton(self.tab_2)
        self.change_button.setStyleSheet("QPushButton {\n"
                                         "    background-color: rgb(255, 255, 255);\n"
                                         "    border-radius: 10px;\n"
                                         "    font-size: 20px;\n"
                                         "    color: #0d7907;\n"
                                         "    font: 1.2rem \"Fira Sans\", sans-serif;\n"
                                         "    border:0.5px solid black;\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: lightgreen;\n"
                                         "}")
        self.change_button.setObjectName("change_button")
        self.gridLayout_2.addWidget(self.change_button, 3, 1, 1, 1)
        self.table_for_db = QtWidgets.QTableWidget(self.tab_2)
        self.table_for_db.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-radius: 10px;\n"
                                        "color: #0d7907;\n"
                                        "font: 1.2rem \"Fira Sans\", sans-serif;\n"
                                        "border:0.5px solid black;")
        self.table_for_db.setObjectName("table_for_db")
        self.table_for_db.setColumnCount(0)
        self.table_for_db.setRowCount(0)
        self.gridLayout_2.addWidget(self.table_for_db, 4, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)
        Function_approximation.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(Function_approximation)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 932, 21))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        self.menu_3 = QtWidgets.QMenu(self.menu)
        self.menu_3.setObjectName("menu_3")
        self.menu_2 = QtWidgets.QMenu(self.menuBar)
        self.menu_2.setObjectName("menu_2")
        Function_approximation.setMenuBar(self.menuBar)
        self.action_exit = QtWidgets.QAction(Function_approximation)
        self.action_exit.setObjectName("action_exit")
        self.action_rus = QtWidgets.QAction(Function_approximation)
        self.action_rus.setObjectName("action_rus")
        self.action_en = QtWidgets.QAction(Function_approximation)
        self.action_en.setObjectName("action_en")
        self.action_reference = QtWidgets.QAction(Function_approximation)
        self.action_reference.setObjectName("action_reference")
        self.menu_3.addAction(self.action_rus)
        self.menu_3.addAction(self.action_en)
        self.menu.addAction(self.menu_3.menuAction())
        self.menu.addSeparator()
        self.menu.addAction(self.action_exit)
        self.menu_2.addAction(self.action_reference)
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())

        self.retranslateUi(Function_approximation)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Function_approximation)

    def retranslateUi(self, Function_approximation):
        _translate = QtCore.QCoreApplication.translate
        Function_approximation.setWindowTitle(_translate("Function_approximation", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Function_approximation", "X"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Function_approximation", "Y"))
        self.button_file.setText(_translate("Function_approximation", "Выбор файла"))
        self.clear_button_table.setText(_translate("Function_approximation", "Очистить таблицу"))
        self.label.setText(_translate("Function_approximation", "Выберите вид аппроксимации:"))
        self.linear_radioButton.setText(_translate("Function_approximation", "Линейная"))
        self.nonlinear_radioButton.setText(_translate("Function_approximation", "Нелинейная"))
        self.comboBox.setItemText(0, _translate("Function_approximation", "Квадратичная: \'y = a*x^2+b*x+c\'"))
        self.comboBox.setItemText(1,
                                  _translate("Function_approximation", "Кубическая: \'y = a*x^3 + b*x^2 + c*x + d\'"))
        self.comboBox.setItemText(2, _translate("Function_approximation", "Степенная:  \'y = k*x^n\'"))
        self.comboBox.setItemText(3,
                                  _translate("Function_approximation", "Экспоненциальная I типа: \'y = a*exp(b^x)\'"))
        self.comboBox.setItemText(4, _translate("Function_approximation", "Экспоненциальная II типа: \'y = a*b^x\'"))
        self.comboBox.setItemText(5, _translate("Function_approximation", "Логарифмическая: \'y = b + a*log(x)\'"))
        self.comboBox.setItemText(6, _translate("Function_approximation", "Гиперболическая:  \'y = b+a/x\'"))
        self.compare_checkBox.setText(_translate("Function_approximation", "Сравнить"))
        self.run_button.setText(_translate("Function_approximation", "ПУСК"))
        self.clear_button_browser.setText(_translate("Function_approximation", "Очисть браузер"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Function_approximation", "Tab 1"))
        self.del_button.setText(_translate("Function_approximation", "Удалить"))
        self.save_button.setText(_translate("Function_approximation", "Сохранить"))
        self.change_button.setText(_translate("Function_approximation", "Загрузить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Function_approximation", "Tab 2"))
        self.menu.setTitle(_translate("Function_approximation", "Настройки"))
        self.menu_3.setTitle(_translate("Function_approximation", "Язык"))
        self.menu_2.setTitle(_translate("Function_approximation", "Справка"))
        self.action_exit.setText(
            _translate("Function_approximation", "Выход                                       Ctrl + Alt + Q"))
        self.action_rus.setText(_translate("Function_approximation", "Русский"))
        self.action_en.setText(_translate("Function_approximation", "Английский"))
        self.action_reference.setText(
            _translate("Function_approximation", "О прогрмме                                   F1"))
