import requests


base_url = "http://hn.algolia.com/api/v1"


def get_new_popular(order_by):
    if order_by == "new":
        # This URL gets the newest stories.
        url = f"{base_url}/search_by_date?tags=story"
    else:
        # This URL gets the most popular stories
        url = f"{base_url}/search?tags=story"
    url_list = requests.get(url).json().get("hits")
    url_datas = []
    for data in url_list:
        objectID = data.get("objectID")
        url_datas.append(
            {
                "title": data.get("title"),
                "url": data.get("url"),
                "points": data.get("points"),
                "author": data.get("author"),
                "num_comments": data.get("num_comments"),
                "objectID": objectID,
            }
        )
    return url_datas


# This function makes the URL to get the detail of a storie by id.
# Heres the documentation: https://hn.algolia.com/api
def get_comment(id):
    comment_url = f"{base_url}/items/{id}"
    comment_json = requests.get(comment_url).json()
    comment_children = []
    for json_data in comment_json.get("children"):
        if json_data.get("author") == None:
            comment_children.append({"author": "", "text": "[deleted]"})
        else:
            comment_children.append(
                {"author": json_data.get("author"), "text": json_data.get("text")}
            )
    comment_data = {
        "title": comment_json.get("title"),
        "points": comment_json.get("points"),
        "author": comment_json.get("author"),
        "url": comment_json.get("url"),
        "children": comment_children,
    }
    return comment_data
