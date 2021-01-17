import networkx as nx
import json
import pandas as pd

## calculate the in-degree of each site in MS8_7
def indegree_dict(name):
    with open('/Users/fengyangguo/Downloads/Code/real_tangle/data/trunk_link_{}.json'.format(name)) as f:
        trunk_link = json.load(f)
    with open('/Users/fengyangguo/Downloads/Code/real_tangle/data/branch_link_{}.json'.format(name)) as f:
        branch_link = json.load(f)


    G = nx.DiGraph()

    for e in range(len(trunk_link)):
        a = trunk_link[e][0]
        b = trunk_link[e][1]
        G.add_edge(a, b)
    for e in range(len(branch_link)):
        a = branch_link[e][0]
        b = branch_link[e][1]
        G.add_edge(a, b)

    in_degree_dict = {}
    for i in G.nodes:
        in_degree_dict[i] = G.in_degree(i)
    with open("/Users/fengyangguo/Downloads/Code/real_tangle/data/{}_indegree_dict.json".format(name),"w") as f:
        json.dump(in_degree_dict,f)


indegree_dict(name="MS{}".format("8_7"))


