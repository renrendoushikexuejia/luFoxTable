# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\MyCode\luFoxTable1.0\luFoxTable.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(358, 748)
        self.lineEditProjectName = QtWidgets.QLineEdit(Form)
        self.lineEditProjectName.setGeometry(QtCore.QRect(160, 20, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.lineEditProjectName.setFont(font)
        self.lineEditProjectName.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditProjectName.setReadOnly(True)
        self.lineEditProjectName.setObjectName("lineEditProjectName")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(20, 70, 321, 531))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(False)
        self.tableWidget.setFont(font)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(70)
        self.checkBoxAutoPaste = QtWidgets.QCheckBox(Form)
        self.checkBoxAutoPaste.setGeometry(QtCore.QRect(20, 620, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.checkBoxAutoPaste.setFont(font)
        self.checkBoxAutoPaste.setChecked(True)
        self.checkBoxAutoPaste.setObjectName("checkBoxAutoPaste")
        self.pushButtonOpen = QtWidgets.QPushButton(Form)
        self.pushButtonOpen.setGeometry(QtCore.QRect(20, 20, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButtonOpen.setFont(font)
        self.pushButtonOpen.setObjectName("pushButtonOpen")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(150, 620, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.comboBoxDelay = QtWidgets.QComboBox(Form)
        self.comboBoxDelay.setGeometry(QtCore.QRect(210, 620, 69, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.comboBoxDelay.setFont(font)
        self.comboBoxDelay.setObjectName("comboBoxDelay")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(290, 620, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 670, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(200, 720, 141, 16))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "luFoxTable"))
        self.checkBoxAutoPaste.setText(_translate("Form", "自动粘贴"))
        self.pushButtonOpen.setText(_translate("Form", "打开"))
        self.label_4.setText(_translate("Form", "延迟"))
        self.label.setText(_translate("Form", "秒"))
        self.label_2.setText(_translate("Form", "单击单元格自动复制"))
        self.label_3.setText(_translate("Form", "--luTools  by  tenting"))
