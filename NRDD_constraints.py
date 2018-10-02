import numpy as np
from scipy import interpolate

planes1=np.load('NRDD_data1.npy')
planes2=np.load('NRDD_data2.npy')

planes=np.append(planes1,planes2).reshape(17,3)

interactions={'O1_O1':0, 'O3_O3':1, 'O4_O4':2, 'O5_O5':3, 'O6_O6':4,
              'O7_O7':5, 'O8_O8':6, 'O9_O9':7, 'O10_O10':8,
              'O11_O11':9, 'O12_O12':10, 'O13_O13':11, 'O14_O14':12,
              'O15_O15':13, 'O5_O5_qm4':14, 'O6_O6_qm4':15,
              'O11_O11_qm4':16}

def print_interactions():
    return interactions.keys()

def sigma_nucleon_bound(int,mchi,r): 
    mchi_vec=planes[interactions[int]][0]
    r_vec=planes[interactions[int]][1]
    sigma_vec=planes[interactions[int]][2]
    return interpolate.interp2d(mchi_vec, r_vec, sigma_vec)(mchi,r)

