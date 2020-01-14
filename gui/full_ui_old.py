# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'full_ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # MY CODE
        self.assets = os.path.join(os.path.dirname(sys.argv[0]), 'assets')
        MainWindow.setWindowTitle('BYU Schdeuling Tool')
        MainWindow.setWindowIcon(QtGui.QIcon(os.path.join(self.assets, 'byu-icon.png')))

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(380, 170)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 981, 681))
        self.stackedWidget.setObjectName("stackedWidget")
        self.searchPage = QtWidgets.QWidget()
        self.searchPage.setObjectName("searchPage")
        self.tableWidget = QtWidgets.QTableWidget(self.searchPage)
        self.tableWidget.setGeometry(QtCore.QRect(210, 40, 751, 621))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.semesterDisplay = QtWidgets.QTextBrowser(self.searchPage)
        self.semesterDisplay.setGeometry(QtCore.QRect(210, 0, 281, 31))
        self.semesterDisplay.setObjectName("semesterDisplay")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.searchPage)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 171, 621))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.searchCol_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.searchCol_3.setContentsMargins(0, 0, 0, 0)
        self.searchCol_3.setObjectName("searchCol_3")
        self.deptLabel_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.deptLabel_3.setObjectName("deptLabel_3")
        self.searchCol_3.addWidget(self.deptLabel_3)
        self.deptLineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.deptLineEdit_3.setObjectName("deptLineEdit_3")
        self.searchCol_3.addWidget(self.deptLineEdit_3)
        self.courseNumLabel_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.courseNumLabel_3.setObjectName("courseNumLabel_3")
        self.searchCol_3.addWidget(self.courseNumLabel_3)
        self.courseNumLineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.courseNumLineEdit_3.setObjectName("courseNumLineEdit_3")
        self.searchCol_3.addWidget(self.courseNumLineEdit_3)
        self.courseNameLabel_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.courseNameLabel_3.setObjectName("courseNameLabel_3")
        self.searchCol_3.addWidget(self.courseNameLabel_3)
        self.courseNameLineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.courseNameLineEdit_3.setObjectName("courseNameLineEdit_3")
        self.searchCol_3.addWidget(self.courseNameLineEdit_3)
        self.instructorLabel_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.instructorLabel_3.setObjectName("instructorLabel_3")
        self.searchCol_3.addWidget(self.instructorLabel_3)
        self.instructorLineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.instructorLineEdit_3.setObjectName("instructorLineEdit_3")
        self.searchCol_3.addWidget(self.instructorLineEdit_3)
        self.courseTypeLabel_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.courseTypeLabel_3.setObjectName("courseTypeLabel_3")
        self.searchCol_3.addWidget(self.courseTypeLabel_3)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.dayCheckbox_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.dayCheckbox_3.setObjectName("dayCheckbox_3")
        self.verticalLayout_12.addWidget(self.dayCheckbox_3)
        self.eveningCheckbox_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.eveningCheckbox_3.setObjectName("eveningCheckbox_3")
        self.verticalLayout_12.addWidget(self.eveningCheckbox_3)
        self.otherCheckbox_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.otherCheckbox_3.setObjectName("otherCheckbox_3")
        self.verticalLayout_12.addWidget(self.otherCheckbox_3)
        self.searchCol_3.addLayout(self.verticalLayout_12)
        self.dayLabel_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.dayLabel_3.setObjectName("dayLabel_3")
        self.searchCol_3.addWidget(self.dayLabel_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.mondayBox_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.mondayBox_3.setObjectName("mondayBox_3")
        self.verticalLayout_13.addWidget(self.mondayBox_3)
        self.wednesdayBox_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.wednesdayBox_3.setObjectName("wednesdayBox_3")
        self.verticalLayout_13.addWidget(self.wednesdayBox_3)
        self.fridayBox_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.fridayBox_3.setObjectName("fridayBox_3")
        self.verticalLayout_13.addWidget(self.fridayBox_3)
        self.horizontalLayout_7.addLayout(self.verticalLayout_13)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.tuesdayBox_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.tuesdayBox_3.setObjectName("tuesdayBox_3")
        self.verticalLayout_14.addWidget(self.tuesdayBox_3)
        self.thursdayBox_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.thursdayBox_3.setObjectName("thursdayBox_3")
        self.verticalLayout_14.addWidget(self.thursdayBox_3)
        self.saturdayBox_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.saturdayBox_3.setObjectName("saturdayBox_3")
        self.verticalLayout_14.addWidget(self.saturdayBox_3)
        self.horizontalLayout_7.addLayout(self.verticalLayout_14)
        self.searchCol_3.addLayout(self.horizontalLayout_7)
        self.creditsLabel_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.creditsLabel_3.setObjectName("creditsLabel_3")
        self.searchCol_3.addWidget(self.creditsLabel_3)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.maxCredits_3 = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.maxCredits_3.setObjectName("maxCredits_3")
        self.horizontalLayout_8.addWidget(self.maxCredits_3)
        self.minCredits_3 = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.minCredits_3.setObjectName("minCredits_3")
        self.horizontalLayout_8.addWidget(self.minCredits_3)
        self.searchCol_3.addLayout(self.horizontalLayout_8)
        self.courseLevelLabel_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.courseLevelLabel_3.setObjectName("courseLevelLabel_3")
        self.searchCol_3.addWidget(self.courseLevelLabel_3)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.level100_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.level100_3.setObjectName("level100_3")
        self.verticalLayout_15.addWidget(self.level100_3)
        self.level200_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.level200_3.setObjectName("level200_3")
        self.verticalLayout_15.addWidget(self.level200_3)
        self.level300_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.level300_3.setObjectName("level300_3")
        self.verticalLayout_15.addWidget(self.level300_3)
        self.level400_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.level400_3.setObjectName("level400_3")
        self.verticalLayout_15.addWidget(self.level400_3)
        self.horizontalLayout_9.addLayout(self.verticalLayout_15)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.level500_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.level500_3.setObjectName("level500_3")
        self.verticalLayout_16.addWidget(self.level500_3)
        self.level600_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.level600_3.setObjectName("level600_3")
        self.verticalLayout_16.addWidget(self.level600_3)
        self.level700_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.level700_3.setObjectName("level700_3")
        self.verticalLayout_16.addWidget(self.level700_3)
        self.horizontalLayout_9.addLayout(self.verticalLayout_16)
        self.searchCol_3.addLayout(self.horizontalLayout_9)
        self.backButton = QtWidgets.QPushButton(self.searchPage)
        self.backButton.setGeometry(QtCore.QRect(860, 0, 101, 31))
        self.backButton.setObjectName("backButton")
        self.picklesButton = QtWidgets.QPushButton(self.searchPage)
        self.picklesButton.setGeometry(QtCore.QRect(10, 0, 111, 31))
        self.picklesButton.setObjectName("picklesButton")
        self.stackedWidget.addWidget(self.searchPage)
        self.schedulePage = QtWidgets.QWidget()
        self.schedulePage.setObjectName("schedulePage")
        self.backButton_2 = QtWidgets.QPushButton(self.schedulePage)
        self.backButton_2.setGeometry(QtCore.QRect(870, 10, 101, 31))
        self.backButton_2.setObjectName("backButton_2")
        self.picklesButton_2 = QtWidgets.QPushButton(self.schedulePage)
        self.picklesButton_2.setGeometry(QtCore.QRect(20, 10, 111, 31))
        self.picklesButton_2.setObjectName("picklesButton_2")
        self.label_2 = QtWidgets.QLabel(self.schedulePage)
        self.label_2.setGeometry(QtCore.QRect(350, 220, 241, 141))
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.schedulePage)
        self.startPage = QtWidgets.QWidget()
        self.startPage.setObjectName("startPage")
        self.advancedSearchButton = QtWidgets.QPushButton(self.startPage)
        self.advancedSearchButton.setGeometry(QtCore.QRect(28, 90, 141, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.advancedSearchButton.sizePolicy().hasHeightForWidth())
        self.advancedSearchButton.setSizePolicy(sizePolicy)
        self.advancedSearchButton.setMinimumSize(QtCore.QSize(120, 50))
        self.advancedSearchButton.setMaximumSize(QtCore.QSize(150, 50))
        self.advancedSearchButton.setObjectName("advancedSearchButton")
        self.scheduleMakerButton = QtWidgets.QPushButton(self.startPage)
        self.scheduleMakerButton.setGeometry(QtCore.QRect(180, 90, 150, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scheduleMakerButton.sizePolicy().hasHeightForWidth())
        self.scheduleMakerButton.setSizePolicy(sizePolicy)
        self.scheduleMakerButton.setMinimumSize(QtCore.QSize(120, 50))
        self.scheduleMakerButton.setMaximumSize(QtCore.QSize(150, 50))
        self.scheduleMakerButton.setObjectName("scheduleMakerButton")
        self.label = QtWidgets.QLabel(self.startPage)
        self.label.setGeometry(QtCore.QRect(70, 10, 201, 71))
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.startPage)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        # MY CODE
        self.advancedSearchButton.clicked.connect(self.gotoSearchPage)
        self.scheduleMakerButton.clicked.connect(self.gotoSchedulePage)
        self.backButton.clicked.connect(self.gotoStartPage)
        self.backButton_2.clicked.connect(self.gotoStartPage)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        self.main_window_ref = MainWindow

    # MY CODE
    def makeWindowSmall(self):
        self.main_window_ref.resize(380, 170)

    # MY CODE
    def makeWindowBig(self):
        self.main_window_ref.resize(1000, 700)

    # MY CODE
    def gotoStartPage(self):
        self.makeWindowSmall()
        self.stackedWidget.setCurrentIndex(2)

    # MY CODE
    def gotoSearchPage(self):
        self.makeWindowBig()
        self.stackedWidget.setCurrentIndex(0)

    # MY CODE
    def gotoSchedulePage(self):
        self.makeWindowBig()
        self.stackedWidget.setCurrentIndex(1)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.semesterDisplay.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Would like to put the semester info here?</p></body></html>"))
        self.deptLabel_3.setText(_translate("MainWindow", "Dept."))
        self.courseNumLabel_3.setText(_translate("MainWindow", "Course Num."))
        self.courseNameLabel_3.setText(_translate("MainWindow", "Course Name"))
        self.instructorLabel_3.setText(_translate("MainWindow", "Instructor"))
        self.courseTypeLabel_3.setText(_translate("MainWindow", "Type"))
        self.dayCheckbox_3.setText(_translate("MainWindow", "DAY"))
        self.eveningCheckbox_3.setText(_translate("MainWindow", "EVENING"))
        self.otherCheckbox_3.setText(_translate("MainWindow", "Something?"))
        self.dayLabel_3.setText(_translate("MainWindow", "Day"))
        self.mondayBox_3.setText(_translate("MainWindow", "Monday"))
        self.wednesdayBox_3.setText(_translate("MainWindow", "Wednesday"))
        self.fridayBox_3.setText(_translate("MainWindow", "Friday"))
        self.tuesdayBox_3.setText(_translate("MainWindow", "Tuesday"))
        self.thursdayBox_3.setText(_translate("MainWindow", "Thursday"))
        self.saturdayBox_3.setText(_translate("MainWindow", "Saturday"))
        self.creditsLabel_3.setText(_translate("MainWindow", "Credits (Max - Min)"))
        self.courseLevelLabel_3.setText(_translate("MainWindow", "Course Level"))
        self.level100_3.setText(_translate("MainWindow", "100"))
        self.level200_3.setText(_translate("MainWindow", "200"))
        self.level300_3.setText(_translate("MainWindow", "300"))
        self.level400_3.setText(_translate("MainWindow", "400"))
        self.level500_3.setText(_translate("MainWindow", "500"))
        self.level600_3.setText(_translate("MainWindow", "600"))
        self.level700_3.setText(_translate("MainWindow", "700"))
        self.backButton.setText(_translate("MainWindow", "Back"))
        self.picklesButton.setText(_translate("MainWindow", "Choose Semester"))
        self.backButton_2.setText(_translate("MainWindow", "Back"))
        self.picklesButton_2.setText(_translate("MainWindow", "Choose Semester"))
        self.label_2.setText(_translate("MainWindow", "THIS IS AN EMPTY TEST PAGE"))
        self.advancedSearchButton.setText(_translate("MainWindow", "Advanced Search"))
        self.scheduleMakerButton.setText(_translate("MainWindow", "Schedule Maker"))
        self.label.setText(_translate("MainWindow", "BYU Class Scheduling & Search Tool\n"
"\n"
"version - 0.0.0\n"
"\n"
"Josh Bedwell"))


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()