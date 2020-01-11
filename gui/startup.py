from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from gui.search_window import SearchWindow
import os
import sys


class Window(QtWidgets.QMainWindow):

	def __init__(self, screen_dim):
		super().__init__()

		self.assets = os.path.join(os.path.dirname(sys.argv[0]), 'assets')
		self.size1 = screen_dim

		self.initUI()

	def initUI(self):
		self.window_width = 600
		self.window_height = 350

		self.center_w = self.size1.width() / 2 - self.window_width / 2
		self.center_h = self.size1.height() / 2 - self.window_height / 2

		self.search_btn = QtWidgets.QPushButton('Advanced Search', self)
		self.schedule_btn = QtWidgets.QPushButton('Schedule Maker', self)
		self.search_btn.resize(200, 100)
		self.schedule_btn.resize(200, 100)
		self.search_btn.move(80, 125)
		self.schedule_btn.move(320, 125)

		self.search_btn.clicked.connect(self.buttonClicked)
		self.schedule_btn.clicked.connect(self.buttonClicked)

		self.setGeometry(self.center_w, self.center_h, self.window_width, self.window_height)

		self.statusBar()

		self.setWindowTitle('BYU Schdeuling Tool')
		self.setWindowIcon(QtGui.QIcon(os.path.join(self.assets, 'byu-icon.png')))

		self.show()

	def buttonClicked(self):

		sender = self.sender()
		self.statusBar().showMessage(sender.text() + ' was pressed')
		if sender.text() == 'Advanced Search':
			SearchWindow(self, self.size1)


class StartupWindow:

	def __init__(self):

		self.app = QtWidgets.QApplication(sys.argv)
		self.window = Window(self.app.primaryScreen().size())
		self.app.exec_()
