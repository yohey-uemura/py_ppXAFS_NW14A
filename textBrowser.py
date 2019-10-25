# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'textBrowser.ui'
#
# Created: Wed Feb 17 17:51:09 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(670, 646)
        self.textBrowser = QtGui.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(50, 150, 571, 421))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(280, 591, 110, 41))
        self.pushButton.setObjectName("pushButton")
        self.spinBox = QtGui.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(470, 30, 121, 24))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.spinBox.setFont(font)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(9999)
        self.spinBox.setObjectName("spinBox")
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(380, 33, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textBrowser_2 = QtGui.QTextBrowser(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(150, 60, 471, 41))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(60, 70, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(190, 110, 431, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(80, 115, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.spinBox, self.textBrowser_2)
        Form.setTabOrder(self.textBrowser_2, self.lineEdit)
        Form.setTabOrder(self.lineEdit, self.textBrowser)
        Form.setTabOrder(self.textBrowser, self.pushButton)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Read from:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "File Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setText(QtGui.QApplication.translate("Form", "k, chi_pos, chi_neg", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Columns:", None, QtGui.QApplication.UnicodeUTF8))

