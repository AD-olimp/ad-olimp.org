from bson import ObjectId
from fastapi import APIRouter
from src.models.posts import Post
from src.config.database import post
from src.schemas.scheme import list_serial


router = APIRouter(
    prefix="/publications",
    tags=["Publication"]
)


@router.get("")
async def get_publication():
    posts = list_serial(post.find())
    return posts


@router.post("")
async def post_publication(item: Post):
    post.insert_one(dict(item))
    return {"status": 200}


@router.put("/{id}")
async def edit_publication(id: str, item: Post):
    post.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(item)})
    return {"status": 200}


@router.delete("/{id}")
async def delete_publication(id: str):
    post.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": 200}
