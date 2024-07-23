from typing import Any
from src.models.feeds import GetFeed, GetSearch


def transform_filter(feeds_filter: GetFeed) -> dict[Any]:
    pub_filter = feeds_filter.publication_filter
    if not pub_filter.tags:
        return dict()
    return {"tags": [el.value for el in pub_filter.tags],
            "date": {"$gt": pub_filter.date_start, "$lt": pub_filter.date_end}}
    # return {"tags": [el.value for el in pub_filter.tags]}
