import matplotlib.pyplot as plt
import networkx as nx
import json
import numpy as np
import pandas as pd
import seaborn as sns; sns.set()
from scipy.stats import mode

def tx_num_confirmbucket(name):

    with open('{}.json'.format(name)) as f:
            data = json.load(f)

    with open('MS11_milestone_dict.json') as f:
            all_milestone = json.load(f)

    with open("{}_tx_per_mile_confirm_spe_fast.json".format(name)) as f:
        tx_per_mile_confirmed_spec = json.load(f)

    tx_num = {}
    for i in tx_per_mile_confirmed_spec.items():
        tx_num[i[0]] = len(i[1])
    # print(tx_num)

    tx_num_order = {}

    for i,j in enumerate(tx_num.items()):
        tx_num_order[i+1] = j[1]
    # print(tx_num_order)

    tx_num_order_list = list(tx_num_order.values())

    x = np.arange(1,(len(tx_num_order)+1))
    y = list(tx_num.keys())

    hash_index = {}
    for i in all_milestone:
        hash_index[i['hash']] = i['index']
    print(hash_index)

    milestone_index = {}
    for i in y:
        milestone_index[i] =hash_index[data[int(i)]['hash']]
    print(milestone_index)

    z = list(milestone_index.values())

    #write down in csv file
    dataframe = pd.DataFrame({'Milestone_num':x,'Milestone_Index':z,'Milestone':y,'Num of Txs':tx_num_order_list})
    dataframe.to_csv("T:\MS11\MS11_txs_num_buckets\{n}_txs_num_per_confirmbucket.csv".format(n = name),index=False,sep=',')


for i in range(1,27):
    tx_num_confirmbucket("MS11_{}".format(i))
