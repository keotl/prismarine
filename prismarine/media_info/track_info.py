from uuid import UUID

from prismarine.media_info.media_info import MediaInfo


class TrackInfo(MediaInfo):

    def __init__(self, id: str, title: str, artist: str, album: str, length: float, format: str, genre: str,
                 track_number: int, total_tracks: int, filename: str, disc_number: int, release_year: int):
        self.filename = filename
        self.album = album
        self.genre = genre
        self.track_number = track_number
        self.total_tracks = total_tracks
        self.title = title
        self.artist = artist
        self.length = length
        self.format = format
        self.disc_number = disc_number
        self.release_year = release_year
        self.album_id = None
        self.artist_id = None
        super().__init__(id)

    def set_album_id(self, album_id: UUID):
        self.album_id = album_id

    def set_artist_id(self, artist_id: UUID):
        self.artist_id = artist_id
