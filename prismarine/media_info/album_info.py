from prismarine.media_info.media_info import MediaInfo
from prismarine.media_info.track_info import TrackInfo


class AlbumInfo(MediaInfo):

    def __init__(self, id, name: str, artist: str, folder_path: str, track_count: int, release_year: int, genre: str):
        self.release_year = release_year
        self.track_count = track_count
        self.folder_path = folder_path
        self.name = name
        self.artist = artist
        self.tracks = []
        self.genre = genre
        super().__init__(id)

    def should_contain(self, track: TrackInfo) -> bool:
        return self.folder_path in track.filename and self.name.lower() == track.album.lower()

    def add_track(self, track: TrackInfo):
        self.tracks.append(track)
