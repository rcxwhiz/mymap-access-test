# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'full_ui_new.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets

import gui.pickle_ui
import gui.single_class
from classroom.semester_manager import SemesterManager
import classroom.schedule_tools

semesterManager = SemesterManager()

app = QtWidgets.QApplication(sys.argv)
PickleSelector = QtWidgets.QWidget()
singleClassSelector = QtWidgets.QWidget()
ClassViewer = QtWidgets.QWidget()
MainWindow = QtWidgets.QMainWindow()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, screenSize):
        # MY CODE
        self.assets = os.path.join(os.path.dirname(sys.argv[0]), 'assets')
        MainWindow.setWindowTitle('BYU Schdeuling Tool - No Semester Selected')
        MainWindow.setWindowIcon(QtGui.QIcon(os.path.join(self.assets, 'byu-icon.png')))
        self.screenSize = screenSize

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(380, 170)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 1081, 821))
        self.stackedWidget.setObjectName("stackedWidget")
        self.searchPage = QtWidgets.QWidget()
        self.searchPage.setObjectName("searchPage")

        self.tableWidget = QtWidgets.QTableWidget(self.searchPage)
        self.tableWidget.setGeometry(QtCore.QRect(210, 40, 861, 781))
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideNone)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setHorizontalHeaderLabels(['College', 'Course', 'Section', 'Title', 'Instructor', 'Time', 'Type', 'Days', 'Credits', 'Location'])
        self.tableWidget.setRowCount(0)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)

        self.verticalLayoutWidget = QtWidgets.QWidget(self.searchPage)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 171, 771))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.searchCol_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.searchCol_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.searchCol_3.setContentsMargins(0, 0, 0, 0)
        self.searchCol_3.setSpacing(0)
        self.searchCol_3.setObjectName("searchCol_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.deptLabel_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.deptLabel_3.setObjectName("deptLabel_3")
        self.verticalLayout_11.addWidget(self.deptLabel_3)
        self.deptLineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.deptLineEdit_3.setObjectName("deptLineEdit_3")
        self.verticalLayout_11.addWidget(self.deptLineEdit_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_11)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.courseNumLabel_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.courseNumLabel_3.setObjectName("courseNumLabel_3")
        self.verticalLayout_13.addWidget(self.courseNumLabel_3)
        self.courseNumLineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.courseNumLineEdit_3.setObjectName("courseNumLineEdit_3")
        self.verticalLayout_13.addWidget(self.courseNumLineEdit_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_13)
        self.searchCol_3.addLayout(self.horizontalLayout_2)
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
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.monCheck = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.monCheck.setObjectName("monCheck")
        self.verticalLayout_4.addWidget(self.monCheck)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.monTimeS = QtWidgets.QTimeEdit(self.verticalLayoutWidget)
        self.monTimeS.setTime(QtCore.QTime(8, 0))
        self.monTimeS.setObjectName("monTimeS")
        self.horizontalLayout_3.addWidget(self.monTimeS)
        self.monTimeE = QtWidgets.QTimeEdit(self.verticalLayoutWidget)
        self.monTimeE.setObjectName("monTimeE")
        self.horizontalLayout_3.addWidget(self.monTimeE)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_10.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tueCheck = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.tueCheck.setObjectName("tueCheck")
        self.verticalLayout_5.addWidget(self.tueCheck)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tueTimeS = QtWidgets.QTimeEdit(self.verticalLayoutWidget)
        self.tueTimeS.setObjectName("tueTimeS")
        self.horizontalLayout_4.addWidget(self.tueTimeS)
        self.tueTimeE = QtWidgets.QTimeEdit(self.verticalLayoutWidget)
        self.tueTimeE.setObjectName("tueTimeE")
        self.horizontalLayout_4.addWidget(self.tueTimeE)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout_10.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.wedCheck = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.wedCheck.setObjectName("wedCheck")
        self.verticalLayout_6.addWidget(self.wedCheck)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.wedTimeS = QtWidgets.QTimeEdit(self.verticalLayoutWidget)
        self.wedTimeS.setObjectName("wedTimeS")
        self.horizontalLayout_5.addWidget(self.wedTimeS)
        self.wedTimeE = QtWidgets.QTimeEdit(self.verticalLayoutWidget)
        self.wedTimeE.setObjectName("wedTimeE")
        self.horizontalLayout_5.addWidget(self.wedTimeE)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.verticalLayout_10.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.thurCheck = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.thurCheck.setObjectName("thurCheck")
        self.verticalLayout_7.addWidget(self.thurCheck)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.thurTimeS = QtWidgets.QTimeEdit(self.verticalLayoutWidget)
        self.thurTimeS.setObjectName("thurTimeS")
        self.horizontalLayout_6.addWidget(self.thurTimeS)
        self.thurTimeE = QtWidgets.QTimeEdit(self.verticalLayoutWidget)
        self.thurTimeE.setObjectName("thuTimeE")
        self.horizontalLayout_6.addWidget(self.thurTimeE)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.verticalLayout_10.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.friCheck = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.friCheck.setObjectName("friCheck")
        self.verticalLayout_8.addWidget(self.friCheck)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.friTimeS = QtWidgets.QTimeEdit(self.verticalLayoutWidget)
        self.friTimeS.setObjectName("friTimeS")
        self.horizontalLayout_10.addWidget(self.friTimeS)
        self.friTimeE = QtWidgets.QTimeEdit(self.verticalLayoutWidget)
        self.friTimeE.setObjectName("friTimeE")
        self.horizontalLayout_10.addWidget(self.friTimeE)
        self.verticalLayout_8.addLayout(self.horizontalLayout_10)
        self.verticalLayout_10.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.satCheck = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.satCheck.setObjectName("satCheck")
        self.verticalLayout_9.addWidget(self.satCheck)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.satTimeS = QtWidgets.QTimeEdit(self.verticalLayoutWidget)
        self.satTimeS.setObjectName("satTimeS")
        self.horizontalLayout_11.addWidget(self.satTimeS)
        self.satTimeE = QtWidgets.QTimeEdit(self.verticalLayoutWidget)
        self.satTimeE.setObjectName("satTimeE")
        self.horizontalLayout_11.addWidget(self.satTimeE)
        self.verticalLayout_9.addLayout(self.horizontalLayout_11)
        self.verticalLayout_10.addLayout(self.verticalLayout_9)
        self.searchCol_3.addLayout(self.verticalLayout_10)
        self.courseTypeLabel_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.courseTypeLabel_3.setObjectName("courseTypeLabel_3")
        self.searchCol_3.addWidget(self.courseTypeLabel_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.dayCheckbox_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.dayCheckbox_3.setObjectName("dayCheckbox_3")
        self.verticalLayout_12.addWidget(self.dayCheckbox_3)
        self.eveningCheckbox_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.eveningCheckbox_3.setObjectName("eveningCheckbox_3")
        self.verticalLayout_12.addWidget(self.eveningCheckbox_3)
        self.onlineCheckbox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.onlineCheckbox.setObjectName("onlineCheckbox")
        self.verticalLayout_12.addWidget(self.onlineCheckbox)
        self.horizontalLayout.addLayout(self.verticalLayout_12)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.slCheckbox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.slCheckbox.setObjectName("slCheckbox")
        self.verticalLayout.addWidget(self.slCheckbox)
        self.stabroadCheckbox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.stabroadCheckbox.setObjectName("stabroadCheckbox")
        self.verticalLayout.addWidget(self.stabroadCheckbox)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.searchCol_3.addLayout(self.horizontalLayout)
        self.creditsLabel_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.creditsLabel_3.setObjectName("creditsLabel_3")
        self.searchCol_3.addWidget(self.creditsLabel_3)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.maxCredits_3 = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.maxCredits_3.setObjectName("maxCredits_3")
        self.maxCredits_3.setMinimum(0.0)
        self.horizontalLayout_8.addWidget(self.maxCredits_3)
        self.minCredits_3 = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.minCredits_3.setObjectName("minCredits_3")
        self.minCredits_3.setMinimum(0.0)
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
        self.backButton.setGeometry(QtCore.QRect(970, 0, 101, 31))
        self.backButton.setObjectName("backButton")
        self.picklesButton = QtWidgets.QPushButton(self.searchPage)
        self.picklesButton.setGeometry(QtCore.QRect(10, 0, 111, 31))
        self.picklesButton.setObjectName("picklesButton")
        self.stackedWidget.addWidget(self.searchPage)
        self.schedulePage = QtWidgets.QWidget()
        self.schedulePage.setObjectName("schedulePage")
        self.backButton_2 = QtWidgets.QPushButton(self.schedulePage)
        self.backButton_2.setGeometry(QtCore.QRect(970, 10, 101, 31))
        self.backButton_2.setObjectName("backButton_2")
        self.picklesButton_2 = QtWidgets.QPushButton(self.schedulePage)
        self.picklesButton_2.setGeometry(QtCore.QRect(20, 10, 111, 31))
        self.picklesButton_2.setObjectName("picklesButton_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.schedulePage)
        self.tableWidget_2.setGeometry(QtCore.QRect(180, 70, 891, 741))
        self.tableWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.label_5 = QtWidgets.QLabel(self.schedulePage)
        self.label_5.setGeometry(QtCore.QRect(190, 50, 111, 16))
        self.label_5.setObjectName("label_5")
        self.layoutWidget = QtWidgets.QWidget(self.schedulePage)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 80, 141, 461))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.classesBox = QtWidgets.QTextEdit(self.layoutWidget)
        self.classesBox.setObjectName("classesBox")
        self.verticalLayout_3.addWidget(self.classesBox)
        self.findSchedules = QtWidgets.QPushButton(self.layoutWidget)
        self.findSchedules.setObjectName("findSchedules")
        self.verticalLayout_3.addWidget(self.findSchedules)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.allButt = QtWidgets.QRadioButton(self.layoutWidget)
        self.allButt.setObjectName("allButt")
        self.verticalLayout_2.addWidget(self.allButt)
        self.earliestButt = QtWidgets.QRadioButton(self.layoutWidget)
        self.earliestButt.setObjectName("earliestButt")
        self.verticalLayout_2.addWidget(self.earliestButt)
        self.earliestStartButt = QtWidgets.QRadioButton(self.layoutWidget)
        self.earliestStartButt.setObjectName("earliestStartButt")
        self.verticalLayout_2.addWidget(self.earliestStartButt)
        self.latestButt = QtWidgets.QRadioButton(self.layoutWidget)
        self.latestButt.setObjectName("latestButt")
        self.verticalLayout_2.addWidget(self.latestButt)
        self.latestStartButt = QtWidgets.QRadioButton(self.layoutWidget)
        self.latestStartButt.setObjectName("latestStartButt")
        self.verticalLayout_2.addWidget(self.latestStartButt)
        self.shortestDayButt = QtWidgets.QRadioButton(self.layoutWidget)
        self.shortestDayButt.setObjectName("shortestDayButt")
        self.verticalLayout_2.addWidget(self.shortestDayButt)
        self.gapsButt = QtWidgets.QRadioButton(self.layoutWidget)
        self.gapsButt.setObjectName("gapsButt")
        self.verticalLayout_2.addWidget(self.gapsButt)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
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

        self.monTimeS.setTime(QtCore.QTime(8, 0))
        self.monTimeE.setTime(QtCore.QTime(9, 0))
        self.tueTimeS.setTime(QtCore.QTime(8, 0))
        self.tueTimeE.setTime(QtCore.QTime(9, 0))
        self.wedTimeS.setTime(QtCore.QTime(8, 0))
        self.wedTimeE.setTime(QtCore.QTime(9, 0))
        self.thurTimeS.setTime(QtCore.QTime(8, 0))
        self.thurTimeE.setTime(QtCore.QTime(9, 0))
        self.friTimeS.setTime(QtCore.QTime(8, 0))
        self.friTimeE.setTime(QtCore.QTime(9, 0))
        self.satTimeS.setTime(QtCore.QTime(8, 0))
        self.satTimeE.setTime(QtCore.QTime(9, 0))


        self.retranslateUi(MainWindow)

        # MY CODE
        self.stackedWidget.setCurrentIndex(2)
        self.advancedSearchButton.clicked.connect(self.gotoSearchPage)
        self.scheduleMakerButton.clicked.connect(self.gotoSchedulePage)
        self.backButton.clicked.connect(self.gotoStartPage)
        self.backButton_2.clicked.connect(self.gotoStartPage)
        self.picklesButton.clicked.connect(self.openPicklePage)
        self.picklesButton_2.clicked.connect(self.openPicklePage)
        self.deptLineEdit_3.textChanged.connect(self.updateDeptFilter)
        self.courseNumLineEdit_3.textChanged.connect(self.updateCourseNumFilter)
        self.courseNameLineEdit_3.textChanged.connect(self.updateCourseNameFilter)
        self.instructorLineEdit_3.textChanged.connect(self.updateInstructorFilter)
        self.dayCheckbox_3.clicked.connect(self.updateTypeFilter)
        self.eveningCheckbox_3.clicked.connect(self.updateTypeFilter)
        self.onlineCheckbox.clicked.connect(self.updateTypeFilter)
        self.slCheckbox.clicked.connect(self.updateTypeFilter)
        self.stabroadCheckbox.clicked.connect(self.updateTypeFilter)
        self.maxCredits_3.valueChanged.connect(self.updateCreditsFilterMax)
        self.minCredits_3.valueChanged.connect(self.updateCreditsFilterMin)
        self.level100_3.clicked.connect(self.updateLevelFilter)
        self.level200_3.clicked.connect(self.updateLevelFilter)
        self.level300_3.clicked.connect(self.updateLevelFilter)
        self.level400_3.clicked.connect(self.updateLevelFilter)
        self.level500_3.clicked.connect(self.updateLevelFilter)
        self.level600_3.clicked.connect(self.updateLevelFilter)
        self.level700_3.clicked.connect(self.updateLevelFilter)
        self.monCheck.clicked.connect(self.updateDaysFilter)
        self.tueCheck.clicked.connect(self.updateDaysFilter)
        self.wedCheck.clicked.connect(self.updateDaysFilter)
        self.thurCheck.clicked.connect(self.updateDaysFilter)
        self.friCheck.clicked.connect(self.updateDaysFilter)
        self.satCheck.clicked.connect(self.updateDaysFilter)
        self.tableWidget_2.cellClicked.connect(self.openSingleClassPage)
        self.tableWidget_2.cellClicked.connect(self.click_section_in_schedules)
        self.findSchedules.clicked.connect(self.updateScheduleTable)
        self.allButt.clicked.connect(self.updateScheduleTable)
        self.earliestStartButt.clicked.connect(self.earliest_start)
        self.earliestButt.clicked.connect(self.earliest)
        self.latestStartButt.clicked.connect(self.latest_start)
        self.latestButt.clicked.connect(self.latest)
        self.shortestDayButt.clicked.connect(self.shortestDay)
        self.gapsButt.clicked.connect(self.leastGaps)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.tableWidget.setSortingEnabled(True)
        self.main_window_ref = MainWindow

    def updateDaysFilter(self):
        semesterManager.day_filter['M'][2] = self.monCheck.isChecked()
        semesterManager.day_filter['T'][2] = self.tueCheck.isChecked()
        semesterManager.day_filter['W'][2] = self.wedCheck.isChecked()
        semesterManager.day_filter['Th'][2] = self.thurCheck.isChecked()
        semesterManager.day_filter['F'][2] = self.friCheck.isChecked()
        semesterManager.day_filter['Sa'][2] = self.satCheck.isChecked()

        semesterManager.day_filter['M'][0] = self.monTimeS.time().hour() * 60 + self.monTimeS.time().minute()
        semesterManager.day_filter['M'][1] = self.monTimeE.time().hour() * 60 + self.monTimeE.time().minute()
        semesterManager.day_filter['T'][0] = self.tueTimeS.time().hour() * 60 + self.tueTimeS.time().minute()
        semesterManager.day_filter['T'][1] = self.tueTimeE.time().hour() * 60 + self.tueTimeE.time().minute()
        semesterManager.day_filter['W'][0] = self.wedTimeS.time().hour() * 60 + self.wedTimeS.time().minute()
        semesterManager.day_filter['W'][1] = self.wedTimeE.time().hour() * 60 + self.wedTimeE.time().minute()
        semesterManager.day_filter['Th'][0] = self.thurTimeS.time().hour() * 60 + self.thurTimeS.time().minute()
        semesterManager.day_filter['Th'][1] = self.thurTimeE.time().hour() * 60 + self.thurTimeE.time().minute()
        semesterManager.day_filter['F'][0] = self.friTimeS.time().hour() * 60 + self.friTimeS.time().minute()
        semesterManager.day_filter['F'][1] = self.friTimeE.time().hour() * 60 + self.friTimeE.time().minute()
        semesterManager.day_filter['Sa'][0] = self.satTimeS.time().hour() * 60 + self.satTimeS.time().minute()
        semesterManager.day_filter['Sa'][1] = self.satTimeE.time().hour() * 60 + self.satTimeE.time().minute()

        if semesterManager.selected_semester is not None:
            self.updateTable()

    def updateCreditsFilterMax(self):
        if self.maxCredits_3.value() < self.minCredits_3.value():
            self.minCredits_3.setValue(self.maxCredits_3.value())
        semesterManager.credits_filter[1] = self.maxCredits_3.value()
        if semesterManager.selected_semester is not None:
            self.updateTable()

    def updateCreditsFilterMin(self):
        if self.minCredits_3.value() > self.maxCredits_3.value():
            self.maxCredits_3.setValue(self.minCredits_3.value())
        semesterManager.credits_filter[0] = self.minCredits_3.value()
        if semesterManager.selected_semester is not None:
            self.updateTable()

    def updateTypeFilter(self):
        semesterManager.type_filter['DAY'] = self.dayCheckbox_3.isChecked()
        semesterManager.type_filter['EVENING'] = self.eveningCheckbox_3.isChecked()
        semesterManager.type_filter['ONLINE'] = self.onlineCheckbox.isChecked()
        semesterManager.type_filter['SALT LAKE'] = self.slCheckbox.isChecked()
        semesterManager.type_filter['ST ABROAD'] = self.stabroadCheckbox.isChecked()
        if semesterManager.selected_semester is not None:
            self.updateTable()

    def updateLevelFilter(self):
        semesterManager.course_level_filter[100] = self.level100_3.isChecked()
        semesterManager.course_level_filter[200] = self.level200_3.isChecked()
        semesterManager.course_level_filter[300] = self.level400_3.isChecked()
        semesterManager.course_level_filter[400] = self.level400_3.isChecked()
        semesterManager.course_level_filter[500] = self.level500_3.isChecked()
        semesterManager.course_level_filter[600] = self.level600_3.isChecked()
        semesterManager.course_level_filter[700] = self.level700_3.isChecked()
        if semesterManager.selected_semester is not None:
            self.updateTable()

    def updateDeptFilter(self):
        semesterManager.dept_filter = self.deptLineEdit_3.text().lower()
        if semesterManager.selected_semester is not None:
            self.updateTable()

    def updateCourseNumFilter(self):
        semesterManager.course_num_filter = self.courseNumLineEdit_3.text()
        if semesterManager.selected_semester is not None:
            self.updateTable()

    def updateCourseNameFilter(self):
        semesterManager.course_name_filter = self.courseNameLineEdit_3.text().lower()
        if semesterManager.selected_semester is not None:
            self.updateTable()

    def updateInstructorFilter(self):
        semesterManager.instructor_filter = self.instructorLineEdit_3.text().lower()
        if semesterManager.selected_semester is not None:
            self.updateTable()

    # MY CODE
    def goodScreenX(self, x):
        if x < 0:
            return 0
        if x > self.screenSize.width():
            return self.screenSize.width()
        return x

    # MY CODE
    def goodScreenY(self, y):
        if y < 0:
            return 0
        if y > self.screenSize.height():
            return self.screenSize.height()
        return y

    # MY CODE
    def openPicklePage(self):
        global PickleSelector
        PickleSelector.show()

    def openSingleClassPage(self, row, column):
        global singleClassSelector
        info = semesterManager.get_by_course_section(semesterManager.selected_semester.semester_year, self.tableWidget_2.horizontalHeaderItem(column).text(), int(self.tableWidget_2.item(row, column).text()))
        singleClassUi.setInfo(info[0], info[1], info[2])
        singleClassUi.populateTable(info)
        singleClassSelector.show()

    # MY CODE
    def makeWindowSmall(self):
        self.main_window_ref.resize(380, 170)
        x = self.main_window_ref.x()
        y = self.main_window_ref.y()
        self.main_window_ref.move(self.goodScreenX(x + 310), self.goodScreenY(y + 265))

    # MY CODE
    def makeWindowBig(self):
        self.main_window_ref.resize(1100, 850)
        x = self.main_window_ref.x()
        y = self.main_window_ref.y()
        self.main_window_ref.move(self.goodScreenX(x - 340), self.goodScreenY(y - 290))

    # MY CODE
    def gotoStartPage(self):
        self.makeWindowSmall()
        self.clearTable()
        semesterManager.selected_semester = None
        self.stackedWidget.setCurrentIndex(2)
        self.updateTitleBar()

    # MY CODE
    def gotoSearchPage(self):
        self.makeWindowBig()
        semesterManager.selected_semester = None
        self.stackedWidget.setCurrentIndex(0)
        self.updateTitleBar()

    # MY CODE
    def gotoSchedulePage(self):
        self.makeWindowBig()
        self.clearTable()
        semesterManager.selected_semester = None
        self.stackedWidget.setCurrentIndex(1)
        self.updateTitleBar()

    def updateTitleBar(self):
        if self.stackedWidget.currentIndex() == 0:
            mode = 'Advanced Search'
        elif self.stackedWidget.currentIndex() == 1:
            mode = 'Schedule Maker'
        else:
            self.main_window_ref.setWindowTitle(f'BYU Schdeuling Tool')
            return None
        if semesterManager.selected_semester is None:
            self.main_window_ref.setWindowTitle(f'BYU Schdeuling Tool - {mode} - No Semester Selected')
        else:
            self.main_window_ref.setWindowTitle(f'BYU Scheduling Tool - {mode} - {semesterManager.selected_semester.semester_year}')

    def updateScheduleTable(self):
        class_list = self.classesBox.toPlainText().split('\n')
        try:
            self.schedules = classroom.schedule_tools.get_combinations(class_list)
        except IndexError:
            self.tableWidget_2.setRowCount(0)
            self.tableWidget_2.setColumnCount(0)
            self.classesBox.setText('Could not find a class')
            return None
        self.populateTable2()

    def select_section(self, cell_value, column):
        good_schedule = []
        for i in range(len(self.schedules)):
            if self.tableWidget_2.item(i, column).text() == cell_value:
                good_schedule.append(self.schedules[i])

        self.schedules = good_schedule
        self.populateTable2()

    def populateTable2(self):
        class_list = self.classesBox.toPlainText().split('\n')
        self.tableWidget_2.setColumnCount(len(class_list))
        try:
            self.tableWidget_2.setRowCount(len(self.schedules))
        except TypeError:
            self.classesBox.setText('Select a semester')
            return None
        self.tableWidget_2.setHorizontalHeaderLabels(class_list)
        for i, tab_schedule in enumerate(self.schedules):
            for j in range(len(class_list)):
                try:
                    self.tableWidget_2.setItem(i, j, QtWidgets.QTableWidgetItem(str(self.schedules[i][j].section_num)))
                except IndexError:
                    self.tableWidget_2.setColumnCount(0)
                    self.tableWidget_2.setRowCount(0)
                    self.classesBox.setText(f'Could not find: {class_list[j]}')
                    break

    def earliest_start(self):
        opt_schedules = classroom.schedule_tools.earliest_start(self.schedules)
        self.populateTable2Opt(opt_schedules)

    def earliest(self):
        opt_schedules = classroom.schedule_tools.earliest(self.schedules)
        self.populateTable2Opt(opt_schedules)

    def latest_start(self):
        opt_schedules = classroom.schedule_tools.latest_start(self.schedules)
        self.populateTable2Opt(opt_schedules)

    def latest(self):
        opt_schedules = classroom.schedule_tools.latest(self.schedules)
        self.populateTable2Opt(opt_schedules)

    def shortestDay(self):
        opt_schedules = classroom.schedule_tools.shortest_day(self.schedules)
        self.populateTable2Opt(opt_schedules)

    def leastGaps(self):
        opt_schedules = classroom.schedule_tools.least_gaps(self.schedules)
        self.populateTable2Opt(opt_schedules)

    def populateTable2Opt(self, schedulesIn):
        class_list = self.classesBox.toPlainText().split('\n')
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.setRowCount(len(schedulesIn))
        for i, tab_schedule in enumerate(schedulesIn):
            for j in range(len(class_list)):
                self.tableWidget_2.setItem(i, j, QtWidgets.QTableWidgetItem(str(schedulesIn[i][j].section_num)))

    def click_section_in_schedules(self, row, column):
        self.cell_value = self.tableWidget_2.item(row, column).text()
        self.sched_column = column

    def apply_clicked_section(self):
        self.select_section(self.cell_value, self.sched_column)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(f'BYU Schdeuling Tool')
        self.deptLabel_3.setText(_translate("MainWindow", "Dept."))
        self.courseNumLabel_3.setText(_translate("MainWindow", "Course Num."))
        self.courseNameLabel_3.setText(_translate("MainWindow", "Course Name"))
        self.instructorLabel_3.setText(_translate("MainWindow", "Instructor"))
        self.monCheck.setText(_translate("MainWindow", "Monday (start-end)"))
        self.tueCheck.setText(_translate("MainWindow", "Tuesday (start-end)"))
        self.wedCheck.setText(_translate("MainWindow", "Wednesday (start-end)"))
        self.thurCheck.setText(_translate("MainWindow", "Thursday (start-end)"))
        self.friCheck.setText(_translate("MainWindow", "Friday (start-end)"))
        self.satCheck.setText(_translate("MainWindow", "Saturday (start-end)"))
        self.courseTypeLabel_3.setText(_translate("MainWindow", "Type"))
        self.dayCheckbox_3.setText(_translate("MainWindow", "DAY"))
        self.eveningCheckbox_3.setText(_translate("MainWindow", "EVENING"))
        self.onlineCheckbox.setText(_translate("MainWindow", "ONLINE"))
        self.slCheckbox.setText(_translate("MainWindow", "SALT LAKE"))
        self.stabroadCheckbox.setText(_translate("MainWindow", "ST ABROAD"))
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
        self.tableWidget_2.setSortingEnabled(False)
        self.label_5.setText(_translate("MainWindow", "Possible Schedules:"))
        self.label_2.setText(_translate("MainWindow", "Enter classes here:"))
        self.findSchedules.setText(_translate("MainWindow", "Find Schedules"))
        self.label_4.setText(_translate("MainWindow", "Optimization"))
        self.allButt.setText(_translate("MainWindow", "None"))
        self.earliestButt.setText(_translate("MainWindow", "Earliest"))
        self.earliestStartButt.setText(_translate("MainWindow", "Earliest Start"))
        self.latestButt.setText(_translate("MainWindow", "Latest"))
        self.latestStartButt.setText(_translate("MainWindow", "Latest Start"))
        self.shortestDayButt.setText(_translate("MainWindow", "Shortest Day"))
        self.gapsButt.setText(_translate("MainWindow", "Least Gaps"))
        self.advancedSearchButton.setText(_translate("MainWindow", "Advanced Search"))
        self.scheduleMakerButton.setText(_translate("MainWindow", "Schedule Maker"))
        self.label.setText(_translate("MainWindow", "BYU Class Scheduling & Search Tool\n\nversion - 0.0.0\n\nJosh Bedwell"))

    def updateTable(self):
        self.tableWidget.setSortingEnabled(False)
        self.clearTable()
        self.filteredSemester = semesterManager.get_filtered_semester()
        num_sections = 0
        for course in self.filteredSemester.courses:
            num_sections += len(course.sections)
        self.tableWidget.setRowCount(num_sections)
        section_ct = 0
        for course in self.filteredSemester.courses:
            for section in course.sections:
                times = []
                for i in range(len(section.start)):
                    times.append(section.start[i] + ' - ' + section.end[i])
                data = [QtWidgets.QTableWidgetItem(course.college_short),
                        QtWidgets.QTableWidgetItem(course.short_title),
                        QtWidgets.QTableWidgetItem(),
                        QtWidgets.QTableWidgetItem(course.long_title),
                        QtWidgets.QTableWidgetItem(section.instructor),
                        QtWidgets.QTableWidgetItem('\n'.join(times)),
                        QtWidgets.QTableWidgetItem(section.type),
                        QtWidgets.QTableWidgetItem('\n'.join(section.days)),
                        QtWidgets.QTableWidgetItem(),
                        QtWidgets.QTableWidgetItem(section.location)]
                data[2].setData(QtCore.Qt.EditRole, QtCore.QVariant(section.section_num))
                data[8].setData(QtCore.Qt.EditRole, QtCore.QVariant(section.credits))
                for i in range(len(data)):
                    self.tableWidget.setItem(section_ct, i, data[i])
                section_ct += 1
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.setColumnWidth(3, 200)
        self.tableWidget.setColumnWidth(5, 125)
        self.tableWidget.setSortingEnabled(True)

    def clearTable(self):
        self.tableWidget.setRowCount(0)


# classViewerUi = gui.single_class.Ui_Form()
# classViewerUi.setupUi(ClassViewer)
# ClassViewer.hide()

screenSize = app.primaryScreen().size()
ui = Ui_MainWindow()
ui.setupUi(MainWindow, screenSize)
MainWindow.show()

singleClassUi = gui.single_class.Ui_Form()
singleClassUi.setupUi(singleClassSelector, ui)
singleClassSelector.hide()

pickleUi = gui.pickle_ui.Ui_Form()
pickleUi.setupUi(PickleSelector, ui)
PickleSelector.hide()

sys.exit(app.exec_())
