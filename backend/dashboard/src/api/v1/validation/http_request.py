from fastapi import HTTPException
from typing import Callable, Optional


def check_publication_existence(f: Callable) -> Optional[HTTPException]:
    async def wrapper(*args, **kwargs):
        publication_id = kwargs.get('publication_id')

        if publication_id is None:
            raise HTTPException(
                status_code=500,
                detail='Декоратор check_publication_existence требует поле publication_id'
            )

        try:
            return await f(*args, **kwargs)

        except KeyError:
            raise HTTPException(status_code=404, detail=f"Публикация с {publication_id = } не найдена")

    return wrapper
