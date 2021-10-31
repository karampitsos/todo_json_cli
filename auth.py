import os
import json

def auth():
	os.system('clear')
	print('list of commands: log in, sign up')
	command = input('command: ')
	if command == 'log in':
		username, password = log_in()
	elif command == 'sign up':
		username, password = sign_up()
	else:
		print('non known command')
		auth()
	return username, password

def log_in():
	username = input('username: ')
	file = open('list_of_users.json', 'r')
	users_data = json.loads(file.read())
	user_data = list(filter(lambda user_data: (user_data['username'] == username), users_data))
	if len(user_data)==0:
		print('wrong username')
		password = ""
		log_in()
	else:
		password = input('password: ')
		if user_data[0]['password'] == password:
			print('you are connected')
			file.close()
		else:
			print('wrong password')
			file.close()
			log_in()
	
	return username, password

def sign_up():
	username = input('username: ')
	password = input('password: ')
	file = open('list_of_users.json', 'r')
	users_data = json.loads(file.read())
	user_data = list(filter(lambda user_data: (user_data['username']== username), users_data))
	file.close()

	if len(user_data) >= 1:
		print('The name is already used')
		sign_up()
	users_data.append({'username':username, 'password':password})
	file = open('list_of_users.json', 'w')
	file.write(json.dumps(users_data))
	file.close()

	return username, password