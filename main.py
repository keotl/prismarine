from jivago.jivago_application import JivagoApplication
from jivago.lang.registry import Registry

import prismarine
from prismarine.infrastructure.config.prismarine_context import PrismarineContext

app = JivagoApplication(prismarine, context=PrismarineContext(prismarine.__name__, Registry()))

if __name__ == '__main__':
    from werkzeug.serving import run_simple

    run_simple('0.0.0.0', 4000, app, threaded=True)
