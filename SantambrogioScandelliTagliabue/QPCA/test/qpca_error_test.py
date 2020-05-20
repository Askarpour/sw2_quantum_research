import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '../modules')
from qpca import qpca
from test_utils import create_matrix
from test_utils import create_rand_vec
import json
import numpy as np
dim = int(sys.argv[1])
precision = int(sys.argv[2])
n_iter = int(sys.argv[3])
n_randvecs = int(sys.argv[4])
n_topick = int(sys.argv[5])
threshold_perc = float(sys.argv[6])
if len(sys.argv)<8:
    destfile = "temp.json"
else:
    destfile = sys.argv[7]
iteration= 0
to_ser=[]

with open(destfile,"w") as f:
    try:
        for k in range(2):
            
            mat = create_matrix(dim)
            initials = [create_rand_vec(dim) for i in range(n_randvecs)]
            real_eigvals = np.linalg.eig(mat)[0]
            real_eigvects = np.linalg.eig(mat)[1]
            print("NEW MATRIX: ",real_eigvals)
            print(": ",real_eigvects)
            res = None
            for i in initials:
                if res is None:
                    res = qpca(mat, precision, initialeig=i)
                else: 
                    res.merge(qpca(mat, precision, initialeig=i))
            
            max_count = res.get_eigvals()[-1][1]
            threshold = max_count * threshold_perc
            
            
            eigvals_to_inspect = [i[0] for i in res.get_eigvals() if i[1]>threshold]
            print("OVER THRESHOLD: ",eigvals_to_inspect)
            eigvals_to_inspect=sorted(eigvals_to_inspect)
            
            eigvals_to_inspect = eigvals_to_inspect[-n_topick:]
            print("SELECTED: ",eigvals_to_inspect)
            
            for e in eigvals_to_inspect:
                approx = res.eigvec_from_eigval(e)[0]
                print("USING", e)
                eigvalstodump = []
                eigvectstodump=[]
                for i in range(n_iter):
                    r = qpca(mat, precision, initialeig=approx)
                    max_eigval = r.get_eigvals()[-1][0]
                    approx = r.eigvec_from_eigval(max_eigval)[0]
                    eigvalstodump.append(max_eigval)
                    eigvectstodump.append(np.array2string(approx))
                print("ESTIMATED: ", max_eigval, " , ", approx)
            to_ser.append([iteration, np.array2string(real_eigvals), np.array2string(real_eigvects),eigvalstodump,eigvectstodump])
            iteration+=1
                
                
                
                
    except KeyboardInterrupt:
        pass
    json.dump(to_ser,f)