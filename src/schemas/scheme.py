def individual_serial(post):
    return {
        "id": str(post["_id"]),
        "name": post["name"],
        "text": post["text"],
        "author": post["author"]
    }


def list_serial(posts):
    return [individual_serial(post) for post in posts]