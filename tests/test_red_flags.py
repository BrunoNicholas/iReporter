# test_red_flags.py

from app import app
import unittest
import json

class RedFlagTestCase(unittest.TestCase):
	def setup(self):
		self.app = create_app(config_name="testing_flags")

	def tearDown(self):
		pass

	def test_route_indices(self):
		pass

if __name__ == '__main__':
    unittest.main()
	