from jivago.wsgi.annotations import Resource
from jivago.wsgi.methods import GET


@Resource("/version")
class VersionResource(object):

    @GET
    def version_check(self) -> dict:
        return {"name": "prismarine", "version": "0.0.1"}
