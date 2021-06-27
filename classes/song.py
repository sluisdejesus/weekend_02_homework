class Song:
    def __init__(self, title):
        self.title = title
        self.song_list = []

    def add_song(self, title):
        self.song_list.append(title)

    def song_list_length(self):
        return len(self.song_list)
