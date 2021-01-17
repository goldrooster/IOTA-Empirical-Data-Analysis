import json
import matplotlib.pyplot as plt
import numpy as np
with open('ALL_tangle_n_in_degree_list.json') as f:
    indegree = json.load(f)

mean_list = []
for i in indegree:
    mean_list.append(np.mean(np.array(i)))
with open('ALL_tangle_n_in_degree_mean.json') as f:
    # json.dump(mean_list,f)
    mean_list = json.load(f)
with open('ALL_tangle_n_in_degree_median.json') as f:
    median_list= json.load(f)
with open('ALL_tangle_n_in_degree_75.json') as f:
    line75= json.load(f)
with open('ALL_tangle_n_in_degree_25.json') as f:
    line25= json.load(f)
with open('ALL_tangle_n_in_degree_max.json') as f:
    max_list= json.load(f)
with open('ALL_tangle_n_in_degree_min.json') as f:
    min_list= json.load(f)

plt.figure(figsize=(3, 2))
linewidth = 0.6
plt.plot(range(1, len(max_list) + 1), max_list, label = 'Max Value',lw = linewidth, linestyle = '--')
plt.plot(range(1, len(line75) + 1), line75,lw = linewidth, linestyle = ':',alpha = 0)
plt.plot(range(1, len(mean_list) + 1), mean_list,label = 'Mean',lw = linewidth, linestyle ='--')
plt.plot(range(1, len(median_list) + 1), median_list,label = 'Median',lw = linewidth, marker= "^",ms = 1)
plt.plot(range(1, len(line25) + 1), line25,lw = linewidth,alpha = 0)
plt.plot(range(1, len(min_list) + 1), min_list,label = 'Min Value',lw = linewidth)

plt.yscale('log')
plt.xlim((0, 97))
# plt.ylim((-1000, 10000))
plt.xticks([1,10,20,30,40,50,60,70,80,90,96], fontsize=6)
# plt.yticks([1, 100, 10000, 1000000,100000000], fontsize=6)
plt.xlabel("Tangle Index", fontsize=6)
plt.ylabel('In-degree Value ', fontsize=6) # ($10^{3}$)
ax = plt.gca()
ax.spines['bottom'].set_linewidth(linewidth-0.2)
ax.spines['left'].set_linewidth(linewidth-0.2)
ax.spines['right'].set_linewidth(linewidth-0.2)
ax.spines['top'].set_linewidth(linewidth-0.2)
ax.fill_between(range(1, len(line75) + 1),line75,line25, color = 'b',alpha = 0.2, label = '25% to 75% Quartile')

plt.yticks([1, 10,100, 1000,10000,100000,1000000], fontsize=6)

plt.tight_layout()
plt.legend(fontsize=5,ncol = 2 )
# plt.savefig('ALL_tangle_n_indegree_max_min_band.png', bbox_inches='tight', pad_inches=0)
plt.savefig('D:/Users/f80055129/Desktop/Submission_Fig/eps_13/ALL_tangle_n_indegree_max_min_band.pdf',bbox_inches='tight', pad_inches=0)
plt.savefig('D:/Users/f80055129/Desktop/Submission_Fig/eps_13/ALL_tangle_n_indegree_max_min_band.png', bbox_inches='tight', pad_inches=0)
# plt.show()
