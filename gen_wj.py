import numpy as np
import os

dirData = 'large_resolution'

w = np.arange(0.4, 4.0000000000000001, 0.009068010076).repeat(397)
# w = np.arange(0.4, 4.001, 0.0363636).repeat(100)
print(w.shape)
# print (w)


j1 = np.arange(0.024, 2.40001, 0.006).tolist()
# j1 = np.arange(0.024, 2.40001, 0.024).tolist()
# print (j1.shape)
j = []
# for i in range (100):
for i in range(397):
    j.append(j1)
print(len(j))
for nnset in range(1, 11):
    nset = 'large_set' + str(nnset)
    # np.savetxt (os.path.join('.', dirData, nset + '_J.dat'), np.array(j).reshape(10000))
    np.savetxt(os.path.join('.', dirData, nset + '_J.dat'), np.array(j).reshape(157609))
    np.savetxt(os.path.join('.', dirData, nset + '_W.dat'), w)
# print (j)
