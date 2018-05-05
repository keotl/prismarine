from jivago.inject.registry import Registry
from jivago.jivago_application import JivagoApplication

import prismarine
from prismarine.infrastructure.config.prismarine_context import PrismarineContext

app = JivagoApplication(prismarine, context=PrismarineContext(prismarine.__name__, Registry()))

if __name__ == '__main__':
    from werkzeug.serving import run_simple

    run_simple('localhost', 4000, app)
