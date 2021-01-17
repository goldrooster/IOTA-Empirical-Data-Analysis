import networkx as nx
import json

## find the descendants of each milestone, which are confirmed by milestone.

def search_descendants(name):
    with open('/Users/fengyangguo/Downloads/Code/real_tangle/data/trunk_link_{}.json'.format(name)) as f:
                trunk_link = json.load(f)
    with open('/Users/fengyangguo/Downloads/Code/real_tangle/data/branch_link_{}.json'.format(name)) as f:
                branch_link = json.load(f)

    with open('/Users/fengyangguo/Downloads/Code/real_tangle/data/{}_sort_timestamp.json'.format(name)) as f:
                sort_timestamp = json.load(f)

    G = nx.DiGraph()

    for e in range(len(trunk_link)):
        a = trunk_link[e][0]
        b = trunk_link[e][1]
        G.add_edge(a, b)
    for e in range(len(branch_link)):
        a = branch_link[e][0]
        b = branch_link[e][1]
        G.add_edge(a, b)

    tx_per_mile = {}

    for i,j in enumerate(sort_timestamp):
        if i ==0:
            tx_per_mile[j] = list(nx.descendants(G,j))
            for n in (list(nx.descendants(G,j))):
                G.remove_node(n)
        else:
            mile_list = list(nx.descendants(G,j))
            if (sort_timestamp[i-1]) in mile_list:
                # mile_list.remove(sort_timestamp[i-1])
                tx_per_mile[j] = mile_list
                for n in (list(nx.descendants(G,j))):
                    G.remove_node(n)
            else:
                tx_per_mile[j] = mile_list
                for n in (list(nx.descendants(G,j))):
                    G.remove_node(n)
                print("Not contain",sort_timestamp[i-1])
    print(len(tx_per_mile))

    with open("/Users/fengyangguo/Downloads/Code/real_tangle/data/{}_tx_per_mile_confirm_spe_fast_mile.json".format(name),"w") as f:
        json.dump(tx_per_mile,f)

search_descendants(name="MS{}".format("8_7"))









