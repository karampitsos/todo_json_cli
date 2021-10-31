import json
import os
from auth import *
from users import *

def main(user):
	os.system('clear')
	user.show_tasks()
	print(' ')
	print('list of commands: load,save,add,clear,remove,update,sort')
	
	command = input('command: ')
	
	if command == 'add':
		name = input('name: ')
		start = input('start: ')
		stop = input('stop: ')
		user.add({'name': name, 'start': start  , 'stop': stop})
	
	elif command =='save':
		user.save()
	
	elif command =='load':
		user.load()
	
	elif command == 'clear':
		user.clear()
	
	elif command == 'sort':
		k = input('by: ')
		user.sort_by(k)
	
	elif command == 'update':
		task_id = int(input('id: '))
		name = input('name: ')
		start = input('start: ')
		stop = input('stop: ')
		user.update(task_id,name,start,stop)
	
	elif command == 'remove':
		task_id = int(input('id: '))
		user.remove(task_id)
	
	elif command =='log out':
		username, password = auth()
		new_user = User(username, password)
		main(new_user)
	
	else:
		print('command does not exists')

	main(user)

if __name__ == '__main__':
	username, password = auth()
	user = User(username, password )
	main(user)