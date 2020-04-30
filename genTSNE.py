import os
import numpy as np
# import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

phases = {}
phases['zero'] = [121, 141, 161, 181, 201, 221, 241, 261, 8041, 8061, 8081, 8101, 8121, 8141,
                  15941, 15961, 15981, 16001, 16021, 16041] + [i for i in range(23841, 23981, 20)] + \
                 [i for i in range(31761, 31881, 20)] + \
                 [i for i in range(39701, 39782, 20)] + \
                 [i for i in range(47641, 47702, 20)] + \
                 [55581, 55601, 55641, 63521, 71461, 79401]

phases['fm'] = [103361, 103381, 103401, 103421, 103441, 103461, 103481, 103501,
                103521, 103541, 103561, 103581, 103601, 111301, 111321, 111341,
                111361, 111381, 111401, 111421, 111441, 111461, 111481, 111501,
                111521, 111541, 119241, 119261, 119281, 119301, 119321, 119341,
                119361, 119381, 119401, 119421, 119441, 119461, 119481, 127181,
                127201, 127221, 127241, 127261, 127281, 127301, 127321, 127341,
                127361, 127381, 127401, 127421, 135121, 135141, 135161, 135181,
                135201, 135221, 135241, 135261, 135281, 135301, 135321, 135341,
                135361, 143061, 143081, 143101, 143121, 143141, 143161, 143181,
                143201, 143221, 143241, 143261, 143281, 143301, 151001, 151021,
                151041, 151061, 151081, 151101, 151121, 151141, 151161, 151181,
                151201, 151221, 151241, 16241, 16261, 24181, 24201, 32061,
                32081, 32101, 32141, 381, 39961, 39981, 40001, 40021,
                40041, 40061, 40081, 47901, 47921, 47941, 47961, 47981,
                48001, 48021, 55821, 55841, 55861, 55881, 55901, 55921,
                55941, 55961, 63661, 63681, 63701, 63741, 63781, 63801,
                63821, 63841, 63861, 63881, 63901, 71601, 71661, 71681,
                71701, 71721, 71741, 71761, 71781, 71801, 71821, 71841,
                79541, 79561, 79581, 79601, 79621, 79641, 79661, 79681,
                79701, 79721, 79741, 79761, 79781, 8301, 8321, 87481,
                87501, 87521, 87541, 87561, 87581, 87601, 87621, 87641,
                87661, 87681, 87701, 87721, 95421, 95441, 95461, 95481,
                95501, 95521, 95541, 95561, 95581, 95601, 95621, 95641,
                95661]
# dirData = 'new_dataInvertZ'
# dirData = 'newdata2_InvertZY'

# newDir = os.path.join('.', 'newdata2_tsne_paramsInvert_types')


dirData = 'large_nf_InvertZY2'
# newDir = os.path.join('.', 'large_tsne_paramsInvert')
newDir = os.path.join('.', 'large_nf_tsne_paramsInvert')
nset = 'large_set1'

if not os.path.exists(newDir):
    os.makedirs(newDir)
# nset = 'set1'

# nset = 'set' + str(nnset)
wData = np.genfromtxt(os.path.join('.', dirData, (nset + '_W' + '.dat')))
cntwj = wData.size
jData = np.genfromtxt(os.path.join('.', dirData, (nset + '_J' + '.dat')))
snz10 = np.genfromtxt(os.path.join('.', dirData, (nset + '_Z' + '.dat')))
snx10 = np.genfromtxt(os.path.join('.', dirData, (nset + '_X' + '.dat')))
sny10 = np.genfromtxt(os.path.join('.', dirData, (nset + '_Y' + '.dat')))

print(snx10.shape)

i = 0
j = 0
xData = snx10.copy()
yData = sny10.copy()
zData = snz10.copy()

