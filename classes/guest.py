class Guest:
    def __init__(self, name, age, fav_song):
        self.name = name
        self.age = age
        self.guest_list = []
        self.fav_song = fav_song

    
# have not been able to test for this
    def fav_song_playing(self):
        for song in self.room.songlist:
            if song == self.fav_song:
                return "Woooo!"
            else:
             return "Booo!"