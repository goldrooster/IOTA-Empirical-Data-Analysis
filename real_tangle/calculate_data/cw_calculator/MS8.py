import json
import networkx as nx

import sys

with open('/home/demo/fyg-iota/branch_trunk/branch_link_MS8_1.json') as f1:
    branch_link = json.load(f1)
with open('/home/demo/fyg-iota/branch_trunk/trunk_link_MS8_1.json') as f2:
    trunk_link = json.load(f2)
with open('/home/demo/fyg-iota/sorted/MS8_1_sorted.json') as f:
    topology = json.load(f2)
G = nx.DiGraph()

for e in range(len(trunk_link)):
    a = trunk_link[e][0]
    b = trunk_link[e][1]
    G.add_edge(a, b)
for e in range(len(branch_link)):
    a = branch_link[e][0]
    b = branch_link[e][1]
    G.add_edge(a, b)

c_w = {}
para = int(sys.argv[1])
for i in topology[((para-1)*10000):(para*10000)]:
    n = len(list(nx.ancestors(G, i)))+1
    c_w[i] = n
# print(c_w)

with open("/home/demo/fyg-iota/cw/MS8_1_cw_{i}_{j}.json".format(i=((para-1)*10000), j=(para*10000)), "w+") as f:
    json.dump(c_w, f)
print(para)