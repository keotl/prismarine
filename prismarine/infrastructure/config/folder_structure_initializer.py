import os
import shutil

from jivago.config.properties.application_properties import ApplicationProperties
from jivago.config.properties.system_environment_properties import SystemEnvironmentProperties
from jivago.config.startup_hooks import Init
from jivago.lang.annotations import Override, Inject
from jivago.lang.runnable import Runnable
from jivago.lang.stream import Stream


@Init
class FolderStructureInitializer(Runnable):

    @Inject
    def __init__(self, application_properties: ApplicationProperties, env: SystemEnvironmentProperties):
        self._transcoded_media_folder = env.get("transcoded_media_folder") or application_properties["transcoded_media_folder"]
        self.folders = Stream.of("media_library", "transcoded_media_folder").map(lambda x: env.get(x) or application_properties[x])

    @Override
    def run(self):
        shutil.rmtree(self._transcoded_media_folder, ignore_errors=True)
        self.folders.forEach(lambda folder: os.makedirs(folder, exist_ok=True))
