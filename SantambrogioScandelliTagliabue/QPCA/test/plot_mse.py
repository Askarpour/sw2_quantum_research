import subprocess
import matplotlib.pyplot as plt

result = []

for i in range(15,28,4):
    result.append(subprocess.check_output(['python','masksfound.py','2','2','3','5','2','0.'+str(i)],shell=True))
    
plt.plot(range(15,28,4),[float(i) for i in result])