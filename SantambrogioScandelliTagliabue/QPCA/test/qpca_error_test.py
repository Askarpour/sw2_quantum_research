import sys
import pickle
sys.path.insert(1, '../modules')
from qpca import qpca
from test_utils import create_matrix
from test_utils import create_rand_vec
import numpy as np

dim = int(sys.argv[1])
precision = int(sys.argv[2])
n_iter = int(sys.argv[3])
n_randvecs = int(sys.argv[4])
n_topick = int(sys.argv[5])
threshold_perc = float(sys.argv[6])
ncomplete = int(sys.argv[7])
if len(sys.argv)<9:
    destfile = "dim"+str(dim)+"_prec"+str(precision)+"_iter"+str(n_iter)+"_rand"+str(n_randvecs)+"_top"+str(n_topick)+"_tresh"+str(threshold_perc).replace(".","")
else:
    destfile = sys.argv[8]
destfile = "test_data/" + destfile

with open(destfile, "ab") as f:
    try:
        for g in range(ncomplete):
            mat = create_matrix(dim)
            initials = [create_rand_vec(dim) for i in range(n_randvecs)]
            real_eigvals = np.linalg.eig(mat)[0]
            real_eigvects = np.linalg.eig(mat)[1].T
            print("REAL EIGENVALUES: ",real_eigvals)
            print("REAL EIGENVECTORS: \n",real_eigvects)
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
            eigvalstodump = []
            eigvectstodump = []
            msetodump = []
            for e in eigvals_to_inspect:
                max_eigval = e
                approx = res.eigvec_from_eigval(e)[0]
                print("USING", e)
                for i in range(n_iter):
                    r = qpca(mat, precision, initialeig=approx)
                    max_eigval = r.get_eigvals()[-1][0]
                    approx = r.eigvec_from_eigval(max_eigval)[0]
                eigvalstodump.append(max_eigval)
                eigvectstodump.append(approx.tolist())
                print("ESTIMATED: ", max_eigval, " , ", approx)
                # compute MSE
                eigv_tocompare = real_eigvects[min([i for i in range(len(real_eigvals))], key= lambda x : abs(real_eigvals[x]-max_eigval))]
                MSE1 = np.mean(np.subtract(approx, eigv_tocompare)**2)
                MSE2 = np.mean(np.subtract(-approx, eigv_tocompare)**2)
                msetodump.append(MSE1 if MSE1<MSE2 else MSE2)
            pickle.dump([real_eigvals.tolist(), real_eigvects.tolist(), eigvalstodump, eigvectstodump, msetodump], f)
    except KeyboardInterrupt:
        pass
