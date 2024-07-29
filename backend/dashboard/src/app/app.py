from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from src.config import NGINXConfig


class App(FastAPI):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def included_routers(self, routers: list[APIRouter]):
        for router in routers:
            self.include_router(router)

        return self

    def included_cors(self, allow_origins=None, allow_credentials=True, allow_methods=None, allow_headers=None):
        allow_origins = ['*'] if allow_origins is None else allow_origins
        allow_methods = ['*'] if allow_methods is None else allow_methods
        allow_headers = ['*'] if allow_headers is None else allow_headers

        self.add_middleware(
            CORSMiddleware,
            allow_origins=allow_origins,
            allow_credentials=allow_credentials,
            allow_methods=allow_methods,
            allow_headers=allow_headers
        )

        return self
