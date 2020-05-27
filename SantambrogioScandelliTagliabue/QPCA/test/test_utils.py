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

def create_rand_vec(dim):
    return  np.random.rand(dim)*2 - 1