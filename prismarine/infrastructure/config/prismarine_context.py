from typing import Type, List

from jivago.config.debug_jivago_context import DebugJivagoContext
from jivago.lang.annotations import Override
from jivago.wsgi.filters.filter import Filter

from prismarine.infrastructure.config.persistence_binder import PersistenceBinder
from prismarine.infrastructure.cors_all_open_filter import CorsAllOpenFilter


class PrismarineContext(DebugJivagoContext):

    @Override
    def configure_service_locator(self):
        PersistenceBinder().bind(self.serviceLocator)
        super().configure_service_locator()

    @Override
    def get_filters(self, path: str) -> List[Type[Filter]]:
        return super().get_filters(path) + [CorsAllOpenFilter]
