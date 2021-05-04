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
			myFile.write('\n')

	def log(info):
		print(info)
		with open('information.txt', 'r+') as myFile:
			data_list = myFile.read().splitlines()
			for data in data_list:
				if info in data:
					return True
