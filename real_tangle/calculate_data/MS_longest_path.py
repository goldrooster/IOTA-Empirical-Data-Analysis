import json
import pandas as pd
import networkx as nx


# data = pd.read_csv('D:/Tangle_data_analysis/tx_shortest_path_pure_data_csv/MS47_shortest_path_pure.csv')


# longest_path = {}




# for i in [1,2,3,4,5,6,7]:
#
#     with open('E:/研究生毕业设计/数据库/MS1_7/trunk_link_MS{}.json'.format(i)) as f:
#         trunk_link = json.load(f)
#     with open('E:/研究生毕业设计/数据库/MS1_7/branch_link_MS{}.json'.format(i)) as f:
#         branch_link = json.load(f)
#     G = nx.DiGraph()
#     for e in range(len(trunk_link)):
#         a = trunk_link[e][0]
#         b = trunk_link[e][1]
#         G.add_edge(a, b)
#     for e in range(len(branch_link)):
#         a = branch_link[e][0]
#         b = branch_link[e][1]
#         G.add_edge(a, b)
#     x = nx.dag_longest_path(G)
#     y = len(x)
#     print(i,y)
#     longest_path[i] = [x,y]

# with open('MS_17_longest_path.json','w') as f:
#     json.dump(longest_path,f)


def longest_path_811(m,n):
        longest_path = {}
        with open('./数据库/MS{m}/MS{m}_data/trunk/trunk_link_MS{m}_{n}.json'.format(m = m,n = n)) as f:
            trunk_link = json.load(f)
        with open('./数据库/MS{m}/MS{m}_data/branch/branch_link_MS{m}_{n}.json'.format(m = m, n=n)) as f:
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
        x = nx.dag_longest_path(G)
        y = len(x)
        print(n, y)
        longest_path[n] = [x, y]

        with open('D:/Tangle_simulator/New folder/Real_longestpath/MS_{m}_{n}_longest_path.json'.format(m=m,n=n), 'w') as f:
            json.dump(longest_path, f)
for n in range(1,23):
    longest_path_811(13,n)

def longest_path_Sim():
        longest_path = {}
        # for i in [0.001,0.01,0.1,0.3,0.5,1,3,5,7,10]:
        for i in range(1,11):
            with open('D:/Tangle_simulator/New folder/Simulated_edges/edges_1000000_{}.json'.format(i)) as f:
                trunk_link = json.load(f)
            G = nx.DiGraph()
            for e in range(len(trunk_link)):
                a = trunk_link[e][0]
                b = trunk_link[e][1]
                G.add_edge(a, b)

            x = nx.dag_longest_path(G)
            y = len(x)
            print(i, y)
            longest_path[i] = y

        with open('D:/Tangle_simulator/New folder/Sim_longestpath/Sim_longest_path_100w.json', 'w') as f:
            json.dump(longest_path, f)
# longest_path_Sim()
# longest_path_Sim()
# for i in range(1,9):
#     longest_path_811(8,i)
# for i in range(1,5):
#     longest_path_811(9,i)
# for i in range(1,10):
#     longest_path_811(10,i)
# for i in range(1,26):

# longest_path_811(11,26)
# MS9 1 320531
# 2 120931
# 3 554478
# 4 212013
# for i in [26]:
#     longest_path_811(11,i)

# with open('D:/Tangle_simulator/New folder/Simulated_edges/edges_1000000_0.001.json') as f:
#     trunk_link = json.load(f)
# G = nx.DiGraph()
# for e in range(len(trunk_link)):
#     a = trunk_link[e][0]
#     b = trunk_link[e][1]
#     G.add_edge(a, b)
#
# x = nx.dag_longest_path(G)
# y = len(x)
# print(y)

#Sim 100w 71063