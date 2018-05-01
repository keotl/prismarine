import glob

import os
from jivago.inject.registry import Component
from jivago.lang.stream import Stream

from prismarine.media_info.media_repository import MediaRepository


@Component
class MediaIndexer(object):

    def __init__(self, media_repository: MediaRepository):
        self.media_repository = media_repository

    def index_tracks(self, folder_path: str):
        files = Stream(glob.glob(os.path.join(folder_path, '**/*'), recursive=True)).filter(
            lambda path: os.path.isfile(path)).toList()


