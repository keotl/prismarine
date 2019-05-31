from datetime import datetime
from multiprocessing.pool import ThreadPool
from uuid import UUID

import os
from jivago.inject.annotation import Component
from jivago.lang.annotations import Inject

from prismarine.configuration.transcoding_settings import TranscodingSettings
from prismarine.media_info.media_library import MediaLibrary
from prismarine.transcoding.transcoding_job import TranscodingJob
from prismarine.transcoding.transcoding_job_repository import TranscodingJobRepository


@Component
class TranscodingService(object):

    @Inject
    def __init__(self, transcoding_job_repository: TranscodingJobRepository, transcoding_settings: TranscodingSettings,
                 media_library: MediaLibrary):
        self.media_library = media_library
        self.transcoding_job_repository = transcoding_job_repository
        self.output_folder = transcoding_settings.transcoded_media_folder
        self.executors = ThreadPool(processes=transcoding_settings.transcoding_executors)

    def enqueue_transcode(self, track_id: UUID) -> TranscodingJob:
        track = self.media_library.get_track(track_id)
        job = TranscodingJob(datetime.now(), track_id, track.filename, os.path.join(self.output_folder, str(track_id)))

        self.transcoding_job_repository.add(job)
        return job
