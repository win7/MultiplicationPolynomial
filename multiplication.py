# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'multiplication.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from multiplication_polynomial import *
from numpy import *

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1103, 659)
        font = QtGui.QFont()
        font.setPointSize(11)
        Dialog.setFont(font)
        Dialog.setToolTip("")
        Dialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(360, 0, 331, 34))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 50, 1091, 51))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 71, 18))
        self.label_2.setObjectName("label_2")
        self.toolButton_load = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_load.setGeometry(QtCore.QRect(80, 10, 33, 34))
        self.toolButton_load.setObjectName("toolButton_load")
        self.pushButton_calculate = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_calculate.setGeometry(QtCore.QRect(900, 10, 88, 34))
        self.pushButton_calculate.setObjectName("pushButton_calculate")
        self.comboBox_method = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_method.setGeometry(QtCore.QRect(753, 10, 141, 31))
        self.comboBox_method.setObjectName("comboBox_method")
        self.comboBox_method.addItem("")
        self.comboBox_method.addItem("")
        self.comboBox_method.addItem("")
        self.comboBox_method.addItem("")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(670, 20, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_clear = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_clear.setGeometry(QtCore.QRect(990, 10, 88, 34))
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(9, 110, 490, 121))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 40, 58, 18))
        self.label_4.setObjectName("label_4")
        self.lineEdit_poly_a = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_poly_a.setGeometry(QtCore.QRect(70, 30, 411, 32))
        self.lineEdit_poly_a.setObjectName("lineEdit_poly_a")
        self.label_poly_a = QtWidgets.QLabel(self.groupBox_2)
        self.label_poly_a.setGeometry(QtCore.QRect(10, 90, 471, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_poly_a.setFont(font)
        self.label_poly_a.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_poly_a.setMidLineWidth(0)
        self.label_poly_a.setAlignment(QtCore.Qt.AlignCenter)
        self.label_poly_a.setObjectName("label_poly_a")
        self.label_41 = QtWidgets.QLabel(self.groupBox_2)
        self.label_41.setGeometry(QtCore.QRect(70, 60, 411, 18))
        self.label_41.setObjectName("label_41")
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(610, 110, 490, 121))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(10, 40, 58, 18))
        self.label_5.setObjectName("label_5")
        self.lineEdit_poly_b = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_poly_b.setGeometry(QtCore.QRect(70, 30, 411, 32))
        self.lineEdit_poly_b.setObjectName("lineEdit_poly_b")
        self.label_poly_b = QtWidgets.QLabel(self.groupBox_3)
        self.label_poly_b.setGeometry(QtCore.QRect(10, 90, 471, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_poly_b.setFont(font)
        self.label_poly_b.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_poly_b.setMidLineWidth(0)
        self.label_poly_b.setAlignment(QtCore.Qt.AlignCenter)
        self.label_poly_b.setObjectName("label_poly_b")
        self.label_42 = QtWidgets.QLabel(self.groupBox_3)
        self.label_42.setGeometry(QtCore.QRect(70, 60, 411, 18))
        self.label_42.setObjectName("label_42")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 290, 1091, 361))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.tableWidget_vn_a = QtWidgets.QTableWidget(self.tab_1)
        self.tableWidget_vn_a.setGeometry(QtCore.QRect(2, 0, 300, 300))
        self.tableWidget_vn_a.setObjectName("tableWidget_vn_a")
        self.tableWidget_vn_a.setColumnCount(0)
        self.tableWidget_vn_a.setRowCount(0)
        self.tableWidget_vn_a.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_vn_a.horizontalHeader().setDefaultSectionSize(60)
        self.tableWidget_coff_a = QtWidgets.QTableWidget(self.tab_1)
        self.tableWidget_coff_a.setGeometry(QtCore.QRect(310, 0, 100, 300))
        self.tableWidget_coff_a.setObjectName("tableWidget_coff_a")
        self.tableWidget_coff_a.setColumnCount(0)
        self.tableWidget_coff_a.setRowCount(0)
        self.tableWidget_coff_a.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_coff_a.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget_dft_a = QtWidgets.QTableWidget(self.tab_1)
        self.tableWidget_dft_a.setGeometry(QtCore.QRect(420, 0, 100, 300))
        self.tableWidget_dft_a.setObjectName("tableWidget_dft_a")
        self.tableWidget_dft_a.setColumnCount(0)
        self.tableWidget_dft_a.setRowCount(0)
        self.tableWidget_dft_a.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_dft_a.horizontalHeader().setDefaultSectionSize(100)
        self.label_6 = QtWidgets.QLabel(self.tab_1)
        self.label_6.setGeometry(QtCore.QRect(130, 300, 31, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_1)
        self.label_7.setGeometry(QtCore.QRect(350, 300, 16, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_1)
        self.label_8.setGeometry(QtCore.QRect(440, 300, 51, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab_1)
        self.label_9.setGeometry(QtCore.QRect(300, 300, 16, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab_1)
        self.label_10.setGeometry(QtCore.QRect(410, 300, 16, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab_1)
        self.label_11.setGeometry(QtCore.QRect(690, 270, 31, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.tableWidget_coff_b = QtWidgets.QTableWidget(self.tab_1)
        self.tableWidget_coff_b.setGeometry(QtCore.QRect(870, 0, 100, 300))
        self.tableWidget_coff_b.setObjectName("tableWidget_coff_b")
        self.tableWidget_coff_b.setColumnCount(0)
        self.tableWidget_coff_b.setRowCount(0)
        self.tableWidget_coff_b.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_coff_b.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget_vn_b = QtWidgets.QTableWidget(self.tab_1)
        self.tableWidget_vn_b.setGeometry(QtCore.QRect(560, 0, 300, 300))
        self.tableWidget_vn_b.setObjectName("tableWidget_vn_b")
        self.tableWidget_vn_b.setColumnCount(0)
        self.tableWidget_vn_b.setRowCount(0)
        self.tableWidget_vn_b.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_vn_b.horizontalHeader().setDefaultSectionSize(60)
        self.tableWidget_dft_b = QtWidgets.QTableWidget(self.tab_1)
        self.tableWidget_dft_b.setGeometry(QtCore.QRect(980, 0, 100, 300))
        self.tableWidget_dft_b.setObjectName("tableWidget_dft_b")
        self.tableWidget_dft_b.setColumnCount(0)
        self.tableWidget_dft_b.setRowCount(0)
        self.tableWidget_dft_b.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_dft_b.horizontalHeader().setDefaultSectionSize(100)
        self.label_12 = QtWidgets.QLabel(self.tab_1)
        self.label_12.setGeometry(QtCore.QRect(690, 300, 31, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab_1)
        self.label_13.setGeometry(QtCore.QRect(970, 300, 16, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tab_1)
        self.label_14.setGeometry(QtCore.QRect(910, 300, 16, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.tab_1)
        self.label_15.setGeometry(QtCore.QRect(1000, 300, 51, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.label_23 = QtWidgets.QLabel(self.tab_1)
        self.label_23.setGeometry(QtCore.QRect(860, 300, 16, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget_yn = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_yn.setGeometry(QtCore.QRect(570, 0, 100, 300))
        self.tableWidget_yn.setObjectName("tableWidget_yn")
        self.tableWidget_yn.setColumnCount(0)
        self.tableWidget_yn.setRowCount(0)
        self.tableWidget_yn.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_yn.horizontalHeader().setDefaultSectionSize(100)
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setGeometry(QtCore.QRect(490, 300, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.tab_2)
        self.label_17.setGeometry(QtCore.QRect(610, 300, 21, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.tableWidget_dft_b_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_dft_b_2.setGeometry(QtCore.QRect(460, 0, 100, 300))
        self.tableWidget_dft_b_2.setObjectName("tableWidget_dft_b_2")
        self.tableWidget_dft_b_2.setColumnCount(0)
        self.tableWidget_dft_b_2.setRowCount(0)
        self.tableWidget_dft_b_2.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_dft_b_2.horizontalHeader().setDefaultSectionSize(100)
        self.label_18 = QtWidgets.QLabel(self.tab_2)
        self.label_18.setGeometry(QtCore.QRect(560, 300, 16, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.tableWidget_dft_a_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_dft_a_2.setGeometry(QtCore.QRect(355, 0, 100, 300))
        self.tableWidget_dft_a_2.setObjectName("tableWidget_dft_a_2")
        self.tableWidget_dft_a_2.setColumnCount(0)
        self.tableWidget_dft_a_2.setRowCount(0)
        self.tableWidget_dft_a_2.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_dft_a_2.horizontalHeader().setDefaultSectionSize(100)
        self.label_19 = QtWidgets.QLabel(self.tab_2)
        self.label_19.setGeometry(QtCore.QRect(380, 300, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.tab_2)
        self.label_20.setGeometry(QtCore.QRect(450, 300, 16, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_21 = QtWidgets.QLabel(self.tab_3)
        self.label_21.setGeometry(QtCore.QRect(480, 300, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.tableWidget_vn_inv = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_vn_inv.setGeometry(QtCore.QRect(360, 0, 300, 300))
        self.tableWidget_vn_inv.setObjectName("tableWidget_vn_inv")
        self.tableWidget_vn_inv.setColumnCount(0)
        self.tableWidget_vn_inv.setRowCount(0)
        self.tableWidget_vn_inv.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_vn_inv.horizontalHeader().setDefaultSectionSize(60)
        self.label_22 = QtWidgets.QLabel(self.tab_3)
        self.label_22.setGeometry(QtCore.QRect(710, 300, 21, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.tableWidget_yn_2 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_yn_2.setGeometry(QtCore.QRect(670, 0, 100, 300))
        self.tableWidget_yn_2.setObjectName("tableWidget_yn_2")
        self.tableWidget_yn_2.setColumnCount(0)
        self.tableWidget_yn_2.setRowCount(0)
        self.tableWidget_yn_2.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_yn_2.horizontalHeader().setDefaultSectionSize(100)
        self.label_24 = QtWidgets.QLabel(self.tab_3)
        self.label_24.setGeometry(QtCore.QRect(350, 300, 16, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.label_40 = QtWidgets.QLabel(self.tab_3)
        self.label_40.setGeometry(QtCore.QRect(290, 300, 21, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_40.setFont(font)
        self.label_40.setAlignment(QtCore.Qt.AlignCenter)
        self.label_40.setObjectName("label_40")
        self.tableWidget_coff_c = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_coff_c.setGeometry(QtCore.QRect(250, 0, 100, 300))
        self.tableWidget_coff_c.setObjectName("tableWidget_coff_c")
        self.tableWidget_coff_c.setColumnCount(0)
        self.tableWidget_coff_c.setRowCount(0)
        self.tableWidget_coff_c.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_coff_c.horizontalHeader().setDefaultSectionSize(100)
        self.label_coff_c = QtWidgets.QLabel(self.tab_3)
        self.label_coff_c.setGeometry(QtCore.QRect(210, 230, 381, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_coff_c.setFont(font)
        self.label_coff_c.setText("")
        self.label_coff_c.setObjectName("label_coff_c")
        self.label_25 = QtWidgets.QLabel(self.tab_3)
        self.label_25.setGeometry(QtCore.QRect(660, 300, 21, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.tabWidget.addTab(self.tab_3, "")
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 240, 1091, 41))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_solution = QtWidgets.QLabel(self.groupBox_4)
        self.label_solution.setGeometry(QtCore.QRect(10, 5, 1071, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_solution.setFont(font)
        self.label_solution.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_solution.setMidLineWidth(0)
        self.label_solution.setAlignment(QtCore.Qt.AlignCenter)
        self.label_solution.setObjectName("label_solution")

        self.pushButton_calculate.clicked.connect(self.calculate)
        self.pushButton_clear.clicked.connect(self.clear)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "FFT-ADA"))
        self.label.setToolTip(_translate("Dialog", "ddd"))
        self.label.setText(_translate("Dialog", "Multiplication of Polynomials"))
        self.label_2.setText(_translate("Dialog", "Load file:"))
        self.toolButton_load.setText(_translate("Dialog", "..."))
        self.pushButton_calculate.setText(_translate("Dialog", "Calculate"))
        self.comboBox_method.setItemText(0, _translate("Dialog", "Mandermonde I"))
        self.comboBox_method.setItemText(1, _translate("Dialog", "Vandermonde R"))
        self.comboBox_method.setItemText(2, _translate("Dialog", "Bit Reverso"))
        self.comboBox_method.setItemText(3, _translate("Dialog", "Lagrange"))
        self.label_3.setText(_translate("Dialog", "Methods:"))
        self.pushButton_clear.setText(_translate("Dialog", "Clear"))
        self.groupBox_2.setTitle(_translate("Dialog", "Polynomial one"))
        self.label_4.setText(_translate("Dialog", "Coeff.:"))
        self.label_poly_a.setText(_translate("Dialog", "..."))
        self.label_41.setText(_translate("Dialog", "Example:  1, 2, 0, 0 for (1 + 2x +0x^2 + 0x^3)"))
        self.groupBox_3.setTitle(_translate("Dialog", "Polynomial two"))
        self.label_5.setText(_translate("Dialog", "Coeff.:"))
        self.label_poly_b.setText(_translate("Dialog", "..."))
        self.label_42.setText(_translate("Dialog", "Example: 1, 1, 0, 0 for (1 - 1x +0x^2 + 0x^3)"))
        self.label_6.setText(_translate("Dialog", "Vn"))
        self.label_7.setText(_translate("Dialog", "a"))
        self.label_8.setText(_translate("Dialog", "DFT(a)"))
        self.label_9.setText(_translate("Dialog", "."))
        self.label_10.setText(_translate("Dialog", "="))
        self.label_11.setText(_translate("Dialog", "Vn"))
        self.label_12.setText(_translate("Dialog", "Vn"))
        self.label_13.setText(_translate("Dialog", "="))
        self.label_14.setText(_translate("Dialog", "b"))
        self.label_15.setText(_translate("Dialog", "DFT(b)"))
        self.label_23.setText(_translate("Dialog", "."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("Dialog", "Evaluate"))
        self.label_16.setText(_translate("Dialog", "DFT(b)"))
        self.label_17.setText(_translate("Dialog", "Yn"))
        self.label_18.setText(_translate("Dialog", "="))
        self.label_19.setText(_translate("Dialog", "DFT(a)"))
        self.label_20.setText(_translate("Dialog", "."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Multi. point"))
        self.label_21.setText(_translate("Dialog", "Vn^-1"))
        self.label_22.setText(_translate("Dialog", "Yn"))
        self.label_24.setText(_translate("Dialog", "="))
        self.label_40.setText(_translate("Dialog", "c"))
        self.label_25.setText(_translate("Dialog", "."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Interpolation"))
        self.label_solution.setText(_translate("Dialog", "..."))

    def clear(self):
        self.initComponent(0, 0)

    def initComponent(self, c, n):
        self.label_poly_a.setText("...")
        self.label_poly_b.setText("...")
        self.label_solution.setText("...")

        self.tableWidget_vn_a.setColumnCount(n)
        self.tableWidget_vn_a.setRowCount(n)
        self.tableWidget_coff_a.setColumnCount(c)
        self.tableWidget_coff_a.setRowCount(n)
        self.tableWidget_dft_a.setColumnCount(c)
        self.tableWidget_dft_a.setRowCount(n)
        self.tableWidget_dft_a_2.setColumnCount(c)
        self.tableWidget_dft_a_2.setRowCount(n)

        self.tableWidget_vn_b.setColumnCount(n)
        self.tableWidget_vn_b.setRowCount(n)
        self.tableWidget_coff_b.setColumnCount(c)
        self.tableWidget_coff_b.setRowCount(n)
        self.tableWidget_dft_b.setColumnCount(c)
        self.tableWidget_dft_b.setRowCount(n)
        self.tableWidget_dft_b_2.setColumnCount(c)
        self.tableWidget_dft_b_2.setRowCount(n)

        self.tableWidget_yn.setColumnCount(c)
        self.tableWidget_yn.setRowCount(n)
        self.tableWidget_yn_2.setColumnCount(c)
        self.tableWidget_yn_2.setRowCount(n)

        self.tableWidget_vn_inv.setColumnCount(n)
        self.tableWidget_vn_inv.setRowCount(n)
        self.tableWidget_yn_2.setColumnCount(c)
        self.tableWidget_yn_2.setRowCount(n)
        self.tableWidget_coff_c.setColumnCount(c)
        self.tableWidget_coff_c.setRowCount(n)

    def dialogMessage(self, message):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Information")
        msgBox.setText(message)
        msgBox.setStandardButtons(QMessageBox.Ok )
        msgBox.exec_()

    def calculate(self):
        try:
            # a = array([1,0,2.5,0,1,0,0,0])
            # b = array([0,2.5,1,0,0,0,0,0])
            # a = array([1, 2, 0, 0])
            # b = array([1, 1, 0, 0])

            a = array(map(float, self.lineEdit_poly_a.text().split(",")))
            b = array(map(float, self.lineEdit_poly_b.text().split(",")))
            n = len(a)
            if len(a) != len(b):
                self.dialogMessage("Verify input")
                return
        except Exception as e:
            self.dialogMessage("Verify input")
            return
        
        self.initComponent(1, n)

        option = self.comboBox_method.currentIndex()
        if option == 0:
            # EVALUATE
            Vn = MatrixVandermodeI(n)
            dft_a = RecursiveFFT(a)
            dft_b = RecursiveFFT(b)
            # PRODUCT POINT
            Yn =  dft_a * dft_b
            # INTERPOLATION
            Vn_inv = 1 / Vn
            c = around(((1.0 / n) * dot(Vn_inv, Yn.transpose()).real), 2)
        elif option == 1:
            # EVALUATE
            Vn = MatrixVandermodeR(n)
            dft_a = dot(Vn, a.transpose())
            dft_b = dot(Vn, b.transpose())
            # PRODUCT POINT
            Yn =  dft_a * dft_b
            # INTERPOLATION
            Vn_inv = linalg.inv(Vn)
            c = around((dot(Vn_inv, Yn.transpose()).real), 2)
        elif option == 2:
            # EVALUATE
            Vn = MatrixVandermodeI(n)
            dft_a = IterativeFFT(a)
            dft_b = IterativeFFT(b)
            # PRODUCT POINT
            Yn =  dft_a * dft_b
            # INTERPOLATION
            Vn_inv = 1 / Vn
            c = around(((1.0 / n) * dot(Vn_inv, Yn.transpose()).real), 2)
        elif option == 3:
            self.dialogMessage("No implementation...")
            self.initComponent(0, 0)
            return

        # INPUT
        self.label_poly_a.setText(FormatPolynomial(a))
        self.label_poly_b.setText(FormatPolynomial(b))

        # OUTPUT
        self.label_solution.setText(FormatPolynomial(c))

        # EVALUATE
        for i in range(n):
            for j in range(n):
                item = QtWidgets.QTableWidgetItem(str(Vn[i][j]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                # item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable)
                self.tableWidget_vn_a.setItem(i, j, item)

                item = QtWidgets.QTableWidgetItem(str(Vn[i][j]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                # item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable)
                self.tableWidget_vn_b.setItem(i, j, item)

        for i in range(1):
            for j in range(n):
                item = QtWidgets.QTableWidgetItem(str(a[j]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                # item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable)
                self.tableWidget_coff_a.setItem(i, j, item)
                
                item = QtWidgets.QTableWidgetItem(str(b[j]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                # item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable)
                self.tableWidget_coff_b.setItem(i, j, item)

        for i in range(1):
            for j in range(n):
                item = QtWidgets.QTableWidgetItem(str(dft_a[j]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                # item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable)
                self.tableWidget_dft_a.setItem(i, j, item)

                item = QtWidgets.QTableWidgetItem(str(dft_b[j]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                # item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable)
                self.tableWidget_dft_b.setItem(i, j, item)

        # PRODUCT POINT
        for i in range(1):
            for j in range(n):
                item = QtWidgets.QTableWidgetItem(str(dft_a[j]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                # item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable)
                self.tableWidget_dft_a_2.setItem(i, j, item)

                item = QtWidgets.QTableWidgetItem(str(dft_b[j]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                # item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable)
                self.tableWidget_dft_b_2.setItem(i, j, item)

                item = QtWidgets.QTableWidgetItem(str(Yn[j]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                # item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable)
                self.tableWidget_yn.setItem(i, j, item)

        # INTERPOLATION
        for i in range(n):
            for j in range(n):
                item = QtWidgets.QTableWidgetItem(str(Vn_inv[i][j]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                # item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable)
                self.tableWidget_vn_inv.setItem(i, j, item)

        for i in range(1):
            for j in range(n):
                item = QtWidgets.QTableWidgetItem(str(Yn[j]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                # item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable)
                self.tableWidget_yn_2.setItem(i, j, item)

                item = QtWidgets.QTableWidgetItem(str(c[j]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                # item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable)
                self.tableWidget_coff_c.setItem(i, j, item)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
