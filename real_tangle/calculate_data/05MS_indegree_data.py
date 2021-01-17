import json
import seaborn as sns; sns.set()

## calculate the in-degree of milestone and normal sites.
def indegree_stastic(name):
    with open("/Users/fengyangguo/Downloads/Code/real_tangle/data/{}_tx_per_mile_confirm_spe_fast_mile.json".format(name)) as f:
        tx_per_mile_confirmed_spec = json.load(f)

    with open("/Users/fengyangguo/Downloads/Code/real_tangle/data/{}_indegree_dict.json".format(name)) as f:
        in_degree_dict = json.load(f)

    #in_degree statistic
    in_degree = []
    for i in tx_per_mile_confirmed_spec.items():
        in_degree_d = {}
        in_degree_d["milestone_num"] = i[0]
        in_degree_d["m_in_degree"] = [in_degree_dict[i[0]]]
        n_in_degree = []
        for j in i[1]:
            n_in_degree.append(in_degree_dict["{}".format(j)])
        in_degree_d["n_in_degree"] = n_in_degree
        all_in_degree = [in_degree_dict[i[0]]]+n_in_degree
        in_degree_d["all_in_degree"] = all_in_degree
        in_degree.append(in_degree_d)

    print(len(in_degree))
    with open("/Users/fengyangguo/Downloads/Code/real_tangle/data/{}_in_degree_stastic.json".format(name),"w") as f:
        json.dump(in_degree,f)

indegree_stastic(name="MS{}".format("8_7"))



