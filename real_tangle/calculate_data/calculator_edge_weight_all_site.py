import json
import networkx as nx
import numpy as np

def site_min_cw (n):
    with open('./数据库/MS1_7/branch_link_MS{}.json'.format(n)) as f:
        branch = json.load(f)
    with open('./数据库/MS1_7/trunk_link_MS{}.json'.format(n)) as f:
        trunk = json.load(f)
    with open('./数据库/MS1_7/cw_MS{}.json'.format(n)) as f:
        cw = json.load(f)

    G = nx.DiGraph()

    for e in range(len(branch)):
        a = branch[e][0]
        b = branch[e][1]
        G.add_edge(a, b)
    for e in range(len(trunk)):
        a = trunk[e][0]
        b = trunk[e][1]
        G.add_edge(a, b)
    nodes = list(G.nodes)
    edge = list(G.edges)
    site_diff = {}
    for i in edge:
        if i[0] not in site_diff.keys():
            site_diff[i[0]] = [cw['{}'.format(i[1])] - cw['{}'.format(i[0])]]
        else:
            site_diff[i[0]] = site_diff[i[0]]+ [cw["{}".format(i[1])] - cw["{}".format(i[0])]]
    print(site_diff)

    site_min_diff = {}
    for i in site_diff.items():
        site_min_diff[i[0]] = i[1]
    print(site_min_diff)

    with open('D:/Tangle_simulator/New folder/Real_cw_diff_site/MS{}_site_edge_weight_min.json'.format(n),'w') as f:
        json.dump(site_min_diff,f)

def site_min_cw_sim (n):
    with open('D:/Tangle_simulator/New folder/Simulated_edges/edges_1000000_{}.json'.format(n)) as f:
        edge = json.load(f)

    with open('D:/Tangle_simulator/New folder/Simulated_cw/Sim_{}.json'.format(n)) as f:
        cw = json.load(f)
    cw['1000000'] = 1
    # G = nx.DiGraph()
    #
    # for e in range(len(branch)):
    #     a = branch[e][0]
    #     b = branch[e][1]
    #     G.add_edge(a, b)

    # nodes = list(G.nodes)
    # edge = list(G.edges)
    site_diff = {}
    for i in edge:
        if i[0] not in site_diff.keys():
            site_diff[i[0]] = [cw['{}'.format(i[1])] - cw['{}'.format(i[0])]]
        else:
            site_diff[i[0]] = site_diff[i[0]]+ [cw["{}".format(i[1])] - cw["{}".format(i[0])]]
    # print(site_diff)

    site_min_diff = {}
    for i in site_diff.items():
        site_min_diff[i[0]] = np.mean(np.array(i[1]))
    print(site_min_diff)
    with open('D:/Tangle_simulator/New folder/Simulated_cw_diff/Sim_ew_dict_{}.json'.format(n), 'w') as f:
        json.dump(site_min_diff, f)
    with open('D:/Tangle_simulator/New folder/Simulated_cw_diff_mean/Sim_ew_mean_{}.json'.format(n),'w') as f:
        json.dump(site_min_diff,f)

for n in range(1,10):
    site_min_cw_sim(n)
# site_min_cw_sim()