from src.app import App
from src.config import app_config
from src.api.v1 import router_v1


def main():
    return App(host='localhost', port=8000, **app_config) \
        .included_cors() \
        .included_routers(routers=[router_v1])


if __name__ == '__main__':
    main()
