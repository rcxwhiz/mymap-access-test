# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pickle_ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import os
import sys
from classroom.semester_manager import SemesterManager
from PyQt5 import QtCore, QtGui, QtWidgets

semesterManager = SemesterManager()


class Ui_Form(object):
    def setupUi(self, Form):
		# MY CODE
        self.assets = os.path.join(os.path.dirname(sys.argv[0]), 'assets')
        Form.setWindowTitle('Semesters')
        Form.setWindowIcon(QtGui.QIcon(os.path.join(self.assets, 'byu-icon.png')))
        
        Form.setObjectName("Form")
        Form.resize(295, 267)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 141, 16))
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 230, 216, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(10, 40, 271, 171))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.tableView = QtWidgets.QTableWidget(self.widget1)
        self.tableView.setObjectName("tableView")
        self.horizontalLayout_2.addWidget(self.tableView)
        self.tableView.setColumnCount(2)
        self.tableView.setHorizontalHeaderLabels(['Semester', 'Downloaded'])
        self.tableView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.verticalHeader().setVisible(False)

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget1)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.updateCachedSemester()

    def updateCachedSemester(self):
        self.tableView.setRowCount(len(semesterManager.semesters))
        semesters = semesterManager.cached_semesters()
        for i in range(len(semesters)):
            name = semesters[i]
            time = semesterManager.semesters[semesters[i]].datestamp
            self.tableView.setItem(i, 0, QtWidgets.QTableWidgetItem(name))
            self.tableView.setItem(i, 1, QtWidgets.QTableWidgetItem(time))
        self.tableView.resizeColumnsToContents()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Cached Semesters"))
        self.pushButton_3.setText(_translate("Form", "Get Semester"))
        self.pushButton.setText(_translate("Form", "Delete"))
        self.pushButton_2.setText(_translate("Form", "Refresh"))
        self.label_2.setText(_translate("Form", "Note: Getting and refreshing semesters may take about an hour."))
        self.pushButton_4.setText(_translate("Form", "Apply"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
