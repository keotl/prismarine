from typing import Optional

from prismarine.media_info.media_info import MediaInfo


class TrackInfo(MediaInfo):

    def __init__(self, id: str, title: str, artist: str, length: str, format: str, genre: str, number: int,
                 tracks_on_disc: Optional[int]):
        self.genre = genre
        self.number = number
        self.tracks_on_disc = tracks_on_disc
        self.title = title
        self.artist = artist
        self.length = length
        self.format = format
        super().__init__(id)
