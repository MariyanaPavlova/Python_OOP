from project_2_spoopify.song import Song
from project_2_spoopify.band import Band

class Album:

    def __init__(self, name, *args):
        self.name = name
        self.songs = list(args)
        self.published = False

    def add_song(self, new_song):
        if new_song.single:
            return f"Cannot add {new_song.name}. It's a single"
        if self.published:
            return "Cannot add songs. Album is published."
        if new_song in self.songs:
            return "Song is already in the album."

        self.songs.append(new_song)
        return f'Song {new_song.name} has been added to the album {self.name}.'

    def remove_song(self, song_name):
        if self.published:
            return "Cannot remove songs. Album is published."

        for s in self.songs:
            if s.name == song_name:
                self.songs.remove(s)
                return f"Removed song {song_name} from album {self.name}."
        return "Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = f'Album {self.name}'

        for s in self.songs:
            result += '\n'
            result += f'== {s.get_info()}'
        return result + "\n"


song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())



