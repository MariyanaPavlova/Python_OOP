from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE)
        return cls(pages)

    def __init__(self, pages):
        self.pages = pages
        self.photos = self.__in_photos(pages)

    def __in_photos(self, pages):
        result = []
        for x in range(pages):
            result.append([])
        return result

    def add_photo(self, label):
        for i, p in enumerate(self.photos):
            if len(p) < PhotoAlbum.PHOTOS_PER_PAGE:
                p.append(label)
                return f'{label} photo added successfully on page {i+1} slot {len(p)}'
        return "No more free slots"

    def display(self):
        separator = "-" * 11
        result = separator + '\n'
        for page in self.photos:
            # ['first game', 'second game']
            # ['[]', '[]']
            # [] []
            result += " ".join("[]" for _ in page) + "\n"
            result += separator + "\n"
        return result.strip()

album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())


