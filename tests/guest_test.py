import unittest
from classes.guest import *

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Freddy Mercury",34)

    def test_guest_has_name(self):
        self.assertEqual("Freddy Mercury",self.guest.name)

    def test_guest_has_age(self):
        self.assertEqual(34, self.guest.age)

    def test_can_add_guest(self):
        self.guest.add_guest(self.guest.name)
        self.assertEqual(1, self.guest.guest_list_length())