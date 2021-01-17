import json


## milestone index list  from old to new
def milestone_list():

    with open('/Users/fengyangguo/Downloads/Code/real_tangle/data/MS8_7.json') as f:
            data = json.load(f)

    with open('/Users/fengyangguo/Downloads/Code/real_tangle/data/MS8_milestone_dict.json') as f:
            all_milestone = json.load(f)

    hash_d = {}
    timestamp = {}
    idata = []
    milestone = []


    for idx,item in enumerate(all_milestone):
        hash_d[item["hash"]] = idx
        timestamp[item["timestamp"]] = idx
        idata.append(item)

    for idx,item in enumerate(data):
        if item["hash"] in hash_d:
            milestone_dict = {}
            milestone_dict["idx"] = idx
            milestone_dict["hash"] = item["hash"]
            milestone_dict["timestamp"] = item["timestamp"]
            milestone.append(milestone_dict)
    
    milestone_num = {}
    for i in milestone:
        milestone_num[i["idx"]] = i["timestamp"]

    #print(milestone_num)

    sort_timestamp = sorted(milestone_num.items(), key= lambda  item:item[1])

    milestone_sorted = []
    for i in sort_timestamp:
        milestone_sorted.append(i[0])

    print(len(milestone_sorted))

    with open("/Users/fengyangguo/Downloads/Code/real_tangle/data/{}_sort_timestamp.json".format("MS8_7"),"w") as f:
        json.dump(milestone_sorted,f)
    
milestone_list()



