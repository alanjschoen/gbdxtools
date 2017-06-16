import json
import requests

VIRTUAL_IPE_URL = "https://idahoapitest.geobigdata.io/v1"

from gbdxtools.ipe.error import NotFound

def get_ipe_graph(conn, graph_id):
    url = "{}/graph/{}".format(VIRTUAL_IPE_URL, graph_id)
    req = conn.get(url)
    if req.status_code == 200:
        return req.json()
    else:
        raise NotFound("No IPE graph found matching id: {}".format(graph_id))

def register_ipe_graph(conn, ipe_graph):
    url = "{}/graph".format(VIRTUAL_IPE_URL)
    res = conn.post(url, json.dumps(ipe_graph), headers={'Content-Type': 'application/json'})
    return res.content

def get_ipe_metadata(conn, ipe_id, node):
    meta = {}
    meta['image'] = conn.get(VIRTUAL_IPE_URL + "/metadata/idaho-virtual/{}/{}/image.json".format(ipe_id, node)).json()
    meta['rpcs'] = conn.get(VIRTUAL_IPE_URL + "/metadata/idaho-virtual/{}/{}/rpcs.json".format(ipe_id, node)).json()
    try:
        meta['georef'] = conn.get(VIRTUAL_IPE_URL + "/metadata/idaho-virtual/{}/{}/georeferencing.json".format(ipe_id, node)).json()
    except:
        meta['georef'] = None
    return meta
