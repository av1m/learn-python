import json


def write_json(filename, data):
    with open("{}.json".format(filename), "w") as out:
        out.write(json.dumps(data, indent=4))