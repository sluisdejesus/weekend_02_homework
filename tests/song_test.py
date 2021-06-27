import unittest
from classes.song import *

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Go Robot", "Red Hot Chilli Peppers")

    def test_song_has_title(self):
        self.assertEqual("Go Robot", self.song.title)

    def test_song_has_artist(self):
        self.assertEqual("Red Hot Chilli Peppers", self.song.artist)