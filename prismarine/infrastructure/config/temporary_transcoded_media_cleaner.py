import os

from jivago.config.properties.application_properties import ApplicationProperties
from jivago.config.properties.system_environment_properties import SystemEnvironmentProperties
from jivago.config.startup_hooks import PostInit
from jivago.lang.annotations import Override, Inject
from jivago.lang.runnable import Runnable
from jivago.lang.stream import Stream
from jivago.scheduling.annotations import Scheduled, Duration


@PostInit
@Scheduled(every=Duration.HOUR)
class TemporaryTranscodedMediaCleaner(Runnable):

    @Inject
    def __init__(self, application_properties: ApplicationProperties, env: SystemEnvironmentProperties):
        self.transcodedMediaFolder = env.get("transcoded_media_folder") or application_properties["transcoded_media_folder"]

    @Override
    def run(self):
        Stream(os.listdir(self.transcodedMediaFolder)).map(lambda filename: os.path.join(self.transcodedMediaFolder, filename)).forEach(lambda x: os.remove(x))
