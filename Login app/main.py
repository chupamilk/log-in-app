import PyQt5.QtWidgets as qwd
from PyQt5.QtGui import QIcon
from data import Save_data

class MainWindow(qwd.QWidget):
	def __init__(self):
		super().__init__()
		# set window settings
		self.setWindowTitle('sign-in')
		self.setStyleSheet('Background: #202020')
		self.setWindowIcon(QIcon('sign-in.png'))
		self.setFixedWidth(645)
		self.setFixedHeight(480)

		self.UIcomponents()

		self.show()

	def UIcomponents(self):
		# sing-in log-in stuff
		# write password: and username:
		self.label_username = qwd.QLabel('username:', self)
		self.label_username.setStyleSheet("color:white; font-size:13px;");
		self.label_username.move(250, 180)
		self.label_password = qwd.QLabel('password:', self)
		self.label_password.setStyleSheet("color:white; font-size:13px;");
		self.label_password.move(250, 280)
		self.label_gmail = qwd.QLabel('gmail:', self)
		self.label_gmail.setStyleSheet("color:white; font-size:13px;");
		self.label_gmail.move(250, 230)

		self.username = qwd.QLineEdit(self)
		self.username.setStyleSheet('background: #f2f2f2')
		self.username.move(250, 200)

		self.gmail = qwd.QLineEdit(self)
		self.gmail.setStyleSheet('background: #f2f2f2')
		self.gmail.move(250, 250)

		self.password = qwd.QLineEdit(self)
		self.password.setStyleSheet('background: #f2f2f2')
		self.password.move(250, 300)

		self.but_ok = qwd.QPushButton('ok', self)
		self.but_ok.setStyleSheet('background: #f2f2f2')
		self.but_ok.move(280, 400)

		# log-in button
		self.log_but = qwd.QPushButton('log-in', self)
		self.log_but.setStyleSheet('background: #f2f2f2')
		self.log_but.move(370, 400)

		# error if the used this name 
		self.error_box = qwd.QErrorMessage()
		self.error_box.setStyleSheet("Background: #F0F8FF")
		self.error_box.setWindowIcon(QIcon('cancel.png'))
		# connect things
		self.but_ok.clicked.connect(self.save)
		self.log_but.clicked.connect(self.open_wid2)

	def save(self):
		username_to_save = self.username.text()
		password_to_save = self.password.text()
		gmail_to_save = self.gmail.text()
		data_to_save = f'{username_to_save} [{gmail_to_save} {password_to_save}] \n' 

		if Save_data.check(gmail_to_save) != True:
			if len(username_to_save) > 5 and len(password_to_save) > 5:
				Save_data.save(data_to_save)
				self.error_box.showMessage('Your account was created! Please log-in.')
			else:
				self.error_box.showMessage('Put at least 5 characters')

		elif Save_data.check(gmail_to_save) == True: # show user a message
			self.error_box.showMessage('You put nothing or you already used that.\n'
				' You have to put at least 5 characters.')

	def open_wid2(self):
		self.close()
		self.secondwid = SecondWindow()

class SecondWindow(qwd.QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('log-in')
		self.setStyleSheet('Background: #202020')
		self.setWindowIcon(QIcon('sign-in.png'))
		self.setFixedWidth(645)
		self.setFixedHeight(480)

		self.UIcomponents()

		self.show()

	def UIcomponents(self):

		self.label_gmail = qwd.QLabel('gmail:', self)
		self.label_gmail.setStyleSheet("color:white; font-size:13px;");
		self.label_gmail.move(250, 180)
		self.label_password = qwd.QLabel('password:', self)
		self.label_password.setStyleSheet("color:white; font-size:13px;");
		self.label_password.move(250, 230)

		self.gmail = qwd.QLineEdit(self)
		self.gmail.setStyleSheet('background: #f2f2f2')
		self.gmail.move(250, 200)

		self.password = qwd.QLineEdit(self)
		self.password.setStyleSheet('background: #f2f2f2')
		self.password.move(250, 250)

		self.but_ok = qwd.QPushButton('ok', self)
		self.but_ok.setStyleSheet('background: #f2f2f2')
		self.but_ok.move(280, 400)

		# open wid 2
		self.sign_but = qwd.QPushButton('sign-in', self)
		self.sign_but.setStyleSheet('background: #f2f2f2')
		self.sign_but.move(370, 400)

		# 
		self.welcome_box = qwd.QErrorMessage()
		self.welcome_box.setStyleSheet("Background: #F0F8FF")
		self.welcome_box.setWindowIcon(QIcon('cancel.png'))

		self.sign_but.clicked.connect(self.open_main)
		self.but_ok.clicked.connect(self.check_data)

	def check_data(self):	
		self.gmail_to_check = self.gmail.text()
		self.password_to_check = self.password.text()
		self.data_to_check = f'[{self.gmail_to_check} {self.password_to_check}]'

		if Save_data.log(self.data_to_check): # checks if the user has an account
			self.welcome_box.showMessage('WELCOME!')
		else:
			self.welcome_box.showMessage("U don't have an account!")

	def open_main(self):
		self.close()
		self.mainwid = MainWindow()

def window():
	app = qwd.QApplication([])
	app.setStyle('Fusion')
	mainwid = MainWindow()

	app.exec_()

window()
