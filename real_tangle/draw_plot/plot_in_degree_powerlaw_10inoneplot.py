import matplotlib.pyplot as plt

import numpy as np
from numpy import pi, r_
import matplotlib.pyplot as plt
from scipy import optimize
import json
from collections import Counter
import random

powerlaw = lambda x, amp, index: amp * (x ** index)


def gen_data(i):
    # with open("D:/Tangle_data_analysis/tx_indegree_data_dict/MS10_{}_indegree_dict.json".format(i)) as f:
    #     data = json.load(f)
    with open('ALL_tangle_all_in_degree_list.json') as f:
        data_list = json.load(f)
    # with open('plot_all_Tangle/All_tangle_in_degree_powerlaw_co.json') as f:
    #     co = json.load(f)
    data_list = data_list[i-1]
    data_c = Counter(data_list)
    xaxis = list(data_c.keys())
    xdata = np.array(xaxis)[1:]
    ydata = np.array(list(data_c.values()))[1:]
    ydata = ydata / len(data_list) * 100
    yerr = 0.2 * ydata  # simulated errors (10%)

    logx = np.log10(xdata)
    logy = np.log10(ydata)
    logyerr = yerr / ydata

    # define our (line) fitting function
    fitfunc = lambda p, x: p[0] + p[1] * x
    errfunc = lambda p, x, y, err: (y - fitfunc(p, x)) / err

    pinit = [1.0, -1.0]
    out = optimize.leastsq(errfunc, pinit,
                           args=(logx, logy, logyerr), full_output=1)

    pfinal = out[0]
    covar = out[1]
    print(pfinal)
    print(covar)

    index = pfinal[1]
    amp = 10.0 ** pfinal[0]

    # index = co['{}'.format(i)][1]
    # amp = co['{}'.format(i)][0]

    return xdata, amp, index, ydata


l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
label = [['Tangle 8','Tangle 18','Tangle 22'],['Tangle 28','Tangle 33','Tangle 43'],['Tangle 66','Tangle 70','Tangle 82']]
shape = [['.','o','v'],['^','<','>'],['s','p','*']]
color = [['green','blue','gray'],['green','blue','gray'],['green','blue','gray']]
ar = np.mat(l)
br = np.mat(label)
sr = np.mat(shape)
cr = np.mat(color)
print(ar)
print(ar[0, 0])

i = 1
for n in [8,18,22,28,33,43,66,70,82]:
# for n in [8]:
    print(i)
    locals()['a{}'.format(i)], locals()['b{}'.format(i)], locals()['c{}'.format(i)], locals()[
            'd{}'.format(i)] = gen_data(n)
    i = i+1

fig, ax = plt.subplots(figsize=(3, 2))

# ax[0, 0].tick_params(labelsize=3,)
# ax[0, 0].loglog(a1,powerlaw(a1,b1,c1),color='r',lw=lw)
# ax[0, 0].scatter(a1,d1,marker='.', s=sw)
linewidth = 0.6
lw = 0.6
sw = 3
for i in range(0, 3):
    for j in range(0, 3):
        a1 = locals()['a{}'.format(ar[i, j])]
        b1 = locals()['b{}'.format(ar[i, j])]
        c1 = locals()['c{}'.format(ar[i, j])]
        d1 = locals()['d{}'.format(ar[i, j])]
        ax.loglog(a1, powerlaw(a1, b1, c1), color='r', lw=lw)
        ax.scatter(a1, d1, s=sw, label=br[i, j],alpha = 0.3, marker = sr[i,j],color = cr[i,j])
linewidth = 0.6
        # ax[i, j].set_xticks([1,100,10000,1000000])
        # ax[i, j].set_yticks([0.00001,0.01,1,100])
ax.set_xticks([1,10, 100,1000, 10000])
ax.set_yticks([0.00001,0.0001,0.001,0.01, 0.1,1, 10,100])
ax.spines['left'].set_linewidth(linewidth)
ax.spines['right'].set_linewidth(linewidth)
ax.spines['top'].set_linewidth(linewidth)
ax.spines['bottom'].set_linewidth(linewidth)
ax.legend(fontsize=5)
fig.text(0.5, 0, 'In-degree Value', ha='center', fontsize=6)
fig.text(0, 0.5, 'Fraction (%)', va='center', rotation='vertical', fontsize=6)
plt.xticks(fontsize = 6)
plt.yticks(fontsize = 6)
plt.tight_layout()
plt.margins(tight=True)
plt.tight_layout()
# plt.subplots_adjust(left=0.18, right=0.95, top=0.95, bottom=0.3)
plt.savefig('D:/Users/f80055129/Desktop/Submission_Fig/eps_13/ALL_tangle_indegree_powerlaw_fitting.pdf',
            bbox_inches='tight', pad_inches=0)
plt.savefig('D:/Users/f80055129/Desktop/Submission_Fig/eps_13/ALL_tangle_indegree_powerlaw_fitting.png',
            bbox_inches='tight', pad_inches=0)
plt.show()
