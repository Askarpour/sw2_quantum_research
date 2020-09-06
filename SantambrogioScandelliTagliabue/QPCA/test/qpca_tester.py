import sys
import pickle
import random
sys.path.insert(1, '../modules')
from qpca import qpca
from test_utils import create_rand_vec
import numpy as np
from qiskit import IBMQ, Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
IBMQ.save_account('a4cafd7af86fa3201e4308125da261daf2873395617f7337cbf274afb0f4be6492bc30c08fba1693395155dd60f27d961e70a4f0670b9cdf30d0be72b4dd9cad')

IBMQ.load_account()
provider=IBMQ.get_provider(hub='ibm-q', group='open', project='main')


dim = int(sys.argv[1])
precision = int(sys.argv[2])
n_iter = int(sys.argv[3])
n_randvecs = int(sys.argv[4])
threshold_perc = 0.13
if len(sys.argv)<6:
    destfile = "dim"+str(dim)+"_prec"+str(precision)+"_iter"+str(n_iter)+"_rand"+str(n_randvecs)
else:
    destfile = sys.argv[5]
destfile = "test_data/" + destfile

sourcefile = "covmat/covmat"+str(dim)+"x"+str(dim)

with open(sourcefile, "rb") as f:
    covmats = []
    while 1:
        try:
            o = pickle.load(f)
        except EOFError:
            break
        covmats.append(o)

#random.shuffle(covmats)

covmats = [covmats[0]]
#sim= Aer.get_backend('qasm_simulator')#
sim = provider.get_backend('ibmq_vigo')


with open(destfile, "ab") as f:
    for mat in covmats:
        initials = [create_rand_vec(dim) for i in range(n_randvecs)]
        
        real_eigvals = np.linalg.eig(mat)[0]
        real_eigvects = np.linalg.eig(mat)[1].T
        print("REAL EIGENVALUES: ",real_eigvals)
        print("REAL EIGENVECTORS: \n",real_eigvects)
        res = None
        for i in initials:
            if res is None:
                res = qpca(mat, precision, initial=i, backend = sim)
            else:
                res.merge(qpca(mat, precision, initial=i, backend = sim))
        
        x = [i[0] for i in res.get_eigvals()]
        heights = [i[1] for i in res.get_eigvals()]
        
        plt.bar(x, heights,width=0.1)
        
        plt.show()
        
        max_count = res.get_eigvals()[-1][1]
        threshold = max_count * threshold_perc

        # eigvals_to_inspect = [i[0] for i in res.get_eigvals() if i[1]>threshold]
        # print("OVER THRESHOLD: ",eigvals_to_inspect)
        # evals=[]
        # for i in eigvals_to_inspect:
        #     addtoevals(evals, i, precision)
        # print("MERGED: ", evals)
        eigvals_to_inspect=sorted([i[0] for i in res.get_eigvals() if i[1]>threshold])
        print("SELECTED: ",eigvals_to_inspect)
        eigvalstodump = []
        eigvectstodump = []
        msetodump = []
        for e in eigvals_to_inspect:
            max_eigval = [e]
            approx = [res.eigvec_from_eigval(e)[0]]
            mse = []
            print("USING", e)
            for i in range(n_iter):
                r = qpca(mat, precision, initial=approx[-1],backend = sim)
                max_eigval.append(r.get_eigvals()[-1][0])
                approx.append(r.eigvec_from_eigval(max_eigval[-1])[0])
                print("ESTIMATED: ", max_eigval[-1], " , ", approx[-1])
                # compute MSE
                eigv_tocompare = real_eigvects[min([i for i in range(len(real_eigvals))], key= lambda x : abs(real_eigvals[x]-max_eigval[-1]))]
                MSE1 = np.mean(np.subtract(approx[-1], eigv_tocompare)**2)
                MSE2 = np.mean(np.subtract(-approx[-1], eigv_tocompare)**2)
                mse.append(MSE1 if MSE1<MSE2 else MSE2)
            eigvalstodump.append(max_eigval)
            eigvectstodump.append(approx)
            msetodump.append(mse)
        print("results: ",[real_eigvals, real_eigvects, eigvalstodump, eigvectstodump, msetodump], f)
