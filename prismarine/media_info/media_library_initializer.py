from jivago.lang.annotations import BackgroundWorker, Inject, Override
from jivago.lang.runnable import Runnable

from prismarine.filesystem.media_indexer import MediaIndexer


@BackgroundWorker
class MediaLibraryInitializer(Runnable):

    @Inject
    def __init__(self, media_indexer: MediaIndexer):
        self.media_indexer = media_indexer

    @Override
    def run(self):
        self.media_indexer.index_tracks("/home/atreides/Music")
        print("done initializing media library")
