import json
import pandas as pd
def creater_1_3():
    with open('D:/Tangle_simulator/timestamp/MS3_timestamp.json') as f:
        data = json.load(f)
    print(len(data.keys()))
    print()
    sorted_time = sorted(list(data.keys()))

    milestone_time = {}
    for i,j in enumerate(sorted_time):
        milestone_time[13251+i] = j
    print(milestone_time)

    with open('D:/Tangle_simulator/timestamp_milestone_index_time/MS3_milestone_time.json','w') as f:
        json.dump(milestone_time,f)

def creater_4_11(n):
    with open('D:\Tangle_data_analysis\milestone_dataset\MS{}_milestone_dict.json'.format(n)) as f:
        data = json.load(f)
    milestone_time = {}
    for i,j in enumerate(data):
        milestone_time[data[i]['index']] = data[i]['timestamp']
    with open('D:/Tangle_simulator/timestamp_milestone_index_time/MS{}_milestone_time.json'.format(n), 'w') as f:
        json.dump(milestone_time, f)
    print(n)
# for i in range(4,12):
#     creater_4_11(i)
creater_4_11(12)