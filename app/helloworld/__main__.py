from .helloworld import app, setup_routes, web

if __name__ == "__main__":
    setup_routes(app)
    web.run_app(app)