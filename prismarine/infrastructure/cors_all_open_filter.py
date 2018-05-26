from jivago.lang.annotations import Override
from jivago.wsgi.filters.filter import Filter
from jivago.wsgi.request.request import Request
from jivago.wsgi.request.response import Response


class CorsAllOpenFilter(Filter):

    @Override
    def doFilter(self, request: Request, response: Response, chain: "FilterChain"):
        chain.doFilter(request, response)

        response.headers['Access-Control-Allow-Origin'] = "*"
