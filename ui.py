# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tool.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(481, 662)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 30, 72, 15))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(110, 30, 281, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(30, 60, 411, 131))
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 381, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(60, 90, 81, 16))
        self.label_3.setObjectName("label_3")
        self.googletextBrowser = QtWidgets.QTextBrowser(self.groupBox)
        self.googletextBrowser.setGeometry(QtCore.QRect(150, 80, 221, 31))
        self.googletextBrowser.setObjectName("googletextBrowser")
        self.googlepushButton = QtWidgets.QPushButton(self.groupBox)
        self.googlepushButton.setGeometry(QtCore.QRect(120, 40, 93, 28))
        self.googlepushButton.setObjectName("googlepushButton")
        self.cleanButton = QtWidgets.QPushButton(Form)
        self.cleanButton.setGeometry(QtCore.QRect(400, 30, 51, 21))
        self.cleanButton.setObjectName("cleanButton")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 200, 411, 211))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 221, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 40, 72, 15))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(10, 70, 72, 15))
        self.label_6.setObjectName("label_6")
        self.userlineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.userlineEdit.setGeometry(QtCore.QRect(50, 40, 321, 21))
        self.userlineEdit.setObjectName("userlineEdit")
        self.passwordlineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.passwordlineEdit.setGeometry(QtCore.QRect(50, 70, 321, 21))
        self.passwordlineEdit.setObjectName("passwordlineEdit")
        self.testpushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.testpushButton.setGeometry(QtCore.QRect(50, 100, 93, 28))
        self.testpushButton.setObjectName("testpushButton")
        self.testtextBrowser = QtWidgets.QTextBrowser(self.groupBox_2)
        self.testtextBrowser.setGeometry(QtCore.QRect(150, 100, 111, 31))
        self.testtextBrowser.setObjectName("testtextBrowser")
        self.webpushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.webpushButton.setGeometry(QtCore.QRect(50, 140, 93, 28))
        self.webpushButton.setObjectName("webpushButton")
        self.webtextBrowser = QtWidgets.QTextBrowser(self.groupBox_2)
        self.webtextBrowser.setGeometry(QtCore.QRect(160, 170, 221, 31))
        self.webtextBrowser.setObjectName("webtextBrowser")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(60, 180, 81, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(30, 430, 72, 15))
        self.label_8.setObjectName("label_8")
        self.textlob = QtWidgets.QTextBrowser(Form)
        self.textlob.setGeometry(QtCore.QRect(30, 450, 411, 192))
        self.textlob.setObjectName("textlob")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "论文引用量"))
        self.label.setText(_translate("Form", "论文标题："))
        self.groupBox.setTitle(_translate("Form", "Google学术"))
        self.label_2.setText(_translate("Form", "请确保本机已连接vpn,并且可以正常访问Google学术"))
        self.label_3.setText(_translate("Form", "引用量为："))
        self.googlepushButton.setText(_translate("Form", "查询"))
        self.cleanButton.setText(_translate("Form", "清除"))
        self.groupBox_2.setTitle(_translate("Form", "web of science"))
        self.label_4.setText(_translate("Form", "内网登录（浙师大）"))
        self.label_5.setText(_translate("Form", "账号"))
        self.label_6.setText(_translate("Form", "密码"))
        self.testpushButton.setText(_translate("Form", "测试登录"))
        self.webpushButton.setText(_translate("Form", "查询"))
        self.label_7.setText(_translate("Form", "引用量为："))
        self.label_8.setText(_translate("Form", "日志"))
