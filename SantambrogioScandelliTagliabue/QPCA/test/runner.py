import os
import numpy as np

for j in range(4,6):
    for i in np.arange(0.05,0.15,0.02):
        os.system('python qpca_error_test.py 2 '+str(j)+' 3 8 2 '+str(i)[:4]+' 200')

