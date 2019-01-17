# test_views.py

from app import app
import unittest
import json

class ViewTestCase(unittest.TestCase):
	def setup(self):
		self.users = []
		self.interventions = []
		self.red_flags = []

	def tearDown(self):
		pass

	def test_route_indices(self):
		pass

if __name__ == '__main__':
    unittest.main()
	