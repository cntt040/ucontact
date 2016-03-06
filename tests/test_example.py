import unittest
from preggy import expect


class TestExample(unittest.TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_just_run_an_example(self):
		expect(True).to_equal(True)