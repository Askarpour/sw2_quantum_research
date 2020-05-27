import os
import numpy as np

for j in range(3):
    for i in range(15,33,4):
        os.system('python qpca_error_test.py 2 6 0 '+str(2**j)+' 2 0.'+str(i)+' 200')
