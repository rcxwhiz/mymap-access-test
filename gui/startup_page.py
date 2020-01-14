# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'startup_page.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import os
import sys
import gui.search_page

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # MY ICON CHANGE
        self.assets = os.path.join(os.path.dirname(sys.argv[0]), 'assets')
        MainWindow.setWindowIcon(QtGui.QIcon(os.path.join(self.assets, 'byu-icon.png')))

        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(350, 175)
        MainWindow.setStyleSheet("")
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.advancedSearchButton = QtWidgets.QPushButton(self.centralwidget)
        self.advancedSearchButton.setGeometry(QtCore.QRect(50, 60, 120, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.advancedSearchButton.sizePolicy().hasHeightForWidth())
        self.advancedSearchButton.setSizePolicy(sizePolicy)
        self.advancedSearchButton.setMinimumSize(QtCore.QSize(120, 50))
        self.advancedSearchButton.setMaximumSize(QtCore.QSize(150, 50))
        self.advancedSearchButton.setObjectName("advancedSearchButton")
        self.scheduleMakerButton = QtWidgets.QPushButton(self.centralwidget)
        self.scheduleMakerButton.setGeometry(QtCore.QRect(181, 60, 120, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scheduleMakerButton.sizePolicy().hasHeightForWidth())
        self.scheduleMakerButton.setSizePolicy(sizePolicy)
        self.scheduleMakerButton.setMinimumSize(QtCore.QSize(120, 50))
        self.scheduleMakerButton.setMaximumSize(QtCore.QSize(150, 50))
        self.scheduleMakerButton.setObjectName("scheduleMakerButton")
        MainWindow.setCentralWidget(self.centralwidget)

        # MY BUTTON CONNECTING
        self.scheduleMakerButton.clicked.connect(self.schedulingButtonAction)
        self.advancedSearchButton.clicked.connect(self.advancedSearchButtonAction)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BYU Class Scheduler"))
        self.advancedSearchButton.setText(_translate("MainWindow", "Advanced Search"))
        self.scheduleMakerButton.setText(_translate("MainWindow", "Schedule Maker"))

    def advancedSearchButtonAction(self):
        print('the search button')
        self = gui.search_page.Ui_MainWindow()

    def schedulingButtonAction(self):
        print('the schedule button')


def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
