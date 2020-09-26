import pickle
import sys

objects = []
file1=open("dim16_prec9_iter2_rand2.txt","w")
with (open("dim16_prec9_iter2_rand2", "rb")) as openfile:
    while True:
        try:
            objects.append(pickle.load(openfile))
            file1.write(str(pickle.load(openfile)))
        except EOFError:
            break
file1.close();
