from datetime import datetime, timedelta
from uuid import UUID


class TranscodingJobStatus(object):
    QUEUED = object()
    IN_PROGRESS = object()
    DONE = object()
    FILE_DELETED = object()
    ERRORED = object()


class TranscodingJob(object):

    def __init__(self, start_time: datetime, track_id: UUID, source_file: str, transcoded_file: str,
                 status=TranscodingJobStatus.QUEUED):
        self.source_file = source_file
        self.transcoded_file = transcoded_file
        self.start_time = start_time
        self.track_id = track_id
        self.status = status

    def age(self) -> timedelta:
        return datetime.now() - self.start_time

    def set_state(self, state: TranscodingJobStatus):
        self.status = state
