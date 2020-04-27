import json
import requests


def parse_github(username):
    """
    This function allows, according to a Github username, to return its node_id, its id as well as its name

    Example:
    parse_github("av1m") # ["MDQ6VXNlcjM2NDU2NzA5", 36456709, "Avi Mimoun"]

    :param username: corresponds to the username Github
    :return list: index 0 is node_id, index 1 is id, index 2 is name
    """
    data = json.loads(requests.get("https://api.github.com/users/{}".format(username)).content)
    return [data["node_id"], data["id"], data["name"]]
