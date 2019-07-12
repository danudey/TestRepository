# middlewares.py
import os

from aiohttp import web

from .config import BROKEFILE

async def fixit(request):
        try:
            os.unlink(BROKEFILE)
        except OSError as exc:
            if exc.errno == 2:
                pass
            else:
                return web.Response(text="Unable to remove the brokefile! Guess it's really broken!", status=500)
        return web.HTTPFound('/')


def create_error_middleware():

    @web.middleware
    async def error_middleware(request, handler):
        if request.path == "/fixit":
            return await fixit(request)
        elif os.path.isfile(BROKEFILE):
            return web.Response(text="It broke!\n", status=500)
        else:
            response = await handler(request)
            return response
    return error_middleware


def setup_middlewares(app):
    error_middleware = create_error_middleware()
    app.middlewares.append(error_middleware)
