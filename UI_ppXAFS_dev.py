# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_ppXAFS_dev.ui'
#
# Created: Thu Feb 25 20:08:29 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1251, 700)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1201, 631))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.pushButton_10 = QtGui.QPushButton(self.tab_3)
        self.pushButton_10.setGeometry(QtCore.QRect(920, 550, 251, 41))
        self.pushButton_10.setObjectName("pushButton_10")
        self.groupBox = QtGui.QGroupBox(self.tab_3)
        self.groupBox.setGeometry(QtCore.QRect(10, 450, 350, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.dsB_pre_end = QtGui.QDoubleSpinBox(self.groupBox)
        self.dsB_pre_end.setGeometry(QtCore.QRect(240, 30, 101, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dsB_pre_end.setFont(font)
        self.dsB_pre_end.setMaximum(30000.0)
        self.dsB_pre_end.setObjectName("dsB_pre_end")
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(195, 35, 41, 16))
        self.label_2.setObjectName("label_2")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 34, 44, 16))
        self.label.setObjectName("label")
        self.dsB_pre_start = QtGui.QDoubleSpinBox(self.groupBox)
        self.dsB_pre_start.setGeometry(QtCore.QRect(70, 30, 111, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dsB_pre_start.setFont(font)
        self.dsB_pre_start.setMaximum(30000.0)
        self.dsB_pre_start.setObjectName("dsB_pre_start")
        self.pushButton_13 = QtGui.QPushButton(self.tab_3)
        self.pushButton_13.setGeometry(QtCore.QRect(380, 470, 91, 41))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_11 = QtGui.QPushButton(self.tab_3)
        self.pushButton_11.setGeometry(QtCore.QRect(380, 530, 91, 41))
        self.pushButton_11.setObjectName("pushButton_11")
        self.groupBox_2 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 520, 350, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.dsB_post_end = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.dsB_post_end.setGeometry(QtCore.QRect(240, 30, 101, 25))
        self.dsB_post_end.setMaximum(30000.0)
        self.dsB_post_end.setObjectName("dsB_post_end")
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(195, 35, 41, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 34, 41, 16))
        self.label_4.setObjectName("label_4")
        self.dsB_post_start = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.dsB_post_start.setGeometry(QtCore.QRect(70, 30, 111, 25))
        self.dsB_post_start.setMaximum(30000.0)
        self.dsB_post_start.setObjectName("dsB_post_start")
        self.pushButton = QtGui.QPushButton(self.tab_3)
        self.pushButton.setGeometry(QtCore.QRect(1060, 11, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.scrollArea = QtGui.QScrollArea(self.tab_3)
        self.scrollArea.setGeometry(QtCore.QRect(920, 50, 251, 491))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 249, 489))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.widget = QtGui.QWidget(self.tab_3)
        self.widget.setGeometry(QtCore.QRect(20, 20, 441, 381))
        self.widget.setObjectName("widget")
        self.widget_2 = QtGui.QWidget(self.tab_3)
        self.widget_2.setGeometry(QtCore.QRect(490, 20, 411, 561))
        self.widget_2.setObjectName("widget_2")
        self.combo_fynctype = QtGui.QComboBox(self.tab_3)
        self.combo_fynctype.setGeometry(QtCore.QRect(100, 415, 131, 27))
        self.combo_fynctype.setObjectName("combo_fynctype")
        self.combo_fynctype.addItem("")
        self.combo_fynctype.addItem("")
        self.combo_fynctype.addItem("")
        self.label_7 = QtGui.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(30, 420, 51, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.checkBox_2 = QtGui.QCheckBox(self.tab_3)
        self.checkBox_2.setGeometry(QtCore.QRect(260, 418, 141, 22))
        self.checkBox_2.setObjectName("checkBox_2")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox_3 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 50, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.rB_kpower0 = QtGui.QRadioButton(self.groupBox_3)
        self.rB_kpower0.setGeometry(QtCore.QRect(10, 35, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.rB_kpower0.setFont(font)
        self.rB_kpower0.setObjectName("rB_kpower0")
        self.rB_kpower1 = QtGui.QRadioButton(self.groupBox_3)
        self.rB_kpower1.setGeometry(QtCore.QRect(60, 35, 41, 20))
        self.rB_kpower1.setObjectName("rB_kpower1")
        self.rB_kpower2 = QtGui.QRadioButton(self.groupBox_3)
        self.rB_kpower2.setGeometry(QtCore.QRect(110, 35, 41, 20))
        self.rB_kpower2.setObjectName("rB_kpower2")
        self.rB_kpower3 = QtGui.QRadioButton(self.groupBox_3)
        self.rB_kpower3.setGeometry(QtCore.QRect(160, 35, 41, 20))
        self.rB_kpower3.setObjectName("rB_kpower3")
        self.widget_4 = QtGui.QWidget(self.tab_2)
        self.widget_4.setGeometry(QtCore.QRect(20, 140, 771, 451))
        self.widget_4.setObjectName("widget_4")
        self.scrollArea_3 = QtGui.QScrollArea(self.tab_2)
        self.scrollArea_3.setGeometry(QtCore.QRect(810, 59, 351, 501))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtGui.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 349, 499))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.pB_openchi = QtGui.QPushButton(self.tab_2)
        self.pB_openchi.setGeometry(QtCore.QRect(1060, 10, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pB_openchi.setFont(font)
        self.pB_openchi.setObjectName("pB_openchi")
        self.frame = QtGui.QFrame(self.tab_2)
        self.frame.setGeometry(QtCore.QRect(250, 20, 541, 101))
        self.frame.setFrameShape(QtGui.QFrame.WinPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_6 = QtGui.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(380, 40, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(120, 40, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.comBox_Pos = QtGui.QComboBox(self.frame)
        self.comBox_Pos.setGeometry(QtCore.QRect(10, 60, 251, 26))
        self.comBox_Pos.setObjectName("comBox_Pos")
        self.comBox_Neg = QtGui.QComboBox(self.frame)
        self.comBox_Neg.setGeometry(QtCore.QRect(280, 60, 251, 26))
        self.comBox_Neg.setObjectName("comBox_Neg")
        self.checkBox = QtGui.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(20, 10, 151, 18))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.pB_addchi = QtGui.QPushButton(self.tab_2)
        self.pB_addchi.setGeometry(QtCore.QRect(810, 10, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pB_addchi.setFont(font)
        self.pB_addchi.setObjectName("pB_addchi")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton_7 = QtGui.QPushButton(self.tab)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 20, 101, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_9 = QtGui.QPushButton(self.tab)
        self.pushButton_9.setGeometry(QtCore.QRect(20, 550, 241, 41))
        self.pushButton_9.setObjectName("pushButton_9")
        self.scrollArea_2 = QtGui.QScrollArea(self.tab)
        self.scrollArea_2.setGeometry(QtCore.QRect(20, 70, 241, 471))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 239, 469))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.widget_3 = QtGui.QWidget(self.tab)
        self.widget_3.setGeometry(QtCore.QRect(280, 20, 881, 571))
        self.widget_3.setObjectName("widget_3")
        self.pushButton_2 = QtGui.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 20, 141, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1251, 22))
        self.menubar.setObjectName("menubar")
        self.menuOption = QtGui.QMenu(self.menubar)
        self.menuOption.setObjectName("menuOption")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAuto_load = QtGui.QAction(MainWindow)
        self.actionAuto_load.setCheckable(True)
        self.actionAuto_load.setObjectName("actionAuto_load")
        self.actionBoost = QtGui.QAction(MainWindow)
        self.actionBoost.setCheckable(True)
        self.actionBoost.setObjectName("actionBoost")
        self.menuOption.addAction(self.actionAuto_load)
        self.menuOption.addAction(self.actionBoost)
        self.menubar.addAction(self.menuOption.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.combo_fynctype.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_10.setText(QtGui.QApplication.translate("MainWindow", "Select All", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Lower", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "End:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Start:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_13.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_11.setText(QtGui.QApplication.translate("MainWindow", "replot", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Upper", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "End:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Start:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_fynctype.setItemText(0, QtGui.QApplication.translate("MainWindow", "average", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_fynctype.setItemText(1, QtGui.QApplication.translate("MainWindow", "linear", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_fynctype.setItemText(2, QtGui.QApplication.translate("MainWindow", "victoreen", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Method", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_2.setText(QtGui.QApplication.translate("MainWindow", "show raw&bk", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("MainWindow", "XANES", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("MainWindow", "k weight(x)", None, QtGui.QApplication.UnicodeUTF8))
        self.rB_kpower0.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.rB_kpower1.setText(QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.rB_kpower2.setText(QtGui.QApplication.translate("MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.rB_kpower3.setText(QtGui.QApplication.translate("MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.pB_openchi.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Neg.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Pos.", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("MainWindow", "plot diff chi(k)", None, QtGui.QApplication.UnicodeUTF8))
        self.pB_addchi.setText(QtGui.QApplication.translate("MainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "EXAFS", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_7.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_9.setText(QtGui.QApplication.translate("MainWindow", "Save Sum", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "Select/Release All", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "TimeScan", None, QtGui.QApplication.UnicodeUTF8))
        self.menuOption.setTitle(QtGui.QApplication.translate("MainWindow", "Option", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAuto_load.setText(QtGui.QApplication.translate("MainWindow", "auto load", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBoost.setText(QtGui.QApplication.translate("MainWindow", "boost", None, QtGui.QApplication.UnicodeUTF8))
