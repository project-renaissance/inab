from django.views import View
from django.http import JsonResponse

class Student:
	def get(self):
		data = [
			{ 'name': "sdfsdfsdf", "age": 123 },
			{ 'name': "ytuytuytu",  "age": 43 }
		]
		return data

class Teacher:
	def get(self):
		data = [
			{ 'name': "qwwqeqwe", "age": 54 },
			{ 'name': "nbvbvbvbnvbn", "age": 7989 }
		]
		return data

class Response(View):
	def get(self, request, parameters):
		paramList = parameters.split('/')
		data = {}
		for i in paramList:
			class_instance = globals()[i]()
			data[i] = class_instance.get()
		return JsonResponse(data)
