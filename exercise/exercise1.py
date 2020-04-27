import requests,json

def parse_github(username):
    contenu = json.loads(requests.get("https://api.github.com/users/"+username).content)
    return [contenu["node_id"],contenu["id"],contenu["name"]]

parse_github("av1m")