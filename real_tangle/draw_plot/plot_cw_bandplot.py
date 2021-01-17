import json
import matplotlib.pyplot as plt
import numpy as np

with open('ALL_tangle_cw_list.json') as f:
    m_indegree = json.load(f)
m_indegree = m_indegree[0:31]
mean_list = []
median_list = []
line75 = []
line25 = []
max_list = []
min_list = []
for i in m_indegree:
    mean_list.append(np.mean(np.array(i)))
    median_list.append(np.median(np.array(i)))
    line75.append(np.percentile(np.array(i),75))
    line25.append(np.percentile(np.array(i),25))
    max_list.append(max(i))
    min_list.append(min(i))

plt.figure(figsize=(3, 2))
linewidth = 0.6
ax = plt.gca()
l1 = plt.plot(range(1, len(max_list) + 1), max_list,label = 'Max Value',lw = linewidth, linestyle = '--') #label = 'Max Value' ,label = 'Mean'
plt.plot(range(1, len(line75) + 1), line75,lw = linewidth, linestyle = ':', alpha = 0)
l2 = plt.plot(range(1, len(mean_list) + 1), mean_list,label = 'Mean',lw = linewidth, linestyle ='-.')
l3 = plt.plot(range(1, len(median_list) + 1), median_list,label = 'Median',lw = linewidth,marker= ".",ms = 1) # ,label = 'Median' ,label = 'Min Value'
plt.plot(range(1, len(line25) + 1), line25,lw = linewidth, alpha = 0)
l4 = plt.plot(range(1, len(min_list) + 1), min_list,label = 'Min Value',lw = linewidth)
l5 = ax.fill_between(range(1, len(line75) + 1), line75, line25, label='25% to 75% Quartile',color='b', alpha=0.2) # , label='25% to 75% Quartile'


plt.yscale('log')
plt.ylim((-1000, 10000000))
plt.xticks(range(1,31),[1,4,5,8,'\n'+'17',18,'\n'+'19',21,'\n'+'22',25,'\n'+'26',27,'\n'+'33',40,'\n'+'45',48,'\n'+'55',59,'\n'+'61',63,'\n'+'66',68,'\n'+'69',73,'\n'+'74',78,'\n'+'79',83,'\n'+'84',91] ,fontsize=5)

plt.xlabel("Tangle Index", fontsize=6)
plt.ylabel('Cumulative Weight ', fontsize=6) # ($10^{3}$)
ax.spines['bottom'].set_linewidth(linewidth-0.2)
ax.spines['left'].set_linewidth(linewidth-0.2)
ax.spines['right'].set_linewidth(linewidth-0.2)
ax.spines['top'].set_linewidth(linewidth-0.2)
plt.yticks([1, 10,100, 1000,10000,100000,1000000,10000000], fontsize=5)

# handles,labels = ax.get_legend_handles_labels()
# ax.legend(handles=[l1,l2,l3,l5,l4],labels=['Max Value','Mean','Median','25% to 75% Quartile','Min Value'])
# plt.legend(handles=[l1,l2,l3,l5,l4],loc='best')

plt.legend(fontsize=5,loc = 'center right',ncol = 1)
plt.savefig('D:/Users/f80055129/Desktop/Submission_Fig/eps_13/ALL_tangle_cw_max_min_band.pdf',bbox_inches='tight', pad_inches=0)
plt.savefig('D:/Users/f80055129/Desktop/Submission_Fig/eps_13/ALL_tangle_cw_max_min_band.png', bbox_inches='tight', pad_inches=0)
plt.show()
