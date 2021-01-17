import matplotlib.pyplot as plt
import networkx as nx
import json
import time
import pandas as pd
import csv

##update: 1. search for real head and tail.
##        2. search for real milestone.
def shortest_path(name):
    # name = "MS8_7"
    with open('/Users/fengyangguo/Downloads/Code/real_tangle/data/trunk_link_{}.json'.format(name)) as f:
        trunk_link = json.load(f)
    with open('/Users/fengyangguo/Downloads/Code/real_tangle/data/branch_link_{}.json'.format(name)) as f:
        branch_link = json.load(f)
    with open('/Users/fengyangguo/Downloads/Code/real_tangle/data/MS8_milestone_dict.json') as f:
        milestone = json.load(f)


    with open("/Users/fengyangguo/Downloads/Code/real_tangle/data/{}.json".format(name)) as f:
        data = json.load(f)
    print("{}".format(name))
    G = nx.DiGraph()

    for e in range(len(trunk_link)):
        a = trunk_link[e][0]
        b = trunk_link[e][1]
        G.add_edge(a, b)
    for e in range(len(branch_link)):
        a = branch_link[e][0]
        b = branch_link[e][1]
        G.add_edge(a, b)

    tail_dict = {}
    tail_time = []
    tail_list = []
    for i in range(len(data)):
        if G.in_degree(i) == 0:
            tail = i
            print("The tail is:",i)
            print("Time:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(data[i]["timestamp"]))))
            print("Time:",int(data[i]["timestamp"]))
            a = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(data[i]["timestamp"])))
            tail_dict[int(data[i]["timestamp"])] = i
            tail_time.append(int(data[i]["timestamp"]))
            tail_list.append(i)

    head_dict = {}
    head_time = []
    head_list = []
    for i in range(len(data)):
        if G.out_degree(i) == 0:
            head = i
            print("The head is:",i)
            print("Time:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(data[i]["timestamp"]))))
            print("Time:",int(data[i]["timestamp"]))
            b = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(data[i]["timestamp"])))
            head_dict[int(data[i]["timestamp"])] = i
            head_time.append(int(data[i]["timestamp"]))
            head_list.append(i)

    pure_tail = []
    pure_head = []
    pure_tail_time = []
    pure_head_time = []
    for i in tail_dict.items():
        if i[0] == max(tail_time):
            pure_tail.append(i[1])
            pure_tail_time.append(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(i[0]))))
    for i in head_dict.items():
        if i[0] == min(head_time):
            pure_head.append(i[1])
            pure_head_time.append(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(i[0]))))

    short_path_list = nx.shortest_path(G,source= pure_tail[0] ,target=pure_head[0])

    milestone_hash_list = []
    for i in milestone:
        milestone_hash_list.append(i['hash'])
    milestone = 0
    node_999 = 0
    for i in short_path_list:
        if data[i]["hash"] in  milestone_hash_list:
            milestone+=1
        # if data[i]["address"]== "999999999999999999999999999999999999999999999999999999999999999999999999999999999":
        #     node_999+=1

    # other = len(short_path_list)-milestone-node_999
    print("Txs number is",len(data))
    print("From the tail to head:",len(short_path_list),"sites")
    print("The milestone num.:",milestone)

    dataframe = pd.DataFrame({'Snapshot':/"{}".format(name),'begin_time':pure_head_time,'end_time':pure_tail_time,"txs_num":len(data),'shortest_path':len(short_path_list),'milestone_num':milestone,'head_num':len(head_list),'head_list':[head_list],'tail_num':len(tail_list),'tail_list':[tail_list]})
    dataframe.to_csv("D:\MS1_7\MS17_shortest_path_pure\{}_shortest_path_pure.csv".format(name),index=False,sep=',')


shortest_path("MS{}".format("8_7"))




