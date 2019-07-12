import aiohttp_jinja2
from aiohttp import web

from .config import HOSTNAME, BROKEFILE

@aiohttp_jinja2.template('index.html')
async def index(request):
    return {"hostname": HOSTNAME}

async def health(request):
    return web.Response(text="It's cool, it's cool.\n")

async def breakit(request):
    open(BROKEFILE,"w").write("Down we go!\n")
    return web.Response(text="Nah")
