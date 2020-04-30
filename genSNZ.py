import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.cluster import AgglomerativeClustering, FeatureAgglomeration
from sklearn.manifold import TSNE

root = ''
dirData = root + 'large_resolution/'
newDir = root + 'large_inverted/'
pictureDir = root + 'large_agglomerative_pca_no_60100/'
# pictureDir = root + 'large_agglomerative_pca_params/'

cntps = 3
nset = 1


def gen_snz():
    nset = 'large_set1'
    wData = np.genfromtxt(os.path.join('.', dirData, (nset + '_W' + '.dat')))
    jData = np.genfromtxt(os.path.join('.', dirData, (nset + '_J' + '.dat')))
    cntwj = wData.size
    print(cntwj)

    iData = []
    rData = []
    for i in range(1, cntps + 1):
        iData.append(np.genfromtxt(os.path.join('.', dirData, (nset + '_Ipsi_' + str(i) + 'ps' + '.txt'))))
        rData.append(np.genfromtxt(os.path.join('.', dirData, (nset + '_Rpsi_' + str(i) + 'ps' + '.txt'))))

    for i in range(cntps):
        iData[i] = np.array(iData[i]).transpose().tolist()
        rData[i] = np.array(rData[i]).transpose().tolist()
    print(np.array(iData).shape)

    for nps in range(cntps):
        zps = []
        xps = []
        yps = []
        for i in range(cntwj):
            ssnz = []
            ssnx = []
            ssny = []
            for k in range(0, 128, 2):
                fiPlus = (iData[nps][i][k] ** 2 + rData[nps][i][k] ** 2) ** 0.5
                fiMinus = (iData[nps][i][k + 1] ** 2 + rData[nps][i][k + 1] ** 2) ** 0.5
                snzi = (fiPlus ** 2 - fiMinus ** 2) / (fiPlus ** 2 + fiMinus ** 2)
                ssnz.append(snzi)
                snzi = (-2 * (rData[nps][i][k + 1] * iData[nps][i][k] - iData[nps][i][k + 1] * rData[nps][i][k])) / (
                        fiPlus ** 2 + fiMinus ** 2)
                ssny.append(snzi)
                snzi = (2 * (iData[nps][i][k + 1] * iData[nps][i][k] + rData[nps][i][k + 1] * rData[nps][i][k])) / (
                        fiPlus ** 2 + fiMinus ** 2)
                ssnx.append(snzi)
            if (ssnz[0] < 0):
                ssnz = list(- np.array(ssnz))
                ssny = list(- np.array(ssny))
            zps.append(ssnz)
            xps.append(ssnx)
            yps.append(ssny)
        np.savetxt(newDir + nset + '_Zpsi_' + str(nps + 1) + 'ps.dat', np.array(zps))
        np.savetxt(newDir + nset + '_Ypsi_' + str(nps + 1) + 'ps.dat', np.array(yps))
        np.savetxt(newDir + nset + '_Xpsi_' + str(nps + 1) + 'ps.dat', np.array(xps))
        np.savetxt(newDir + nset + '_J.dat', np.array(jData))
        np.savetxt(newDir + nset + '_W.dat', np.array(wData))


# nset = 'large_set1'
# wData = np.genfromtxt(newDir + nset + '_W.dat')
# jData = np.genfromtxt(newDir + nset + '_J.dat')
# zData = np.genfromtxt(newDir + nset + '_Zpsi_1ps.dat')
# xData = np.genfromtxt(newDir + nset + '_Xpsi_1ps.dat')
# yData = np.genfromtxt(newDir + nset + '_Ypsi_1ps.dat')
#
# cntwj = len(wData)

gen_snz()


def agf(linkage, n_cl, type, affinity, X, X_reduced):
    aggl = AgglomerativeClustering(n_clusters=n_cl, linkage=linkage, affinity=affinity)
    aggl.fit(X_reduced)
    label = aggl.labels_
    plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=label,
                edgecolor='none', alpha=0.7, s=5,
                cmap=plt.cm.nipy_spectral)
    plt.axis('off')
    plt.savefig(os.path.join(pictureDir, "on_tsne" + nset + linkage + '_' + affinity + '_' + type + '_ncluster=' + str(
        n_cl) + '.png'))
    plt.show()
    plt.close()
    # plt.new
    plt.xlabel("J (коэффициент связи между ячейками)")
    plt.ylabel("W (параметр накачки)")
    plt.scatter(jData1, wData1, s=5, c=label,
                edgecolor='none',
                cmap=plt.cm.nipy_spectral)

    plt.savefig(os.path.join(pictureDir,
                             "after_tsne" + nset + linkage + '_' + affinity + '_' + type + '_ncluster=' + str(
                                 n_cl) + '.png'))
    # plt.savefig(
    plt.show()
    plt.close()

    aggl = AgglomerativeClustering(n_clusters=n_cl, linkage=linkage, affinity=affinity)
    aggl.fit(X)
    label = aggl.labels_
    plt.xlabel = 'J (коэффициент связи между ячейками)'
    plt.ylabel = 'W (параметр накачки)'
    plt.scatter(jData1, wData1, s=5, c=label,
                edgecolor='none',
                cmap=plt.cm.nipy_spectral)

    plt.savefig(os.path.join(pictureDir,
                             "raw" + nset + linkage + '_' + affinity + '_' + type + '_ncluster=' + str(n_cl) + '.png'))
    plt.show()
    plt.close()


def genAll(type, X, X_reduced):
    print(type)
    for (link, dist) in types:
        for n_cl in range(5, 6):
            agf(link, n_cl, type, dist, X, X_reduced)
        # agf ('complete', n_cl, type)
        # agf ('average', n_cl, type)
        # agf ('single', n_cl, type)
    print(type + 'finished')


nset = 'large_set1'
wData = np.genfromtxt(newDir + nset + '_W.dat')
jData = np.genfromtxt(newDir + nset + '_J.dat')
zData = np.genfromtxt(newDir + nset + '_Zpsi_1ps.dat')
xData = np.genfromtxt(newDir + nset + '_Xpsi_1ps.dat')
yData = np.genfromtxt(newDir + nset + '_Ypsi_1ps.dat')

cntwj = len(wData)


def read_data(minj, maxj, minw, maxw):
    resind = []
    for i in range(cntwj):
        if ((minw < wData[i] < maxw) and (minj < jData[i] < maxj)):
            resind.append(i)
    return (np.array(resind))


# jmin, jmax, wmin, wmax = 0, 1, 0, 1
# ind = read_data(jmin, jmax, wmin, wmax)
# print(ind)
# name = "j=" + str(jmin) + "-" + str(jmax) + "_w=" + str(wmin) + "-" + str(wmax) + "_"
# print(name)
# print(len(ind))


# без прореживания
snx10 = xData
sny10 = yData
snz10 = zData
jData1 = jData
wData1 = wData

types = [(link, dist)
         for link in ['average', 'complete', 'single']
         for dist in ['euclidean', 'manhattan', 'cosine']]
types.append(('ward', 'euclidean'))
print(types)
