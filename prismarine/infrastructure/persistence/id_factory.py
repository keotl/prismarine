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
    x = x.replace("œ", "oe") \
        .replace("é", "e") \
        .replace("è", "e") \
        .replace("ê", "e") \
        .replace("à", "a") \
        .replace("û", "u") \
        .replace("ù", "u") \
        .replace("ô", "o")

    return ''.join(e for e in x if
                   (ord("A") <= ord(e) <= ord("Z") or
                    ord("a") <= ord(e) <= ord("z") or
                    ord("0") <= ord(e) <= ord("9"))
                   )
