import aiohttp_jinja2
from aiohttp import web

from .config import HOSTNAME

@aiohttp_jinja2.template('index.html')
async def index(request):
    return {"hostname": HOSTNAME}

async def health(request):
    return web.Response(text="It's cool, it's cool.")

async def breakit(request):
    open("/tmp/getbrokeson","w").write("Down we go")
    return web.Response(text="Nah")
