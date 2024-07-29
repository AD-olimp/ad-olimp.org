from typing import Any
from src.models.feeds import GetFeed, GetSearch


def transform_filter(feeds_filter: GetFeed) -> dict[Any]:
    p_filter = feeds_filter.publication_filter
    tags = [el.value for el in p_filter.tags]
    if not tags:
        return {"date": {"$gt": p_filter.date_start, "$lt": p_filter.date_end}}
    return {"tags": tags,
            "date": {"$gt": p_filter.date_start, "$lt": p_filter.date_end}}


def get_query(parameters: GetSearch):
    p_filter = parameters.search_filter.publication_filter
    text = parameters.search_filter.text
    tags = [el.value for el in p_filter.tags]
    return ({
        "$and": [
            {"$text": {"$search": text}},
            {"tags": tags} if tags != [] else dict(),
            {"data": {"$gt": p_filter.date_start, "$lt": p_filter.date_end}}
        ]
    }, {"score": {"$meta": "textScore"}})
