# test_users.py

from app import app
import unittest
import json

class UserTestCase(unittest.TestCase):
	def setup(self):
		self.app = create_app(config_name="testing_users")

	def tearDown(self):
		pass

	def test_route_indices(self):
		pass

if __name__ == '__main__':
    unittest.main()
	