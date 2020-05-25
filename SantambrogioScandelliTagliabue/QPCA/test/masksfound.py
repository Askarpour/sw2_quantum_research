import pickle
import sys


dim = int(sys.argv[1])
precision = int(sys.argv[2])
n_iter = int(sys.argv[3])
n_randvecs = int(sys.argv[4])
n_topick = int(sys.argv[5])
threshold_perc = float(sys.argv[6])
if len(sys.argv)<8:
    destfile = "dim"+str(dim)+"_prec"+str(precision)+"_iter"+str(n_iter)+"_rand"+str(n_randvecs)+"_top"+str(n_topick)+"_tresh"+str(threshold_perc).replace(".","")
else:
    destfile = sys.argv[7]
destfile = "test_data/" + destfile
instances = []
with open(destfile, 'rb') as f:
    while True:
        try:
            instances.append(pickle.load(f))
        except(EOFError):
            break

mmse = 0
count_mse =0 
for i in instances:
    
    real_val = i[0]
    real_val=sorted(real_val)
    mask = [False]*len(real_val)
    real_vec = i[1]
    found_val = i[2]
    found_vec = i[3]
    mse = i[4]
    mmse+=sum(mse)
    count_mse += len(mse)
    #print("REAL: ",real_val)
    #print("FOUND: ",found_val)
    for v in found_val:
        rval_index = min([i for i in range(len(real_val))], key= lambda x : abs(real_val[x]-v))
        
        mask[rval_index] = True
    #print(mask)
print(mmse/count_mse)
    