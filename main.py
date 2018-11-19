import logging

from jivago.jivago_application import JivagoApplication
from jivago.lang.registry import Registry

import prismarine
from prismarine.infrastructure.config.prismarine_context import PrismarineContext

logging.getLogger().setLevel(logging.INFO)
app = JivagoApplication(prismarine, context=PrismarineContext(prismarine, Registry()))

if __name__ == '__main__':
    app.run_dev(host='0.0.0.0', port=4000)
