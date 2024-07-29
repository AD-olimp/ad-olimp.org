from dataclasses import asdict

from src.app import App
from src.config import configuration
from src.api.v1 import router_v1


def main():
    return App(host='0.0.0.0', port=8000, **asdict(configuration.app)) \
        .included_cors() \
        .included_routers(routers=[router_v1])


if __name__ == '__main__':
    main()
