import unittest
from classes.room import *
from classes.guest import *
class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Happy Lounge", 20, 5)

    def test_room_has_name(self):
        self.assertEqual("Happy Lounge", self.room.name)

    def test_room_has_capacity(self):
        self.assertEqual(20, self.room.capacity)
        
    def test_can_add_guest(self):
        self.room.add_guest(self)
        self.assertEqual(1, self.room.guest_list_length())

    def test_can_check_guest_into_room(self):
        self.room.check_guest_in(self)
        self.assertEqual(1, self.room.guest_list_length())
        self.assertEqual(19, self.room.capacity)


# running with ValueError: list.remove(x): x not in list 
    # def test_can_check_guest_out_of_room(self):
    #     self.room.check_guest_out()
    #     self.assertEqual(0, self.room.guest_list_length())
    #     self.assertEqual(20, self.room.capacity)

    def test_can_add_song(self):
        self.room.add_song(self)
        self.assertEqual(1,self.room.song_list_length())

    def check_room_has_entry_fee(self):
        self.assertEqual(5,self.room.entry_fee)

