import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.cluster import AgglomerativeClustering, FeatureAgglomeration
from sklearn.manifold import TSNE

root = './'
# dirData = root + 'large_resolution/'
newDir = root + 'large_nf_InvertZY2/'
pictureDir = root + 'large_aggl_new_not_filtered_part/'
# pictureDir = root + 'large_agglomerative_pca_params/'
if not os.path.exists(pictureDir):
    os.makedirs(pictureDir)

cntps = 3

types = []
types.append(('ward', 'euclidean'))
print(types)

nset = 'large_set1'
wData = np.genfromtxt(newDir + nset + '_W.dat')
jData = np.genfromtxt(newDir + nset + '_J.dat')
zData = np.genfromtxt(newDir + nset + '_Z.dat')
xData = np.genfromtxt(newDir + nset + '_X.dat')
yData = np.genfromtxt(newDir + nset + '_Y.dat')

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

jmin, jmax, wmin, wmax = 0, 0.5, 1.5, 4
ind = read_data(jmin, jmax, wmin, wmax)
wData1 = wData[ind]
jData1 = jData[ind]
snz10 = zData[ind]
snx10 = xData[ind]
sny10 = yData[ind]

cntwj1 = len(wData1)


def agf(linkage, n_cl, type, affinity, X, X_reduced):
    # aggl = AgglomerativeClustering(n_clusters=n_cl, linkage=linkage, affinity=affinity)
    # aggl.fit(X_reduced)
    # label = aggl.labels_
    # plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=label,
    #             edgecolor='none', alpha=0.7, s=5,
    #             cmap=plt.cm.nipy_spectral)
    # plt.axis('off')
    # plt.savefig(os.path.join(pictureDir, "on_tsne" + nset + linkage + '_' + affinity + '_' + type + '_ncluster=' + str(
    #     n_cl) + '.png'))
    # plt.show()
    # plt.close()
    # # plt.new
    # plt.xlabel("J (коэффициент связи между ячейками)")
    # plt.ylabel("W (параметр накачки)")
    # # plt.xlabel('Leprechauns')
    # # plt.ylabel('Gold')
    # # plt.legend(loc='upper left')
    # plt.scatter(jData1, wData1, s=5, c=label,
    #             edgecolor='none',
    #             cmap=plt.cm.nipy_spectral)

    # plt.savefig(os.path.join(pictureDir,
    #                          "after_tsne" + nset + linkage + '_' + affinity + '_' + type + '_ncluster=' + str(
    #                              n_cl) + '.png'))
    # # plt.savefig(
    # plt.show()
    # plt.close()

    aggl = AgglomerativeClustering(n_clusters=n_cl, linkage=linkage, affinity=affinity)
    aggl.fit(X)
    label = aggl.labels_
    print(label)
    # print(np.max(label))
    plt.xlabel("J (коэффициент связи между ячейками)")
    plt.ylabel("W (параметр накачки)")
    plt.scatter(jData1, wData1, s=5, c=label,
                edgecolor='none',
                cmap='inferno', vmin=1, vmax=(n_cl))

    plt.savefig(os.path.join(pictureDir,
                             "raw" + nset + linkage + '_' + affinity + '_' + type + '_ncluster=' + str(n_cl) + '.png'))
    plt.show()
    plt.close()
    plt.xlabel("J (коэффициент связи между ячейками)")
    plt.ylabel("W (параметр накачки)")
    plt.scatter(jData1, wData1, s=5, c=label,
                edgecolor='none',
                cmap='tab10', vmin=1, vmax=(n_cl))

    plt.savefig(os.path.join(pictureDir,
                             "raw2" + nset + linkage + '_' + affinity + '_' + type + '_ncluster=' + str(n_cl) + '.png'))
    plt.show()
    plt.close()
    plt.show()
    plt.close()
    plt.xlabel("J (коэффициент связи между ячейками)")
    plt.ylabel("W (параметр накачки)")
    plt.scatter(jData1, wData1, s=5, c=label,
                edgecolor='none',
                cmap='tab10', vmin=0, vmax=(n_cl - 1))

    plt.savefig(os.path.join(pictureDir,
                             "raw3" + nset + linkage + '_' + affinity + '_' + type + '_ncluster=' + str(n_cl) + '.png'))
    plt.show()
    plt.close()

    plt.show()
    plt.close()
    plt.show()
    plt.close()
    plt.xlabel("J (коэффициент связи между ячейками)")
    plt.ylabel("W (параметр накачки)")
    plt.scatter(jData1, wData1, s=5, c=label,
                edgecolor='none',
                cmap='tab10')

    plt.savefig(os.path.join(pictureDir,
                             "raw4" + nset + linkage + '_' + affinity + '_' + type + '_ncluster=' + str(n_cl) + '.png'))
    plt.show()
    plt.close()


def genAll(type, X, X_reduced):
    print(type)
    for (link, dist) in types:
        for n_cl in range(3, 5):
            agf(link, n_cl, type, dist, X, X_reduced)
        # agf ('complete', n_cl, type)
        # agf ('average', n_cl, type)
        # agf ('single', n_cl, type)
    print(type + 'finished')


from sklearn.decomposition import PCA


def gen_with_pca(pcan, p1, p2, p3, p4, name, X):
    pca = PCA(n_components=pcan)
    X_pca = pca.fit_transform(X)
    # print(X_reduced.shape)
    tsne = TSNE(n_components=2, learning_rate=p1, perplexity=p2, n_iter=p3,
                n_iter_without_progress=p4)  # change for the best
    X_reduced = tsne.fit_transform(X_pca)
    #  tsne.fit_transform(X_pca)
    genAll(name + str(pcan) + '_less', X_pca, X_reduced)


X = []
for ii in range(cntwj1):
    X.append(snx10[ii] + sny10[ii] + snz10[ii])
X = np.array(X)
# gen_with_pca(10, 200, 70, 1000, 500, 'xyz', X)
# gen_with_pca(25, 200, 70, 1000, 500, 'xyz', X)
# gen_with_pca(3, 200, 70, 1000, 500, 'xyz', X)
gen_with_pca(10, 80, 70, 1000, 500, 'xyz', X)
gen_with_pca(25, 80, 70, 1000, 500, 'xyz', X)
gen_with_pca(5, 80, 70, 1000, 500, 'xyz', X)
