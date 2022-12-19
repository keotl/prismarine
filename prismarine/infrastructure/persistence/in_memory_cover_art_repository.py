from jivago.inject.annotation import Singleton
from jivago.lang.annotations import Inject, Override

from prismarine.filesystem.media.cover_art_repository import CoverArtRepository
from prismarine.filesystem.media.no_such_artwork_exception import NoSuchArtworkException
from prismarine.filesystem.tags.artwork import Artwork


@Singleton
class InMemoryCoverArtRepository(CoverArtRepository):

    @Inject
    def __init__(self):
        self.content = {}

    @Override
    def get_artwork(self, album_id: str) -> Artwork:
        if self.has_artwork_for(album_id):
            return self.content[album_id]
        raise NoSuchArtworkException()

    @Override
    def save(self, album_id: str, image: Artwork):
        self.content[album_id] = image

    @Override
    def has_artwork_for(self, album_id: str) -> bool:
        return album_id in self.content
