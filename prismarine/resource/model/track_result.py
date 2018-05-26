from jivago.lang.annotations import Serializable


@Serializable
class TrackModel(object):

    def __init__(self, id: str, title: str, album: str, genre: str, artist: str, length: str, track_number: int):
        self.id = id
        self.title = title
        self.album = album
        self.genre = genre
        self.artist = artist
        self.length = length
        self.track_number = track_number
