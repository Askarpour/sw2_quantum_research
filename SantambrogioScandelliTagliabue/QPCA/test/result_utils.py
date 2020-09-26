import numpy as np
import pickle
#Script containing useful functions to parse result data from tests

def check(inst):
    real_val=inst[0]
    #print(sorted(real_val), sum(sorted(real_val)[-2:]))
    return sum(sorted(real_val)[-2:])>0
        

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

def compute_mask_metric(mask):
    lenmask = 0
    for i in range(len(mask)-1,-1,-1):
        if mask[i]:
            lenmask+=1
        else:
            break
    return lenmask

#Compute mean square error of an approximation of an eigenvector from a real eigenvector
def comp_mse(real,approx):
    MSE1 = np.mean(np.subtract(real, approx)**2)
    MSE2 = np.mean(np.subtract(-real, approx)**2)
    return MSE1 if MSE1<MSE2 else MSE2

def filemetrics_fix(dim, precision, n_iter, n_randvecs, destfile=None):
    if destfile is None:
        destfile = "dim"+str(dim)+"_prec"+str(precision)+"_iter"+str(n_iter)+"_rand"+str(n_randvecs)
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
    print(instances[0])
    
    mmse = [0]*(n_iter+1)
    mmasklen = [0]*(n_iter+1)
    for i in instances:
        real_val = i[0]
        for j in range(n_iter+1):
            mse = 0
            count_mse= 0
            mask = [False]*len(real_val)
            found_vals = [k[j] for k in i[2]]
            print("AT ITER "+str(j)+" FOUND ", found_vals)
            for v in range(len(found_vals)):
                #v index of found eig, rval_index index of real eig
                real_val_index = min([i for i in range(len(real_val))], key= lambda x : abs(sorted(real_val)[x]-found_vals[v]))
                real_vec_index = min([i for i in range(len(real_val))], key= lambda x : abs(real_val[x]-found_vals[v]))
                mask[real_val_index] = True
                real_vec = i[1][real_vec_index]
                found_vec = i[3][v][j]
                print("realvec: ",real_vec," found: ", found_vec) 
                mse += comp_mse(real_vec, found_vec)
                count_mse+=1
            lenmask = compute_mask_metric(mask)
            mmse[j]+=mse/count_mse
            mmasklen[j]+=lenmask
            print(mmse,mmasklen)
    print(destfile, mmse, len(instances), mmasklen)
    return (np.array(mmse)/len(instances), np.array(mmasklen)/len(instances))

#print(filemetrics_fix(4,7,2,2))