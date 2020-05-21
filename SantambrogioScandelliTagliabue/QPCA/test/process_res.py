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

with open(destfile, 'rb') as f:
    while True:
        try:
            print(pickle.load(f))
        except(EOFError):
            break
