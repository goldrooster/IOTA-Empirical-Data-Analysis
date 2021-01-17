import json
import numpy as np

def confirmation(m,n):
    ## confirmation relation
    with open("D:/MS8/mileconfirm_sites_new/MS%s_%s_tx_per_mile_confirm_spe_fast.json" %(m,n)) as f:
        data = json.load(f)
    ## timestamp of the milestones and transactions
    with open("timestamp_allsites/MS%s_%s_timestamp_allsites.json" %(m,n)) as f:
        timestamp = json.load(f)

    confirmation_t_list = []
    confirmation_t_dict = {}
    for i in data.items():
        for j in i[1]:
            t = timestamp["{}".format(i[0])][0] - timestamp["{}".format(j)][0]
            if t > 0:
                confirmation_t_list.append(t)
                confirmation_t_dict[j] = t

    print("MS%s_%s" %(m,n),len(confirmation_t_list),np.mean(confirmation_t_list))
    with open("timestamp_delay_new/MS%s_%s_dict.json" %(m,n),'w') as f:
        json.dump(confirmation_t_dict,f)
for n in [4]:
    confirmation(8,n)
