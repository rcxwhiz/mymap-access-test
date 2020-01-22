# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'single_class.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from classroom.semester_manager import SemesterManager

semesterManager = SemesterManager()


class Ui_Form(object):
    def setupUi(self, Form, big_ui_ref):
        self.form_ref = Form
        self.assets = os.path.join(os.path.dirname(sys.argv[0]), 'assets')
        Form.setWindowIcon(QtGui.QIcon(os.path.join(self.assets, 'byu-icon.png')))

        Form.setObjectName("Form")
        Form.resize(1205, 205)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 1181, 141))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setObjectName("tableWidget")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 160, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(big_ui_ref.apply_clicked_section)
        self.pushButton.clicked.connect(self.form_ref.hide)
        self.pushButton.clicked.connect(self.wipeTable)

        self.headers = ['Class',
                   'Section',
                   'Instructor',
                   'Days',
                   'Start Times',
                   'End Times',
                   'Location',
                   'Type',
                   'Total Seats',
                   'Offered']

        self.tableWidget.setHorizontalHeaderLabels(self.headers)

        self.tableWidget.verticalHeader().setVisible(False)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def wipeTable(self):
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setHorizontalHeaderLabels(self.headers)

    def setInfo(self, semester_year, course_name, section_num):
        self.form_ref.setWindowTitle(f'{semester_year.semester_year} - {course_name.short_title} - Section {section_num.section_num}')
        self.semester_year = semester_year
        self.course_name = course_name
        self.section_num = section_num

    def populateTable(self, info):
        self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(info[1].short_title))
        self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(str(info[2].section_num)))
        self.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem(info[2].instructor))
        self.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem('\n'.join(info[2].days)))
        self.tableWidget.setItem(0, 4, QtWidgets.QTableWidgetItem('\n'.join(info[2].start)))
        self.tableWidget.setItem(0, 5, QtWidgets.QTableWidgetItem('\n'.join(info[2].end)))
        self.tableWidget.setItem(0, 6, QtWidgets.QTableWidgetItem(info[2].location))
        self.tableWidget.setItem(0, 7, QtWidgets.QTableWidgetItem(info[2].type))
        self.tableWidget.setItem(0, 8, QtWidgets.QTableWidgetItem(info[2].seats))
        self.tableWidget.setItem(0, 9, QtWidgets.QTableWidgetItem(info[1].offered))

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("Form", "Choose Section"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
