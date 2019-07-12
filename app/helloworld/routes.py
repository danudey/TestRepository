# aiohttpdemo_polls/routes.py
from .views import index, health, breakit

def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_get('/health_check', health)
    app.router.add_get('/breakit', breakit)
