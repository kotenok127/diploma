import os
import numpy as np
# import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import matplotlib.patches as mpatches

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

phases['af'] = [103221, 103241, 111161, 111181, 119101, 119121, 119141, 119161,
                127041, 127061, 134981, 135001, 135021, 142921, 142941, 150861,
                150881, 63541, 71481, 79421, 87341, 87361, 95281, 95301,
                95321]

phases['random'] = [1, 101, 15881, 15901, 15921, 21, 23821, 41, 55621,
                    61, 63561, 7941, 7961, 7981, 8001, 8021, 81]

# phases['vert'] = [103341, 111261, 135101, 150961, 281, 39801, 39841, 47741,
#                   47781, 55721, 71561, 79461, 79501, 87461]
# phases['hor'] = [103321, 111281, 119201, 119221, 127141, 127161, 135081, 143021,
#                  143041, 150941, 150981, 301, 31881, 321, 341, 361,
#                  39821, 47761, 55681, 55701, 63621, 63641, 71581, 79521,
#                  8241, 8261, 8281, 87441, 95381, 95401]

phases['hor_vert_dom'] = [281] + [301, 321, 341, 361, 8241, 8261, 8281]
phases['hor_vert_af'] = [103341, 111261, 135101, 150961, 39801, 39841, 47741,
                         47781, 55721, 71561, 79461, 79501, 87461] + \
                        [103321, 111281, 119201, 119221, 127141, 127161,
                         135081, 143021, 143041, 150941, 150981, 31881,
                         39821, 47761, 55681, 55701, 63621, 63641, 71581, 79521,
                         87441, 95381, 95401]

phases['diag'] = [16061, 16081, 16101, 16121, 23981, 24001, 24021, 24041, 24061,
                  24081, 31921, 31941, 31961, 31981, 32001, 32021, 39861, 39881, 39901, 39921, 39941, 47841, 47861,
                  55781, 55801, 63761, 8161, 8181]

# phases['wave'] = [111241, 119181, 127121, 135061, 143001,  16141,  16161,  16181,
#         16201,  16221,  24101,  24121,  24141,  24161,  31901,  32121,
#         47801,  47821,  55661,  55741,  55761,  71621,   8201,   8221,
#         87401]
# phases['domens'] = [32041, 47721, 47881, 63721, 71641]


phases['domen_waves'] = [111241, 119181, 127121, 135061, 143001, 16141, 16161, 16181,
                         16201, 16221, 24101, 24121, 24141, 24161, 31901, 32121,
                         47801, 47821, 55661, 55741, 55761, 71621, 8201, 8221,
                         87401] + [32041, 47721, 47881, 63721, 71641]

phases['squares'] = [103261, 103281, 103301, 111201, 111221, 127081, 127101, 135041,
                     142961, 142981, 150901, 150921, 63581, 63601, 71501, 71521,
                     71541, 79441, 79481, 87381, 87421, 95341, 95361]

colors_phase = {'zero': 'purple',
                'fm': 'yellow',
                'af': 'red',
                'random': 'grey',
                # 'vert': 'blue',
                # 'hor': 'green',
                'diag': 'orange',
                # 'wave': 'brown',
                'domen_waves': 'green',
                'hor_vert_dom': 'brown',
                'hor_vert_af': 'blue',
                # 'domens': 'darkblue',
                'squares': 'lime'
                }



dirData = 'large_nf_InvertZY2'
# newDir = os.path.join('.', 'large_tsne_paramsInvert')
newDir = os.path.join('.', 'large_nf_good_tsne_phases')
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
# sny10 = np.genfromtxt(os.path.join('.', dirData, (nset + '_Y' + '.dat')))

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
set_dict = {}

for cur in range(397 * 397):
    if (i % 4 == 0 and j % 4 == 0):
        snx10.append(xData[cur])
        sny10.append(yData[cur])
        snz10.append(zData[cur])
        jData1.append(jData[cur])
        wData1.append(wData[cur])
        setni.append(cur + 1)
        set_dict[cur + 1] = len(jData1) - 1
    j = (j + 1) % 397
    if ((cur + 1) % 397 == 0):
        i += 1

jData = jData1.copy()
wData = wData1.copy()

print(set_dict)

cntwj = len(wData)
print(cntwj)


