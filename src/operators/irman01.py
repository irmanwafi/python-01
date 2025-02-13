class Playlist:
    def __init__(self, name, songs):
        self.name = name
        self.songs = songs

    def __len__(self):  # Defines length based on number of songs
        return len(self.songs)

my_playlist = Playlist("Rock", ["Song1", "Song2", "Song3"])
print(len(my_playlist))  # Output: 3
