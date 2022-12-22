import logging
import traceback
from jivago.lang.annotations import Override, Inject
from jivago.lang.runnable import Runnable
from jivago.scheduling.annotations import Scheduled, Duration

from prismarine.filesystem.media.track_transcoder import TrackTranscoder


@Scheduled(every=Duration.HOUR)
class TemporaryTranscodedMediaCleaner(Runnable):

    @Inject
    def __init__(self, track_transcoder: TrackTranscoder):
        self._track_transcoder = track_transcoder
        self._logger = logging.getLogger(self.__class__.__name__)

    @Override
    def run(self):
        try:
            self._track_transcoder.cleanup()
        except Exception as e:
            traceback.print_exc()
            self._logger.error(e)
