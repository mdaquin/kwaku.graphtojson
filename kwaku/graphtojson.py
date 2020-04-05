
def export(config, graph):
    if "query" not in config:
        return ["config invalid"]
    if "size" not in config:
        return ["config invalid"]        
    if "attributes" not in config:
        return ["config invalid"]
    r=graph.search(query=config["query"], size=config["size"])
    result = []
    for hit in r["hits"]:
        o={}
        for at in config["attributes"]:
            o[at] = process(hit, config["attributes"][at], graph)
        result.append(o)
    return result

def process(node, att, graph):
    res = []
    lookinto = ["outedges", "attributes"]
    catt=att
    if ".." in att:
        catt = att[:att.index("..")]
        lookinto.remove("attributes")
    if catt.startswith("-"):
        if "attributes" in lookinto:
            lookinto.remove("attributes")
        lookinto.remove("outedges")
        lookinto.append("inedges")
        catt = catt[1:]        
    for li in lookinto:
        if li == "attributes":
            if catt in node:
                if isinstance(node[catt], unicode):
                    res = node[catt].encode('utf-8')
                else:
                    res = node[catt]
        if li == "outedges":
            nodes = []
            for oe in node["outedges"]:
                if oe[0] == catt:
                    nodes.append(oe[1])
            if ".." in att:
                for n in nodes:
                    nn = graph.search(query="nodeid:"+n)
                    if len(nn["hits"])>0:
                      nn = nn["hits"][0]
                      res2 = process(nn, att[att.index("..")+2:], graph)
                      if res2 != None:
                          if isinstance(res2, list):
                              res.extend(res2)
                          else:
                              res.append(res2)                      
            else:
                res = nodes
        if li == "inedges":
            nodes = []
            for oe in node["inedges"]:
                if oe[1] == catt:
                    nodes.append(oe[0])
            if ".." in att:
                for n in nodes:
                    nn = graph.search(query='nodeid:"'+n+'"')
                    if len(nn["hits"])>0:
                        nn = nn["hits"][0]
                        res2 = process(nn, att[att.index("..")+2:], graph)
                        if res2 != None:
                            if isinstance(res2, list):
                                res.extend(res2)
                            else:
                                res.append(res2)
            else:
                res = nodes
    return res
            
