import os
import numpy as np

for j in range(4,6):
    for i in np.arange(0.05,0.16,0.02):
        os.system('python qpca_error_test.py 4 '+str(j)+' 0 4 4 '+str(i)[:4]+' 4')


