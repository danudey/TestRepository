# aiohttpdemo_polls/routes.py
from .views import index, health

def setup_routes(app):
    app.router.add_get('/', index)

def health_check(app):
    app.router.add_get('/health_check', health)
