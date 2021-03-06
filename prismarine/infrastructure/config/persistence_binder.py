from jivago.config.abstract_binder import AbstractBinder
from jivago.inject.service_locator import ServiceLocator
from jivago.lang.annotations import Override

from prismarine.filesystem.media.cover_art_repository import CoverArtRepository
from prismarine.infrastructure.persistence.in_memory_cover_art_repository import InMemoryCoverArtRepository
from prismarine.infrastructure.persistence.in_memory_media_library import InMemoryMediaLibrary
from prismarine.media_info.media_library import MediaLibrary


class PersistenceBinder(AbstractBinder):

    @Override
    def bind(self, service_locator: ServiceLocator):
        service_locator.bind(MediaLibrary, InMemoryMediaLibrary)
        service_locator.bind(CoverArtRepository, InMemoryCoverArtRepository)
