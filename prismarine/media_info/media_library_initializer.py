import logging

from jivago.config.properties.application_properties import ApplicationProperties
from jivago.config.properties.system_environment_properties import SystemEnvironmentProperties
from jivago.config.startup_hooks import Init
from jivago.lang.annotations import Inject, Override
from jivago.lang.runnable import Runnable
from jivago.scheduling.annotations import Scheduled, Duration

from prismarine.filesystem.media_indexer import MediaIndexer


@Init
@Scheduled(every=Duration.HOUR)
class MediaLibraryInitializer(Runnable):
    LOGGER = logging.getLogger("MediaLibraryInitializer")

    @Inject
    def __init__(self, media_indexer: MediaIndexer, application_properties: ApplicationProperties, env: SystemEnvironmentProperties):
        self.application_properties = application_properties
        self.media_indexer = media_indexer
        self.env = env

    @Override
    def run(self):
        self.LOGGER.info("initializing media library...")
        self.media_indexer.index_tracks(self.env.get("media_library") or self.application_properties["media_library"])
        self.LOGGER.info("Indexed tracks.")

        self.LOGGER.info("done initializing media library")
