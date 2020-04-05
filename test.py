import json
import sys
sys.path.insert(1, '/home/mdaquin/code/ingraph/')
from ingraph.ingraph import InGraph
from kwaku.graphtojson import export

config = {
    "query": "outedges:role OR biography:* OR outedges:affiliation",
    "size": 400,
    "attributes": {
        "biography": "biography",
        "titles": "-author..title"
        }
    }

graphid  = "test_ptg_graph"
es_url = "http://127.0.0.1:9200/"

graph = InGraph(graphid, es_url)

print(json.dumps(export(config, graph), indent=3))
