import os
import json

class User:
	def __init__(self, name, password):
		self.name = name
		self.password = password
		self.task_list = []

	def add(self, task):
		self.task_list.append(task)

	def remove(self, task_id):
		self.task_list.pop(task_id)

	def clear(self):
		self.task_list = []

	def update(self, task_id, name, start, stop):
		self.task_list[task_id]['name'] = name
		self.task_list[task_id]['start'] = start
		self.task_list[task_id]['stop'] = stop

	def sort_by(self, key):
		if key == 'start':
			self.task_list.sort(key = lambda task: task['start'] )
		elif key == 'stop':
			self.task_list.sort(key = lambda task: task['stop'] )
		elif key == 'name':
			self.task_list.sort(key = lambda task: task['name'] )
		else:
			pass

	def show_tasks(self):
		print('          TASKS')
		print('# # # # # # # # # # # # # ')
		print('NAME   START   STOP')
		print('# # # # # # # # # # # # # ')
		for task in self.task_list:
			print(task['name']+' '+task['start']+' - '+task['stop'])
		print('# # # # # # # # # # # # # ')
		
	def load(self):
		if os.path.isfile('./{name}.json'.format(name = self.name)):
			file = open('{name}.json'.format(name = self.name),'r')
			self.task_list = json.loads(file.read())
			file.close()
		else:
			pass

	def save(self):
		file = open('{name}.json'.format(name = self.name),'w') 
		file.write(json.dumps(self.task_list))
		file.close()