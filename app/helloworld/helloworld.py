from aiohttp import web
import aiohttp_jinja2
import jinja2

from socket import gethostname

from .routes import setup_routes
from .config import BASE_DIR


# some bits of text for the page.
# template_data = open('web/index.html', 'rt').read()

# template = Template(template_data)
# output = template.render(hostname=gethostname())

app = web.Application()
aiohttp_jinja2.setup(
    app,
    loader=jinja2.FileSystemLoader(str(BASE_DIR / "templates"))
)

if __name__ == "__main__":
    setup_routes(app)
    web.run_app(app)