import unittest
from classes.guest import *

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Freddy Mercury",34, "Go Robot")

    def test_guest_has_name(self):
        self.assertEqual("Freddy Mercury",self.guest.name)

    def test_guest_has_age(self):
        self.assertEqual(34, self.guest.age)

    def test_guest_has_fav_song(self):
        self.assertEqual("Go Robot",self.guest.fav_song)

    


