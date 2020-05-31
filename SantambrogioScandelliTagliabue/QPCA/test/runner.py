import os
import numpy as np

for j in range(4,8):
    os.system('python qpca_error_test.py 4 '+str(j)+' 0 4 4 0.14 500')
