from flask import jsonify, request,
import json
from .models.user import User

def UserController:
	def __init__(self):
		self.data = request.json

	def index(self):
		''' this function returns all users '''
		pass

	def create(self):
		''' this function returns entry to store a user '''
		pass

	def store(self):
		''' this function stores a new user '''
		pass

	def show(self, id):
		''' this function returns the details of a specific user '''
		pass

	def edit(self, id):
		''' this function returns entry to edit a user's details '''
		pass

	def update(self, id):
		''' this function stores an update of a user's details '''
		pass

	def destroy(self, id):
		''' this function reads a user's details and deletes them '''
		pass