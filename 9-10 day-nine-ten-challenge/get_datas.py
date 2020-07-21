import requests
import json


base_url = "http://hn.algolia.com/api/v1"


# This URL gets the newest stories.
def get_new():
    new = f"{base_url}/search_by_date?tags=story"
    new_html = requests.get(new).json().get("hits")
    new_datas = []
    for data in new_html:
        new_datas.append(
            {
                "title": data.get("title"),
                "url": data.get("url"),
                "points": data.get("points"),
                "author": data.get("author"),
                "num_comments": data.get("num_comments"),
                "objectID": data.get("objectID"),
                "story_text": data.get("story_text"),
            }
        )
    return new_datas


# This URL gets the most popular stories
def get_popular():
    popular = f"{base_url}/search?tags=story"
    popular_html = requests.get(popular).json().get("hits")
    popular_datas = []
    for data in popular_html:
        popular_datas.append(
            {
                "title": data.get("title"),
                "url": data.get("url"),
                "points": data.get("points"),
                "author": data.get("author"),
                "num_comments": data.get("num_comments"),
                "objectID": data.get("objectID"),
                "story_text": data.get("story_text"),
            }
        )
    return popular_datas


# This function makes the URL to get the detail of a storie by id.
# Heres the documentation: https://hn.algolia.com/api
def get_comment(id):
    return f"{base_url}/items/{id}"