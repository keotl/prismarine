from jivago.lang.annotations import BackgroundWorker, Inject

from prismarine.filesystem.media_indexer import MediaIndexer


@BackgroundWorker
class MediaLibraryInitializer(object):

    @Inject
    def __init__(self, media_indexer: MediaIndexer):
        self.media_indexer = media_indexer

    def __call__(self):
        self.media_indexer.index_tracks("/home/atreides/Music")
        print("done initializing media library")
