from jivago.lang.annotations import Serializable


@Serializable
class TrackModel(object):

    def __init__(self, id: str, title: str, album_id: str, genre: str, artist: str, length: str, track_number: int,
                 disc_number: int, artwork_url: str, album: str):
        self.id = id
        self.title = title
        self.album_id = album_id
        self.genre = genre
        self.artist = artist
        self.length = length
        self.track_number = track_number
        self.disc_number = disc_number
        self.artwork_url = artwork_url
        self.album = album
