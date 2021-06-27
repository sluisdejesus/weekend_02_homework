class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.songlist = []
        self.guest_list =[]

    def guest_list_length(self):
        return len(self.guest_list)

    def add_guest(self, guest):
        self.guest_list.append(guest)
    
    def check_guest_in(self, guest):
        self.capacity -= 1
        self.guest_list.append(self)

    def check_guest_out(self, guest):
        self.capacity += 1
        self.guest_list.pop(self)

    def add_song(self, song):
        self.songlist.append(song)

    def song_list_length(self):
        return len(self.songlist)

