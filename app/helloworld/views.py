import aiohttp_jinja2
from .config import HOSTNAME

@aiohttp_jinja2.template('index.html')
async def index(request):
    return {"hostname": HOSTNAME}
