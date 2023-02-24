class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self,new_album):
        for al in self.albums:
            if al.name == new_album.name:
                return f"Band {self.name} already has {new_album.name} in their library."

        self.albums.append(new_album)
        return f"Band {self.name} has added their newest album {new_album.name}."


    def remove_album(self, album_name):
        for al in self.albums:
            if al.name == album_name:
                if al.published:
                    return f"Album has been published. It cannot be removed."
                else:
                    self.albums.remove(al)
                    return f"Album {album_name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        result = f'Band {self.name}'

        for al in self.albums:
            result += '\n'
            result += al.details()
        return result