import json


n = 13
m = 933211
with open('D:/Tangle_simulator/timestamp_milestone_index_time/MS{}_milestone_time.json'.format(n)) as f:
    data = json.load(f)
length = len(data)


slope = {}
slope[data['{}'.format(m)]] = 0
for i,j in enumerate(data.items()):
    if i > 0:
        slope[data[j[0]]] =1
print(slope)
print(len(slope))
with open('D:/Tangle_simulator/timestamp_milestone_slope/MS{}_milestone_time_slope.json'.format(n),'w') as f:
    json.dump(slope,f)