def tsne_dots(name, dots):
    tsne = TSNE(n_components=2, learning_rate=lr, perplexity=perp, n_iter=n_i,
                n_iter_without_progress=n_iwp)
    X_reduced = tsne.fit_transform(XX)
    plt.figure()
    myc = wData.copy()
    mys = jData.copy()
    for i in dots:
        mys[set_dict[i]] = 100

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
    for i in dots:
        mys[set_dict[i]] = 100
        # mys[(i - 1)] = 100

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


label = ['grey' for i in range(cntwj)]
# label = np.zeros(cntwj)
# cur_col = 0
for f_name in phases.keys():
    # cur_col += 1
    cur_col = colors_phase.get(f_name)
    f_values = phases.get(f_name)
    print(f_name, cur_col)
    # print(f_values)
    # cncn += len(f_values)
    for i in f_values:
        label[set_dict[i]] = cur_col


def run_all_phases(suf):
    tsne = TSNE(n_components=2, learning_rate=lr, perplexity=perp, n_iter=n_i,
                n_iter_without_progress=n_iwp)
    X_reduced = tsne.fit_transform(XX)

    fig, ax = plt.subplots()

    # plt.figure()
    mys = np.zeros(cntwj)
    print(label)
    for i in range(cntwj):
        if (label[i] == 'grey'):
            mys[i] = 1
        else:
            mys[i] = 10

    scatter = ax.scatter(X_reduced[:, 0], X_reduced[:, 1], c=label,
                edgecolor='none', alpha=0.7, s=mys)
    # cmap='rainbow', vmin=0, vmax=10)
    # plt.colorbar()
    patches = [mpatches.Patch(color=colors_phase[phase], label=phase) for phase in colors_phase.keys()]

    plt.legend(handles=patches)


    plt.savefig(os.path.join(newDir, (
            'all_colored' +
            suf +
            # '_color=j' +
            '_lr=' + str(lr) +
            '_perp=' + str(perp) +
            '_n_i=' + str(n_i) +
            '_n_iwp=' + str(n_iwp) +
            'nset' + '.png')))
    # plt.savefig(os.path.join(newDir, ('tsneXYZ_color=j' +nset+'_'+ str(pps + 1) + 'ps.png')))
    # plt.show()
    plt.close()

    # legend[set_dict[i]] = f_name

def run_no_leg(suf):
    tsne = TSNE(n_components=2, learning_rate=lr, perplexity=perp, n_iter=n_i,
                n_iter_without_progress=n_iwp)
    X_reduced = tsne.fit_transform(XX)

    fig, ax = plt.subplots()
    mys = np.zeros(cntwj)
    print(label)
    for i in range(cntwj):
        if (label[i] == 'grey'):
            mys[i] = 1
        else:
            mys[i] = 10


    ax.scatter(X_reduced[:, 0], X_reduced[:, 1], c=label,
                edgecolor='none', alpha=0.7, s=mys)


    plt.savefig(os.path.join(newDir, (
            'all_colored' +
            suf +
            # '_color=j' +
            '_lr=' + str(lr) +
            '_perp=' + str(perp) +
            '_n_i=' + str(n_i) +
            '_n_iwp=' + str(n_iwp) +
            'nset' + '.png')))
    # plt.savefig(os.path.join(newDir, ('tsneXYZ_color=j' +nset+'_'+ str(pps + 1) + 'ps.png')))
    # plt.show()
    plt.close()



def run_phases(suf):
    for f_name in phases.keys():
        f_values = phases.get(f_name)
        print(f_name)
        print(f_values)
        tsne_dots(f_name + suf, f_values)


n_iwp = 500
n_i = 1000
lr = 0
perp = 0


def gen_all():
    global lr
    global perp
    global XX
    XX = []
    for ii in range(cntwj):
        XX.append(snx10[ii] + sny10[ii] + snz10[ii])

    for (lr, perp) in [(80, 70), (200, 100)]:
        # run_phases("_xyz")
        run_no_leg("_no_leg1_xyz")

    # XX = []
    # for ii in range(cntwj):
    #     XX.append(snx10[ii] + sny10[ii])
    #
    # for (lr, perp) in [(160, 70), (140, 50)]:
    #     run_phases("_xy")

    # XX = []
    # for ii in range(cntwj):
    #     XX.append(snz10[ii])
    #
    # for (lr, perp) in [(200, 70), (100, 70)]:
    #     run_all_phases("_z")
    #     # run_all_phases("_z_white")


gen_all()
