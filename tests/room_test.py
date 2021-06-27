import unittest
from classes.room import *
class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Happy Lounge", 20)

    def test_room_has_name(self):
        self.assertEqual("Happy Lounge", self.room.name)

    def test_room_has_capacity(self):
        self.assertEqual(20, self.room.capacity)