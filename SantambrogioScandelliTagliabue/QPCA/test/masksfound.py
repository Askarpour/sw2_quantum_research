import pickle

def check(inst):
    real_val=inst[0]
    #print(sorted(real_val), sum(sorted(real_val)[-2:]))
    return sum(sorted(real_val)[-2:])>0.63
        

def filemetrics(dim, precision, n_iter, n_randvecs, n_topick, threshold_perc, destfile=None, limit=500):
    if destfile is None:
        destfile = "dim"+str(dim)+"_prec"+str(precision)+"_iter"+str(n_iter)+"_rand"+str(n_randvecs)+"_top"+str(n_topick)+"_tresh"+str(threshold_perc).replace(".","")[:3]
        
    destfile = "test_data/" + destfile
    instances = []
    with open(destfile, 'rb') as f:
        while True:
            try:
                inst=pickle.load(f)
                if check(inst):
                    instances.append(inst)
            except(EOFError):
                break
    
    mmse = 0
    count_mse = 0 
    mmasklen = 0
    print(len(instances))
    if limit > len(instances):
        limit=len(instances)
    for i in instances[:limit]:
        real_val = i[0]
        real_val=sorted(real_val)
        mask = [False]*len(real_val)
        found_val = i[2]
        mse = i[4]
        mmse+=sum(mse)
        count_mse += len(mse)
        for v in found_val:
            rval_index = min([i for i in range(len(real_val))], key= lambda x : abs(real_val[x]-v))
            mask[rval_index] = True
        lenmask = 0
        for i in range(len(mask)-1,-1,-1):
            if mask[i]:
                lenmask+=1
            else:
                break
        mmasklen+=lenmask
        print(mask,lenmask)
    return (mmse/count_mse,mmasklen/limit)

print(filemetrics(4,6,3,4,4,0.15))