import json
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def sit_cw (m,n):
    with open('D:/Users/f80055129/Desktop/branch_trunk/branch_link_MS{x}_{y}.json'.format(x = m, y = n)) as f:
        branch = json.load(f)
    with open('D:/Users/f80055129/Desktop/branch_trunk/trunk_link_MS{x}_{y}.json'.format(x = m, y = n)) as f:
        trunk = json.load(f)
    with open('D:/Users/f80055129/Desktop/cw/cw_30/MS%s_%s.json' % (m, n)) as f:
        cw = json.load(f)
    link_list = branch+trunk
    # print(link_list)
    link_set = []
    for i in link_list:
        link_set.append(tuple(i))
    edge = set(link_set)
    print(len(edge))

    site_diff = {}
    site_diff_list = []
    for i in edge:
        if i[0] not in site_diff.keys():
            diff = [cw['{}'.format(i[1])] - cw['{}'.format(i[0])]]
            site_diff[i[0]] = diff
            site_diff_list.append(diff)
        else:
            site_diff[i[0]] = site_diff[i[0]] + [cw["{}".format(i[1])] - cw["{}".format(i[0])]]
            site_diff_list.append([cw["{}".format(i[1])] - cw["{}".format(i[0])]])
    site_mean_diff = {}
    site_max = {}
    site_min = {}

    for i in site_diff.items():
        site_mean_diff[i[0]] = np.mean(i[1])
        site_max = max(i[1])
        site_min = min(i[1])

    with open('D:/Tangle_simulator/New folder/Real_cw_diff_min_30/MS%s_%s_site_edge_weight_min.json' %(m, n), 'w') as f:
        json.dump(site_min,f)
    with open('D:/Tangle_simulator/New folder/Real_cw_diff_max_30/MS%s_%s_site_edge_weight_min.json' %(m, n), 'w') as f:
        json.dump(site_max,f)
    with open('D:/Tangle_simulator/New folder/Real_cw_diff_mean_30/MS%s_%s_site_edge_weight_min.json' %(m, n), 'w') as f:
        json.dump(site_mean_diff,f)
    # print(site_diff)
    print(len(site_diff_list))

    with open('D:/Tangle_simulator/New folder/Real_cw_diff_site/MS%s_%s_site_edge_weight.json' %(m,n),'w') as f:
        json.dump(site_diff,f)
    with open('D:/Tangle_simulator/New folder/Real_cw_diff_site/MS%s_%s_edge_weight_list.json' % (m, n),'w') as f:
        json.dump(site_diff_list, f)
for n in [1]:
    sit_cw(8,n)
for n in [2,3,4]:
    sit_cw(9,n)
for n in [2,3,6,7,8]:
    sit_cw(10,n)
for n in [5,12,17,20]:
    sit_cw(11,n)
for n in [1,5,7,9,13,14,15,19,20]:
    sit_cw(12,n)
# for n in [5]:
#     sit_cw(12,n)
for n in [4,5,9,10,17]:
    sit_cw(13,n)



