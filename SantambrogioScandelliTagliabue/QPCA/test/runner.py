import os
import numpy as np

for j in range(4,5,2):
    os.system('python qpca_tester.py 16 9 0 '+str(j))
