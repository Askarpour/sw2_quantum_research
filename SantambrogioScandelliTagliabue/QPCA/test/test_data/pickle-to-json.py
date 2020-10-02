import pickle
import sys
import json

data={}
data['test']=[]


objects = []
nomefile="dim16_prec9_iter2_rand2"

with (open(nomefile, "rb")) as openfile:
    while True:
        try:
            objects.append(pickle.load(openfile))
            #file1.write(pickle.load(openfile))
            data['test'].append({
                'real_eigvals': str(pickle.load(openfile)[0]),
                'real_eigvects': str(pickle.load(openfile)[1]),
                'eigvalstodump': str(pickle.load(openfile)[2]),
                'eigvectstodump': str(pickle.load(openfile)[3]),
                'msetodump': str(pickle.load(openfile)[4])
                })
            #print("Da qui inizia tutto\n")
            #print(pickle.load(openfile))
        except EOFError:
            break
with open(nomefile + '.json','w') as outfile:
    json.dump(data,outfile)
