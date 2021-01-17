import json

## attach timestamp and issuing timestamp
def timestamp(m,n):
    with open('/Users/fengyangguo/Downloads/Code/real_tangle/data/MS%s_%s.json' %(m,n)) as f:
        data = json.load(f)

    with open('/Users/fengyangguo/Downloads/Code/real_tangle/data/MS%s_%s_sort_timestamp.json' %(m,n)) as f:
        b_e_time = json.load(f)
    print(len(b_e_time))
    b_time = int(min(b_e_time))
    e_time = int(max(b_e_time))
    max_delay = int(e_time) - int(b_time)
    print(b_time)
    print(e_time)

    timestamp = {}
    ### if at and it are valid, then timestamp = at,it
    it13=[]
    it10 = []
    for j,i in enumerate(data):
        at = int(i['attachment_timestamp'])
        it = int(i['timestamp'])
        at_cut = i['attachment_timestamp'][0:10]
        if len(i['timestamp']) > 10:
            it13.append(i)
        if len(i['timestamp']) == 10:
            it10.append(i)
        if at >b_time and at < e_time:
            if it > b_time and it < e_time:
                t = [at,it]
            else:
                t = [at]
        else:
            if int(at_cut) > b_time and int(at_cut) < e_time:
                if it > b_time and it < e_time:
                    t = [int(at_cut),it]
            else:
                t = [it]

        timestamp[j] = t

    print(timestamp[3224])
    # print(timestamp)
    print(len(timestamp))
    print(len(it13))
    print(len(it10))
    # with open('./timestamp_allsites/MS%s_%s_timestamp_allsites.json' %(m,n),'w') as f:
    #     json.dump(timestamp,f)

timestamp(8, 7)

# for n in range(1, 5):
#     timestamp(9, n)
# for n in range(1, 10):
#     timestamp(10, n)
# for n in range(1, 27):
#     timestamp(11, n)
# for n in range(4, 21):
#     timestamp(12, n)
# for n in range(1, 23):
#     timestamp(13, n)
