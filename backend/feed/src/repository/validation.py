from functools import wraps
from typing import Callable


def exist_validation(raise_if_exists=False):
    def decorator(f: Callable):
        @wraps(f)
        async def wrapper(*args, **kwargs):
            print(args, kwargs, 'ДАЙТЕ СЕКС')
            publication_id = kwargs.get('publication_id')
            session = kwargs.get('session')
            self = kwargs.get('self') # ебать я придумал конечно

            if publication_id is None:
                raise ValueError('Для проверки существования требуется publication_id')

            publication = self.collection.find_one({"_id": publication_id}, session)

            if publication is None and not raise_if_exists:
                raise KeyError(f'Публикации {publication_id = } не существует')

            await f(*args, **kwargs)

        return wrapper
    return decorator