snx10 = []
sny10 = []
snz10 = []
jData1 = []
wData1 = []
setni = []
for cur in range(397*397):
  if (i%4 == 0 and j % 4 == 0):
    snx10.append(xData[cur])
    sny10.append(yData[cur])
    snz10.append(zData[cur])
    jData1.append(jData[cur])
    wData1.append(wData[cur])
    setni.append(cur + 1)
  j = (j + 1) % 397
  if ((cur + 1) % 397 == 0):
    i += 1

jData = jData1.copy()
wData = wData1.copy()

cntwj = len(wData)
print(cntwj)

def invertTSNE(name, X):
    # for n_i in range(1000, 5000, 500):
    for n_i in range(1000, 1001, 500):
        print("n_i")
        for n_iwp in range(500, 501, 100):
        # for n_iwp in range(500, 900, 100):
            print("n_iwp")
            for perp in range(70, 30, -20):
                print("perp", perp)
                for lr in range(200, 100, -20):
                    print("lr", lr)
                    tsne = TSNE(n_components=2, learning_rate=lr, perplexity=perp, n_iter=n_i,
                                n_iter_without_progress=n_iwp)
                    X_reduced = tsne.fit_transform(X)

                    plt.figure()
                    myc = wData.copy()
                    mys = jData.copy()



                    plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=myc,
                                edgecolor='none', alpha=0.7, s=mys,
                                cmap=plt.cm.get_cmap('nipy_spectral', 10))
                    # print("ok")
                    plt.colorbar()
                    plt.savefig(os.path.join(newDir, (
                            name +
                            '_color=w' +
                            '_lr=' + str(lr) +
                            '_perp=' + str(perp) +
                            '_n_i=' + str(n_i) +
                            '_n_iwp=' + str(n_iwp) +
                            'nset' + '.png')))
                    # plt.show()
                    plt.close()

                    plt.figure()

                    myc = jData.copy()
                    mys = wData.copy()

                    plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=myc,
                                edgecolor='none', alpha=0.7, s=mys,
                                cmap=plt.cm.get_cmap('nipy_spectral', 10))
                    # print("ok2")

                    plt.colorbar()
                    plt.savefig(os.path.join(newDir, (
                            name +
                            '_color=j' +
                            '_lr=' + str(lr) +
                            '_perp=' + str(perp) +
                            '_n_i=' + str(n_i) +
                            '_n_iwp=' + str(n_iwp) +
                            'nset' + '.png')))
                    # plt.savefig(os.path.join(newDir, ('tsneXYZ_color=j' +nset+'_'+ str(pps + 1) + 'ps.png')))
                    # # plt.show()
                    plt.close()

# XX = []
# for ii in range(cntwj):
#     XX.append(snz10[ii])
# print('tsneZ')
# invertTSNE('tsneZ', XX)
# print('tsneZ finished')



# XX = []
# for ii in range(cntwj):
#     XX.append(snx10[ii] + sny10[ii])
# print('tsneXY')
# invertTSNE('tsneXY', XX)
# print('tsneXY finished')

XX = []
for ii in range(cntwj):
    XX.append(snx10[ii] + sny10[ii] + snz10[ii])
print('tsneXYZ')
invertTSNE('tsneXYZ', XX)
print('tsneXYZ finished')

#
# XX = []
# for ii in range(cntwj):
#     XX.append(snx10[ii])
# print('tsneX')
# invertTSNE('tsneX', XX)
# print('tsneX finished')

# while (True):
# perp = input ('perplexity')
# lr = input('learning_rate')
# n_i = input ('n_iter')
# n_iwp = input ('n_iter_without_progress')

# if (not lr):
# lr = 200
# else:
# lr = int(lr)
# if (not perp):
# perp = 30
# else:
# perp = int(perp)
# if (not n_i):
# n_i = 1000
# else:
# n_i = int(n_i)
# if (not n_iwp):
# n_iwp = 300
# else:
# n_iwp = int(n_iwp)

# print (perp)
# print (lr)
# print (n_i)
# print (n_iwp)
# print ('tsne in progress')
