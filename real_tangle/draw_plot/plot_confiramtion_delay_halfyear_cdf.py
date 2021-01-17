import json
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
from collections import Counter
import random

# delay = []
# for i in range(1,23):
#     with open("D:/Tangle_simulator/timestamp_delay_without0/MS13_{}_time_delay.json".format(i)) as f:
#         data = json.load(f)
#     delay = delay+data
#
# with open("D:/Tangle_simulator/timestamp_delay_without0/MS13_time_delay.json.json",'w') as f:
#     json.dump(delay,f)

# with open("ALL_tangle_confirmation_delay_list_min.json") as f:
with open("D:/Tangle_simulator/timestamp_delay_new/Alltangle_confirmation_new.json") as f:
    data = json.load(f)
# print(len(data))
# print(Counter(data[12]))
# color = ['green','blue','gray','red','green','gray','green','blue','gray']
color=['blue','g','orange','orangered','blue']
line = ['-','-','-','-','-.']
# line = ['--','-.',':','-','-.']
data1= []
data2= []
data3= []
data4= []
data5= []
# for i in range(0,4):
#     data1 = data1+data[i]
# for i in range(4,7):
#     data2 = data2+data[i]
# for i in range(7,9):
#     data3 = data3+data[i]
# for i in range(9,11):
#     data4 = data4+data[i]
# for i in range(11,13):
#     data5 = data5+data[i]
for i in range(0,4):
    data1 = data1+data[i]
for i in range(4,7):
    data2 = data2+data[i]
for i in range(7,19):
    data3 = data3+data[i]
data3 = random.sample(data3,int(len(data3)*0.3))
for i in range(19,54):
    data4 = data4+data[i]
data4 = random.sample(data4,int(len(data4)*0.3))
for i in range(54,96):
    data5 = data5+data[i]
data5 = random.sample(data5,int(len(data5)*0.2))
# print(len(data5))
random.seed(10)
# data6 = random.sample(data5,int(len(data5)*0.5))
data0 = [data1,data2,data3,data4,data5]
# data0 = data5
# data0 =[ data0[0]]
label = ['2016.11-2017.05', '2017.06-2017.10', '2017.11-2018.4', '2018.5-2018.10', '2018.10-2019.04']
# def cdf0(data_m):
#     # print('mean',np.mean(np.array(data_m)))
#     # print('median',np.median(np.array(data_m)))
#
#     ecdf = sm.distributions.ECDF(data_m)
#     x = np.linspace(min(data_m),max(data_m))
#     y = ecdf(x)
#     return x,y
def cdf(d,n):
    # plt.hist(data, bins=(len(Counter(data)) -1)*60 , cumulative=True, histtype='step', normed=True,label =label[n] )
    print(len(d))
    d = np.array(d)
    m = np.arange(1, len(d) + 1) / np.float(len(d))
    Xs = np.sort(d)
    ax.step(Xs, m,label =label[n],lw = 0.6, color = color[n],linestyle = line[n])
    plt.xscale('log')

# plt.figure(figsize=(3, 2))
linestyle_tuple = ['-', '--', '-.', ':', '--', '-.', '-', '--', '-.','-.', '-', '--', '-.','-.', '-', '--', '-.']
fig, ax = plt.subplots(figsize=(3, 2))
for i,j in enumerate(data0):
    cdf(j,i)
# cdf(data1,1)


# for n,i in enumerate(data0):
#     # print(i)
#     x,y= cdf(i)
#     plt.step(x,y,label = '{}'.format(label[n]),linestyle = linestyle_tuple[n],lw = 0.8,density = 100)
#

vlinewidth = 0.4
plt.vlines(77,-0.05,1.05, colors = "black", linestyles = "dashed",lw = vlinewidth)
plt.vlines(1,-0.05,1.05, colors = "black", linestyles = "dashed",lw = vlinewidth)
plt.vlines(10,-0.05,1.05, colors = "black", linestyles = "dashed",lw = vlinewidth)
plt.hlines(0.12,0,1000000, colors = "black", linestyles = "dashed",lw = vlinewidth)
plt.hlines(0.65,0,1000000, colors = "black", linestyles = "dashed",lw = vlinewidth)
plt.hlines(0.95,0,1000000, colors = "black", linestyles = "dashed",lw = vlinewidth)
plt.text(300,0.8,'77 mins', fontsize = 5)
plt.arrow(300,0.8,-220,0.14,linewidth = 0.6,head_width =0.005, head_length =0.00005,color = 'red',linestyle = '--')

plt.xlabel("Confirmation Time (min)",fontsize = 6)
plt.ylabel("Fraction (%)",fontsize = 6)
plt.xscale('log')
plt.ylim((-0.05,1.05))
plt.xlim((0,1000000))
# plt.yticks([0.8,0.9,1])
plt.xticks([0.01,0.1,1,10,100,1000,10000,100000,1000000],['$10^{-2}$','$10^{-1}$','$10^{0}$','$10^{1}$','$10^{2}$','$10^{3}$','$10^{4}$','$10^{5}$','$10^{6}$'])
# plt.ylim((0.8,1.02))
plt.yticks([0.,0.12,0.2,0.4,0.6,0.65,0.8,0.95,1.00],[0,12,20,40,60,65,80,95,100])
# plt.yscale('log')
plt.legend(fontsize = 5,loc = 'center right',ncol = 1)
plt.xticks(fontsize=5)
plt.yticks(fontsize=5)
ax = plt.gca()
linewidth = 0.4
ax.spines['bottom'].set_linewidth(linewidth)
ax.spines['left'].set_linewidth(linewidth)
ax.spines['right'].set_linewidth(linewidth)
ax.spines['top'].set_linewidth(linewidth)
plt.subplots_adjust(left=0.18, right=0.95, top=0.95, bottom=0.3)
plt.margins(tight=True)
# plt.tight_layout()
# plt.savefig('D:/Users/f80055129/Desktop/Submission_Fig/eps/1_12/edge_weight_site.eps',bbox_inches='tight')
plt.savefig('D:/Users/f80055129/Desktop/Submission_Fig/eps_13/ALL_tangle_confirmation_delay_cdf10_new.pdf',
            bbox_inches='tight', pad_inches=0)
plt.savefig('D:/Users/f80055129/Desktop/Submission_Fig/eps_13/ALL_tangle_confirmation_delay_cdf10_new.png',
            bbox_inches='tight',pad_inches=0)
plt.show()

