import json
import matplotlib.pyplot as plt
#longest path
MS17_l = [24188, 42481, 42314, 635201, 1132339, 589288, 289577]
MS8_l = [107642, 17387, 6135, 363, 7226, 68540, 1262, 724571]
MS8_l.reverse()
MS9_l = [320531, 120931, 554478, 212013]
MS10_l = [264444, 121354, 136390, 179111, 149835, 112115, 87321, 95621, 71132]
MS11_l = [120295, 94242, 4018, 4437, 11859, 11300, 5286, 6844, 9774, 2538, 11225, 37538, 96749, 69407, 37147, 33370, 115131, 115876, 40692, 47097, 38903, 11030, 103960, 53194, 19984, 278191]
MS12_l = [379241, 103175, 110980, 114428, 122302, 120652, 79793, 30457, 31151, 27992, 76878, 114145, 139303, 88597, 36816, 72229, 119278, 83158, 139528, 94137]
MS13_l = [155891, 166809, 229101, 192079, 51470, 111930, 79229, 79822, 12037, 72201, 171092, 38093, 116669, 131203, 124337, 117312, 166351, 123767, 172938, 196206, 56277, 79486]

#shortest path re-calculate in calculator_shortestpath_max_shortesPath.py
MS17_s = [4923,3481,2539, 2253, 2921, 2674, 1405]
MS8_s = [126, 113, 60, 66, 115, 245, 31, 39]
MS8_s.reverse()
MS9_s = [252, 190, 1408, 1565]
MS10_s = [700, 2824, 238, 2424, 305, 1981, 5026, 6378, 3764]
MS11_s = [9034, 6103, 142, 308, 692, 866, 272, 397, 212, 112, 860, 2556, 2361, 3030, 297, 2878, 5123, 4761, 1679, 3313, 2423, 1361, 6865, 3837, 416, 7442]
MS12_s = [4527, 4103, 7223, 3432, 5574, 5816, 4601, 2320, 2162, 2022, 2144, 1659, 2236, 3523, 1460, 2628, 3198, 2525, 7465, 3642]
MS13_s = [328, 1447, 3059, 3061, 2420, 2646, 1165, 2605, 622, 982, 4536, 1445, 5697, 4919, 4869, 5135, 8609, 5838, 6548, 5731, 2405, 3253]

MS_s = MS17_s + MS8_s + MS9_s + MS10_s+ MS11_s+ MS12_s+ MS13_s
MS_l = MS17_l + MS8_l + MS9_l + MS10_l+ MS11_l+ MS12_l+ MS13_l

ration = list(map(lambda x: x[0]/x[1], zip(MS_l, MS_s)))

plt.figure(figsize=(3, 2))
linewidth = 0.6
plt.plot(range(1, len(MS_l) + 1), MS_l, label = 'Longest Path',lw = linewidth, linestyle = '--')
plt.plot(range(1, len(MS_s) + 1), MS_s,label = 'Shortest Path',lw = linewidth, linestyle =':')
plt.plot(range(1, len(ration) + 1), ration,label = 'Diameter Ratio',lw = linewidth)
plt.xlim((0, 97))
# plt.ylim((0, 1000000))
plt.xticks([1,10,20,30,40,50,60,70,80,90,96], fontsize=6)
plt.yscale('log')
plt.xlabel("Tangle Index", fontsize=6)
plt.ylabel('Value ', fontsize=6) # ($10^{3}$)
ax = plt.gca()
ax.spines['bottom'].set_linewidth(linewidth-0.2)
ax.spines['left'].set_linewidth(linewidth-0.2)
ax.spines['right'].set_linewidth(linewidth-0.2)
ax.spines['top'].set_linewidth(linewidth-0.2)
ax.fill_between(range(1, len(MS_l) + 1),MS_s,MS_l, color = 'b',alpha = 0.2)
hl = plt.legend(fontsize= 5.5, ncol = 2)
plt.yticks([1, 100, 10000, 1000000,100000000], fontsize=6)

plt.tight_layout()
plt.savefig('D:/Users/f80055129/Desktop/Submission_Fig/eps_13/ALL_tangle_long_short_ratio_band.png', bbox_inches='tight', pad_inches=0)
plt.savefig('D:/Users/f80055129/Desktop/Submission_Fig/eps_13/ALL_tangle_long_short_ratio_band.pdf',bbox_inches='tight',pad_inches=0)
# plt.show()