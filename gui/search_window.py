from PyQt5 import QtWidgets
from PyQt5 import QtGui
import os
import sys


class SearchWindow(QtWidgets.QMainWindow):

	def __init__(self, parent, screen_dim):
		super(SearchWindow, self).__init__(parent)

		self.assets = os.path.join(os.path.dirname(sys.argv[0]), 'assets')
		self.size1 = screen_dim

		self.initUI()

	def initUI(self):
		self.window_width = 1000
		self.window_height = 700
		self.center_w = self.size1.width() / 2 - self.window_width / 2
		self.center_h = self.size1.height() / 2 - self.window_height / 2

		self.setGeometry(self.center_w, self.center_h, self.window_width, self.window_height)

		self.setWindowTitle('BYU Schdeuling Tool - Advanced Search')
		self.setWindowIcon(QtGui.QIcon(os.path.join(self.assets, 'byu-icon.png')))

		self.show()


class SearchWindow0:

	def __init__(self, size_in):

		# app = QtWidgets.QApplication(sys.argv)
		window = SearchWindow(size_in)
		# app.exec_()
