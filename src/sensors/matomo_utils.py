# coding: utf-8
import json

import requests
import logging
base_url = "http://benchmark-analytics-open.apps.op.acp.adeo.com/"
token = "0b44547f5f0c9d526b46247c65aeef57"
# logging.basicConfig(level=logging.DEBUG)
def basicMatomoRequest(method = "", query = {}):
    params = dict()
    params['token_auth'] = token
    params['module'] = "API"
    params['method'] = method
    params["period"] = "range"
    params["date"] = "2020-01-02,2020-01-10"
    params["format"] = "JSON"
    params["idSite"] = "1"
    params.update(query)
    return requests.get(base_url, params=params)

def getValueFromActionID(segment, id):
    params = dict()
    params["segment"] = segment
    params["idSubtable"] = id
    response = basicMatomoRequest(method="Events.getNameFromActionId", query=params)
    if response.status_code == 200:
        responsesList = []
        for values in response.json():
            responsesList.append(values["label"])
        return responsesList
    raise

def getActionsIdByCategory(segment):
    params = dict()
    params["segment"] = segment
    response = basicMatomoRequest(method="Events.getAction", query=params)
    if response.status_code == 200:
        idSubList = dict()
        idSubList["idsubdatatable"] = []
        idSubList["label"] = []
        for action in response.json():
            idSubList["idsubdatatable"].append(action["idsubdatatable"])
            idSubList["label"].append(action["label"])
        return idSubList
    raise


def getCategories():
    params = dict()
    response = basicMatomoRequest(method="Events.getCategory", query=params)
    if response.status_code == 200:
        categoryList = dict()
        categoryList["segment"] = []
        categoryList["label"] = []
        for category in response.json():
            categoryList["segment"].append(category["segment"])
            categoryList["label"].append(category["label"])
        return categoryList
    raise

categoryList = getCategories()
print(categoryList)
for segment in categoryList["segment"]:
    idSubList = getActionsIdByCategory(segment)
    print(idSubList)





