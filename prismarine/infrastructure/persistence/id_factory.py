from typing import List
from jivago.inject.annotation import Component


@Component
class IdFactory(object):

    def create_album_id(self, artist: str, title: str):
        return self._join_elements([artist, title])

    def create_track_id(self, artist: str, album: str, title: str):
        return self._join_elements([artist, album, title])

    def create_artist_id(self, artist: str):
        return self._join_elements([artist])

    def _join_elements(self, elements: List[str]):
        return "_".join(map(_sanitize, elements))

def _sanitize(x: str):
    return ''.join(e for e in x if e.isalnum())
