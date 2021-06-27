from classes.room import *

class Guest:
    def __init__(self, name, age, fav_song, wallet):
        self.name = name
        self.age = age
        self.fav_song = fav_song
        self.wallet = wallet

    
# have not been able to test for this
    def fav_song_playing(self):
        for song in self.room.songlist:
            if song == self.fav_song:
                print("Woooo!")
            else:
                print("Booo!")