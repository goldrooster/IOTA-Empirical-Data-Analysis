import json
from igraph import Graph
import sys
# MS8_n
n = 1
with open('/home/demo/fyg-iota/branch_trunk/branch_link_MS8_{}.json'.format(n)) as f1:
    branch_link = json.load(f1)
with open('/home/demo/fyg-iota/branch_trunk/trunk_link_MS8_{}.json'.format(n)) as f2:
    trunk_link = json.load(f2)
with open('/home/demo/fyg-iota/sorted/MS8_{}_sorted.json'.format(n)) as f:
    topology = json.load(f)

g = Graph(directed = True)
link = branch_link + trunk_link
link_set = []
for i in link:
    link_set.append(tuple(i))
g.add_vertices(len(topology))
g.add_edges(link_set)

c_w = {}
para = int(sys.argv[1])
for i in topology[((para-1)*10000):(para*10000)]:
    n = len(list(Graph.bfsiter(g, i, mode='in', advanced='False')))
    c_w[i] = n
# print(c_w)

with open("/home/demo/fyg-iota/cw/MS8_{n}_cw_{i}_{j}.json".format(n=n, i=((para-1)*10000), j=(para*10000)), "w+") as f:
    json.dump(c_w, f)
print(para)