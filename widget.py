# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(900, 900)
        self.textBrowser = QtGui.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 881, 581))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.frame = QtGui.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 630, 881, 61))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.pushButton_import = QtGui.QPushButton(self.frame)
        self.pushButton_import.setGeometry(QtCore.QRect(20, 12, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Unicode MS"))
        font.setPointSize(12)
        self.pushButton_import.setFont(font)
        self.pushButton_import.setObjectName(_fromUtf8("pushButton_import"))
        self.pushButton_log = QtGui.QPushButton(self.frame)
        self.pushButton_log.setGeometry(QtCore.QRect(390, 10, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Unicode MS"))
        font.setPointSize(12)
        self.pushButton_log.setFont(font)
        self.pushButton_log.setObjectName(_fromUtf8("pushButton_log"))
        self.pushButton_start = QtGui.QPushButton(self.frame)
        self.pushButton_start.setGeometry(QtCore.QRect(760, 10, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Unicode MS"))
        font.setPointSize(12)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setObjectName(_fromUtf8("pushButton_start"))
        self.progressBar = QtGui.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(10, 600, 881, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.textBrowser_detail = QtGui.QTextBrowser(Form)
        self.textBrowser_detail.setGeometry(QtCore.QRect(10, 700, 881, 191))
        self.textBrowser_detail.setObjectName(_fromUtf8("textBrowser_detail"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Phonetic symbol", None))
        self.pushButton_import.setText(_translate("Form", "导入文件", None))
        self.pushButton_log.setText(_translate("Form", "打开log", None))
        self.pushButton_start.setText(_translate("Form", "开始", None))

