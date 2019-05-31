import threading
from typing import List

from jivago.inject.annotation import Component, Singleton
from jivago.lang.nullable import Nullable
from jivago.lang.stream import Stream

from prismarine.transcoding.transcoding_job import TranscodingJob, TranscodingJobStatus


@Component
@Singleton
class TranscodingJobRepository(object):

    def __init__(self):
        self.jobs: List[TranscodingJob] = []
        self._lock = threading.Lock()

    def add(self, job: TranscodingJob):
        with self._lock:
            self.jobs.append(job)

    def get_queued(self) -> Nullable[TranscodingJob]:
        with self._lock:
            return Stream(self.jobs) \
                .firstMatch(lambda job: job.status == TranscodingJobStatus.QUEUED) \
                .ifPresent(lambda job: job.set_state(TranscodingJobStatus.IN_PROGRESS))
