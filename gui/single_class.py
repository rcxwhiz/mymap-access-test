# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'single_class.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        # MY CODE
        self.assets = os.path.join(os.path.dirname(sys.argv[0]), 'assets')
        Form.setWindowTitle('BYU Schdeuling Tool')
        Form.setWindowIcon(QtGui.QIcon(os.path.join(self.assets, 'byu-icon.png')))

        Form.setObjectName("Form")
        Form.resize(1040, 60)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 1021, 41))
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setHorizontalHeaderLabels(['College', 'Course', 'Section', 'Title', 'Instructor', 'Time', 'Type', 'Days', 'Credits', 'Location'])

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
