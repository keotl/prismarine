from jivago.lang.annotations import Serializable


@Serializable
class AlbumResult(object):

    def __init__(self, id: str, name: str, artist: str, year: int, artwork_url: str):
        self.id = id
        self.name = name
        self.artist = artist
        self.year = year
        self.artwork_url = artwork_url
