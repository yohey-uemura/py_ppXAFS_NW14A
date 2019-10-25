# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plot_RawBk.ui'
#
# Created: Wed Feb 24 20:39:31 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(754, 724)
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(40, 30, 671, 501))
        self.widget.setObjectName("widget")
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(560, 630, 141, 31))
        self.pushButton.setObjectName("pushButton")
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(50, 570, 211, 111))
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.dsb_pos_bk_start = QtGui.QDoubleSpinBox(self.groupBox)
        self.dsb_pos_bk_start.setGeometry(QtCore.QRect(60, 30, 141, 27))
        self.dsb_pos_bk_start.setObjectName("dsb_pos_bk_start")
        self.dsb_pos_bk_end = QtGui.QDoubleSpinBox(self.groupBox)
        self.dsb_pos_bk_end.setGeometry(QtCore.QRect(60, 70, 141, 27))
        self.dsb_pos_bk_end.setObjectName("dsb_pos_bk_end")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 35, 41, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 75, 41, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(320, 570, 211, 111))
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.dsb_neg_bk_start = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.dsb_neg_bk_start.setGeometry(QtCore.QRect(60, 30, 141, 27))
        self.dsb_neg_bk_start.setObjectName("dsb_neg_bk_start")
        self.dsb_neg_bk_end = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.dsb_neg_bk_end.setGeometry(QtCore.QRect(60, 70, 141, 27))
        self.dsb_neg_bk_end.setObjectName("dsb_neg_bk_end")
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 35, 41, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 75, 41, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "close", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "Pos: background", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "start:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "end:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Dialog", "Neg: background", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "start:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "end:", None, QtGui.QApplication.UnicodeUTF8))

