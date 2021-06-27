import unittest
from classes.song import *

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Go Robot")

    def test_song_has_title(self):
        self.assertEqual("Go Robot", self.song.title)

    def test_can_add_song(self):
        self.song.add_song(self.song.title)
        self.assertEqual(1, self.song.song_list_length())