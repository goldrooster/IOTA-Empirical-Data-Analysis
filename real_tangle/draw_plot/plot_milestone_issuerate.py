import json  #milestone_time_slope
import numpy as np
import matplotlib.pyplot as plt

# mile_time = []
# for i in range(1,13):
#     with open('D:/Tangle_simulator/timestamp_milestone_slope/MS{}_milestone_time_slope.json'.format(i)) as f:
#         data = json.load(f)
#         timestamp = list(data.keys())
#         mile_time = mile_time+timestamp

# with open('milestamp_timestamp_12.json','w') as f:
#     json.dump(mile_time,f)


with open('milestamp_timestamp_13.json') as f:
    data = json.load(f)
# with open("D:/Users/f80055129/Desktop/Submission_Fig/数据库/MS13/MS13_milestone_dict.json") as f:
#     MS13 = json.load(f)
# for i in MS13:
#     data.append(i['timestamp'])
#
# data = sorted(data)
#
# with open('milestamp_timestamp_13.json','w') as f:
#     json.dump(data,f)
# print(data)
print('finish')
print(max(data))
# print(data)
##min  1477332033
##max  1537178395
##max 1554881404 2019-4-10 9:30am

##max(with 12) 1545469290
#6h 9974394
#12h 4987196
#24h 2493599
# issue_rate = {}
# for i in range(1,9974380):
#     s = 0
#     if 1477332033+ 21600*(i-1) < int(data[i]) < 1477332033+21600*i:
#         s+=1
#     issue_rate[i] = s
# print(issue_rate)

# print(int(data[0]))
# for j in range(1,9974380):
#     a = []
#     for i in data:
#         if 1477332033+ 21600*(0) < int(i) < 1477332033+21600*1:
#             a.append(int(i))
# print(len(a))
# l = []
# for i in data:
#     if 1477332033+ 21600 < int(i) < 1477332033+21600*2:
#         l.append(i)
# print(len(l))

def rate(interval):
    t = {}
    a = 1
    l = []
    for i,j in enumerate(data):
        if int(j) < 1477332033+interval * a:
            None
        else:
            a+=1
            l.append(i-1)
            # print(i-1)
        # print(len(l))
    # print(l)
    return l
def yaxis(interval):
    l = rate(interval)
    y = [l[0]]
    for i,j in enumerate(l):
        if i > 0:
            y.append(l[i]-l[i-1])
    print(y)
    return y

y1 = yaxis(21600)
y2 = yaxis(43200)
y3 = yaxis(86400)
fig = plt.figure(figsize=(3, 2))
plt.scatter([i*4 for i in range(len(y3))],y3,marker='^',label = 'Interval = 24h',s =2,color = 'blue',alpha=0.5)
plt.scatter([i*2 for i in range(len(y2))], y2,marker='.',label = 'Interval = 12h',s = 2,color = 'xkcd:green',alpha=0.5)
# plt.scatter(range(len(y1)),y1,marker='.',label = 'Interval = 6h',s = 2,color = 'blue',alpha=0.7)
plt.xlabel('Time Units',fontsize=6)
plt.ylabel('Milestone (#$10^{3}$)',fontsize=6)
plt.xticks(range(0,3600,250),['Nov\n2016','','Mar\n2017','','Jul','','Nov','','Mar\n2018','','Jul','','Nov','', 'Mar\n2019','May'])
plt.yticks(range(0,7000,1000),['0','1','2','3','4','5','6'])
ax = plt.gca()
linewidth = 0.4
ax.spines['bottom'].set_linewidth(linewidth)
ax.spines['left'].set_linewidth(linewidth)
ax.spines['right'].set_linewidth(linewidth)
ax.spines['top'].set_linewidth(linewidth)
plt.xticks(fontsize=6)
plt.yticks(fontsize=6)
plt.subplots_adjust(left=0.18, right=0.95, top=0.95, bottom=0.3)
plt.margins(tight=True)
plt.legend(fontsize=5)
plt.tight_layout()

# plt.savefig('./eps_13/MS_mile_issuerate.pdf',bbox_inches = 'tight',pad_inches=0)
# plt.savefig('./eps_13/MS_mile_issuerate.png',bbox_inches = 'tight',pad_inches=0)
# plt.savefig('')
plt.show()
