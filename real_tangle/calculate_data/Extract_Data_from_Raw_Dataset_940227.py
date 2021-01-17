import iota
import iotapy
import json

# Export the useful data from the raw dataset, the extracting process begin from the last milestone,
# Because the last milestone is the last confirmed transaction in each dataset.

name = "MS13"

r = iotapy.storage.providers.rocksdb.RocksDBProvider(
        db_path='/home/fyg/MS13/0933210-1039245/mainnetdb',
        db_log_path='/home/fyg/MS13/0933210-1039245/mainnetdb.log',
        read_only=True
    )
r.init()


file = "MS13_940227.json"
all_nines = '9' * 81
#Last milestone hash, the extracting process always begin from the last milestone
solid_milestone = "BYMILWAGSRENEYICAHLOGNQUEYZ9IOTZBEMZGDBCNXAJCQLMHYTXBJAFQWTZZGPVROKJRXTUCYTXZ9999"
traversal_queue = [solid_milestone]

EMPTY = iota.TransactionHash('9' * 81)

tx_list = []
memDB = set()

i = 0
with open(file,"w+") as f:
    while traversal_queue:

        tx_hash = traversal_queue.pop()

        if tx_hash in memDB or tx_hash == all_nines:
            continue

        txh = iota.TransactionHash(tx_hash)
        tx = r.get(txh, 'transaction')
        tx_dict = {}
        txb = str(tx.as_json_compatible()['branch_transaction_hash'])
        txt = str(tx.as_json_compatible()['trunk_transaction_hash'])
        address = str(tx.as_json_compatible()['address'])
        txtime = str(tx.timestamp)

        tx_dict["hash"] = tx_hash
        tx_dict["branch_hash"] = txb
        tx_dict["trunk_hash"] = txt
        tx_dict["timestamp"] = txtime
        tx_dict["address"] = address

        tx_list.append(tx_dict)

        memDB.add(tx_hash)
        traversal_queue.append(txb)
        traversal_queue.append(txt)
        i+=1
        print(i)

    json.dump(tx_list,f)
pass



