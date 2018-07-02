from jivago.config.properties.application_properties import ApplicationProperties
from jivago.config.startup_hooks import Init
from jivago.lang.annotations import Inject, Override
from jivago.lang.runnable import Runnable
from jivago.scheduling.annotations import Scheduled, Duration

from prismarine.filesystem.media_indexer import MediaIndexer


@Init
@Scheduled(every=Duration.HOUR)
class MediaLibraryInitializer(Runnable):

    @Inject
    def __init__(self, media_indexer: MediaIndexer, application_properties: ApplicationProperties):
        self.application_properties = application_properties
        self.media_indexer = media_indexer

    @Override
    def run(self):
        print("initializing media library...")
        self.media_indexer.index_tracks(self.application_properties["media_library"])
        print("Indexed tracks.")

        print("done initializing media library")
