from jivago.config.debug_jivago_context import DebugJivagoContext
from jivago.lang.annotations import Override

from prismarine.infrastructure.config.persistence_binder import PersistenceBinder


class PrismarineContext(DebugJivagoContext):

    @Override
    def configure_service_locator(self):
        PersistenceBinder().bind(self.serviceLocator)
        super().configure_service_locator()
