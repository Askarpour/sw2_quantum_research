import numpy as np
import scipy

#Creates a random covariance matrix dim x dim
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

#Creates a random covariance matrix dim x dim having k eigenvalues that are 
#larger than others
def create_cus_matrix(dim, k):
    w = np.random.randn(dim, k)
    s = w.dot(w.T)
    d = np.diag(np.random.rand(dim))
    s = np.add(s,d)
    return s/np.trace(s)

#Creates a random vector of length dim
def create_rand_vec(dim):
    return  np.random.rand(dim)*2 - 1

#Useful function to merge different eigenvalues found being the same eigenvalue
#due to noisy measurements
def addtoevals(vec, i, prec):
    toremove=[]
    toadd = i
    for j in vec:
        if abs(toadd-j)<=1.01*(1/2**(prec)):
            toremove.append(j)
    for j in toremove:
        vec.remove(j)
    vec.append(toadd)
