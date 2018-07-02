import os

from jivago.config.properties.application_properties import ApplicationProperties
from jivago.config.startup_hooks import Init
from jivago.lang.annotations import Override, Inject
from jivago.lang.runnable import Runnable
from jivago.lang.stream import Stream


@Init
class FolderStructureInitializer(Runnable):

    @Inject
    def __init__(self, application_properties: ApplicationProperties):
        self.folders = Stream.of("media_library", "transcoded_media_folder").map(lambda x: application_properties[x])

    @Override
    def run(self):
        self.folders.forEach(lambda folder: os.makedirs(folder, exist_ok=True))
