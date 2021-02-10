import pickle
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

sourcefile = ""

with open(sourcefile, "rb") as f:
    covmats = []
    while 1:
        try:
            o = pickle.load(f)
        except EOFError:
            break
        covmats.append(o)

eigvals = [0]*len(covmats[0])

for mat in covmats:
        eig = np.linalg.eig(mat)[0]
        eig[::-1].sort()
        for i in range(len(eig)):
            eigvals[i] += eig[i]

eigvals = [i/len(covmats) for i in eigvals]

fig = plt.figure(figsize=(8,5))
sing_vals = np.arange(len(eigvals)) + 1
plt.plot(sing_vals, eigvals, 'bo-', linewidth=2)
plt.xlabel('Principal Component')
plt.xticks(sing_vals)
plt.ylabel('Eigenvalue')
#I don't like the default legend so I typically make mine like below, e.g.
#with smaller fonts and a bit transparent so I do not cover up data, and make
#it moveable by the viewer in case upper-right is a bad place for it
leg = plt.legend(['Eigenvalues'], loc='best', borderpad=0.3,
                 shadow=False, prop=matplotlib.font_manager.FontProperties(size='small'),
                 markerscale=0.4)
leg.get_frame().set_alpha(0.4)
#plt.show()
plt.savefig("averaged_scree_plot_.png")
