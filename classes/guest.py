class Guest:
    def __init__(self, name, age, fav_song):
        self.name = name
        self.age = age
        self.guest_list = []
        self.fav_song = fav_song

    def guest_list_length(self):
        return len(self.guest_list)
    
    def add_guest(self, guest):
        self.guest_list.append(guest)