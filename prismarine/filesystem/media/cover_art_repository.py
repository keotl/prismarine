from prismarine.filesystem.tags.artwork import Artwork


class CoverArtRepository(object):

    def get_artwork(self, album_id: str) -> Artwork:
        raise NotImplementedError

    def save(self, album_id: str, image: Artwork):
        raise NotImplementedError

    def has_artwork_for(self, album_id: str) -> bool:
        raise NotImplementedError
