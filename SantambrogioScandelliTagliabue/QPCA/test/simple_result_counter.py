import pickle
import sys
#Simple script useful to print a result file and count how many matrices have been
# analysed in that file

counter = 0
dim = int(sys.argv[1])
precision = int(sys.argv[2])
n_iter = int(sys.argv[3])
n_randvecs = int(sys.argv[4])

if len(sys.argv)<6:
    destfile = "dim"+str(dim)+"_prec"+str(precision)+"_iter"+str(n_iter)+"_rand"+str(n_randvecs)
else:
    destfile = sys.argv[5]
destfile = "test_data/" + destfile

with open(destfile, 'rb') as f:
    while True:
        try:
            print(pickle.load(f))
            counter+=1
        except(EOFError):
            break
print(counter)
