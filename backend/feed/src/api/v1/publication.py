from fastapi import APIRouter

from .schemas.publication import Publication
 

publication_router = APIRouter(
    prefix="/publications",
    tags=["Publication"]
)


@publication_router.post("/")
async def create_publication(publication: Publication):
    ...

@publication_router.get("/{publication_id}")
async def get_publication(publication_id: str) -> Publication:
    ...

@publication_router.put("/{publication_id}")
async def edit_field_publication(publication_id: str, field, value):
    ...

@publication_router.put("/{publication_id}")
async def edit_publication(publication_id: str, new_publication: Publication):
    ...

@publication_router.delete("/{publication_id}")
async def delete_publication(publication_id: str):
    ...
