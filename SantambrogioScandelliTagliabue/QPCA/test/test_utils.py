import numpy as np
import scipy

def create_matrix(dim):
    data = scipy.random.rand(10,dim)*20
    means = np.mean(data,axis=0)
    u=np.ones(len(data))[None]
    u=u.reshape((len(data),1))
    means=means.reshape((len(data[0]),1))
    centered = data-np.dot(u,means.T)

    covmat = np.dot(centered.transpose(),centered)
    covmat=covmat/np.trace(covmat)
    return covmat

def create_cus_matrix(dim, k):
    w = np.random.randn(dim, k)
    s = w.dot(w.T)
    d = np.diag(np.random.rand(dim))
    s = np.add(s,d)
    return s/np.trace(s)

def create_rand_vec(dim):
    return  np.random.rand(dim)*2 - 1

def addtoevals(vec, i, prec):
    toremove=[]
    toadd = i
    for j in vec:
        if abs(toadd-j)<=1.01*(1/2**(prec)):
            toremove.append(j)
    for j in toremove:
        vec.remove(j)
    vec.append(toadd)
