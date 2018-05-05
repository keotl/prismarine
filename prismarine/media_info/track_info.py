from prismarine.media_info.media_info import MediaInfo


class TrackInfo(MediaInfo):

    def __init__(self, id: str, title: str, artist: str, album: str, length: float, format: str, genre: str,
                 track_number: int, total_tracks: int, filename: str):
        self.filename = filename
        self.album = album
        self.genre = genre
        self.track_number = track_number
        self.total_tracks = total_tracks
        self.title = title
        self.artist = artist
        self.length = length
        self.format = format
        super().__init__(id)
