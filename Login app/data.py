class Save_data:

	def check(gmail):
		with open('information.txt', 'r+') as myFile:
			# checek if the user puts the same files :D
			word_list = myFile.read() 
			if gmail in word_list: # checks if the user used this gmail
				return True

	def save(data_to_save):
		with open('information.txt', 'a+') as myFile:
			myFile.write(data_to_save)

	def log(gmail, passw):
		data_user = f'{gmail} {passw}'
		with open('information.txt', 'r+') as myFile:
			data_list = myFile.readlines()
			for data in data_list:
				if data[:-1].endswith(data_user):
					return True

				elif data.endswith(data_user):
					return True
				return False