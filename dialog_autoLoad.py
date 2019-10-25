# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_autoLoad.ui'
#
# Created: Thu Feb 25 20:10:19 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(843, 281)
        self.pB_cp_from = QtGui.QPushButton(Dialog)
        self.pB_cp_from.setGeometry(QtCore.QRect(40, 35, 121, 41))
        self.pB_cp_from.setObjectName("pB_cp_from")
        self.tB_DatDir = QtGui.QTextBrowser(Dialog)
        self.tB_DatDir.setGeometry(QtCore.QRect(180, 35, 581, 41))
        self.tB_DatDir.setObjectName("tB_DatDir")
        self.tB_cp_direction = QtGui.QTextBrowser(Dialog)
        self.tB_cp_direction.setGeometry(QtCore.QRect(180, 95, 581, 41))
        self.tB_cp_direction.setObjectName("tB_cp_direction")
        self.pB_cp_direction = QtGui.QPushButton(Dialog)
        self.pB_cp_direction.setGeometry(QtCore.QRect(40, 96, 121, 41))
        self.pB_cp_direction.setObjectName("pB_cp_direction")
        self.spinBox = QtGui.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(650, 160, 111, 27))
        self.spinBox.setMaximum(1800)
        self.spinBox.setProperty("value", 1200)
        self.spinBox.setObjectName("spinBox")
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(550, 165, 91, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pB_exec = QtGui.QPushButton(Dialog)
        self.pB_exec.setGeometry(QtCore.QRect(40, 210, 121, 41))
        self.pB_exec.setAutoDefault(True)
        self.pB_exec.setObjectName("pB_exec")
        self.pB_close = QtGui.QPushButton(Dialog)
        self.pB_close.setGeometry(QtCore.QRect(640, 210, 121, 41))
        self.pB_close.setObjectName("pB_close")
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(190, 223, 381, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(140, 165, 61, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(200, 160, 113, 27))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(420, 160, 113, 27))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(340, 165, 81, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.pB_cp_from.setText(QtGui.QApplication.translate("Dialog", "Open Data Dir.", None, QtGui.QApplication.UnicodeUTF8))
        self.pB_cp_direction.setText(QtGui.QApplication.translate("Dialog", "Copy Direction", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Wait for [s]", None, QtGui.QApplication.UnicodeUTF8))
        self.pB_exec.setText(QtGui.QApplication.translate("Dialog", "exec auto Load", None, QtGui.QApplication.UnicodeUTF8))
        self.pB_close.setText(QtGui.QApplication.translate("Dialog", "close", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "header:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setToolTip(QtGui.QApplication.translate("Dialog", "<html><head/><body><p>write a common part of data files (ex. a_001_0001.dat, a_001_0002.dat, =&gt; \'ax\')</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_2.setToolTip(QtGui.QApplication.translate("Dialog", "<html><head/><body><p>write a common extention (ex. a_001_0001.dat, a_001_0002.dat, =&gt; \'dat\')</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_2.setText(QtGui.QApplication.translate("Dialog", "dat", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "extention:", None, QtGui.QApplication.UnicodeUTF8))

