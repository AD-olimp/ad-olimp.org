from typing import Any
from src.models.feeds import GetFeed, GetSearch


def transform_filter(feeds_filter: GetFeed) -> dict[Any]:
    pub_filter = feeds_filter.publication_filter
    if not pub_filter.tags:
        return dict()
    return {"tags": [el.value for el in pub_filter.tags],
            "date": {"$gt": pub_filter.date_start, "$lt": pub_filter.date_end}}


def get_pipeline(parameters: GetSearch):
    p_filter = parameters.search_filter.publication_filter
    text = parameters.search_filter.text
    text_dict = {"$text": {"$search": text}} if text != "" else dict()
    tags_dict = {"tags": [el.value for el in p_filter.tags]} if [el.value for el in p_filter.tags] != [] else dict()
    score_dict = {"score": {"$meta": "textScore"}} if text_dict != dict() else dict()
    used_text_filter = text_dict != dict()
    return ({
        "$and": [
            text_dict,
            tags_dict,
            {"data": {"$gt": p_filter.date_start, "$lt": p_filter.date_end}}
        ]
    }, score_dict, used_text_filter)
