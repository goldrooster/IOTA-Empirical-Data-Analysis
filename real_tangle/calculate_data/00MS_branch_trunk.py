import json

## Example, extracting MS8_2 branch and trunk data, store in json file.
def branch_trunk():
    with open("/Users/fengyangguo/Downloads/Code/real_tangle/data/MS8_7.json".format(),"r") as f:
         data = json.load(f)


    hash_d = dict()
    branch_d = dict()
    trunk_d = dict()
    branch_link = []
    trunk_link = []
    idata = []


    for idx, item in enumerate(data):
      hash_d[item['hash']] = idx
      branch_d[item['trunk_transaction_hash']] = idx
      trunk_d[item['branch_transaction_hash']] = idx
      idata.append(item)

    for idx, item in enumerate(idata):
      if item['branch_transaction_hash'] in hash_d:
        branch_link.append((idx, hash_d[item['branch_transaction_hash']]))
      if item['trunk_transaction_hash'] in hash_d:
        trunk_link.append((idx, hash_d[item['trunk_transaction_hash']]))

    print(len(data))

    with open("/Users/fengyangguo/Downloads/Code/real_tangle/data/branch_link_{}.json".format("MS8_7"),"w+") as f:
      f.write(json.dumps(branch_link))
    with open("/Users/fengyangguo/Downloads/Code/real_tangle/data/trunk_link_{}.json".format("MS8_7"),"w+") as f:
      f.write(json.dumps(trunk_link))
    # print('ok')


 #    branch_transaction_hash
branch_trunk()
