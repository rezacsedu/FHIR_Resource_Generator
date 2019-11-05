from json import dumps

def Entry(data):
    """Generates and returns the transaction entry"""

    if "id" not in data:
        raise BaseException("Entry has no 'id'\n%s"%dumps(
            data,
            sort_keys=False,
            indent=4
        ))

    if "resourceType" not in data:
        raise BaseException("Entry has no 'resourceType'\n%s"%dumps(
            data,
            sort_keys=False,
            indent=4
        ))

    return {
        "request": {
            "method": "PUT",
            "url": data["resourceType"] + "/" + data["id"]
        },
        "resource": data
    }
