# ИНВЕРТИРОВАНИЕ ДАННЫХ
import os
import numpy as np

# change for 1 if it is old data
cntps = 3

# cntwj = 10000  # change for 10000 if you want to generate all sets

dirData = 'large_not_filteredZXY'
# dirData = 'newdata_filteredZXY'

newDir = os.path.join('.', 'large_nf_InvertZY2')

if not os.path.exists(newDir):
    os.makedirs(newDir)

for nnset in range(1, 2):
    # print(os.path.join('.', newDir, nset + '_Z.dat'))
    # # nset = 'set' + str(nnset)
    nset = 'large_set' + str(nnset)
    wData = np.genfromtxt(os.path.join('.', dirData, (nset + '_W' + '.dat')))
    cntwj = wData.size
    jData = np.genfromtxt(os.path.join('.', dirData, (nset + '_J' + '.dat')))
    iData2 = []
    rData2 = []
    for j in range(cntps):
        iData2.append([])
        rData2.append([])
    iData = []
    rData = []
    for i in range(1, cntps + 1):
        iData.append(np.genfromtxt(os.path.join('.', dirData, (nset + '_Ipsi_' + str(i) + 'ps' + '.dat'))))
        rData.append(np.genfromtxt(os.path.join('.', dirData, (nset + '_Rpsi_' + str(i) + 'ps' + '.dat'))))
    snz10 = []
    sny10 = []
    snx10 = []
    nps = 0
    for i in range(cntwj):
        # zps = []
        # xps = []
        # yps = []
        # for nps in range(cntps):
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
        # zps.append(ssnz)
        # xps.append(ssnx)
        # yps.append(ssny)
        snz10.append(ssnz)
        snx10.append(ssnx)
        sny10.append(ssny)
    # print(np.array(zps))
    # fl = True
    # for j in range(cntps):
    # if (not fl):
    # break
    # for k in range(cntps):
    # for q in range(64):
    # if (abs (zps[j][q] - zps[k][q]) > 0.001):
    # fl = False
    # elif (abs (xps[j][q] - xps[k][q]) > 0.001):
    # fl = False
    # elif (abs (yps[j][q] - yps[k][q]) > 0.001):
    # fl = False
    # if (fl):
    # wData2.append(wData[i])
    # jData2.append(jData[i])
    # for j in range(cntps):
    # rData2[j].append(rData[j][i])
    # iData2[j].append(iData[j][i])

    # print(len(wData2))
    # проверим, что удовлетворяет условию
    print(np.array(snz10).shape)
    np.savetxt(os.path.join('.', newDir, nset + '_Z.dat'), np.array(snz10))
    np.savetxt(os.path.join('.', newDir, nset + '_X.dat'), np.array(snx10))
    np.savetxt(os.path.join('.', newDir, nset + '_Y.dat'), np.array(sny10))
    np.savetxt(os.path.join('.', newDir, nset + '_J.dat'), np.array(jData))
    np.savetxt(os.path.join('.', newDir, nset + '_W.dat'), np.array(wData))
# for j in range(cntps):
# np.savetxt (os.path.join('.', newDir, nset + '_Ipsi_' + str (j + 1) + 'ps.dat'), np.array(iData2[j]))
# np.savetxt (os.path.join('.', newDir, nset + '_Rpsi_' + str (j + 1) + 'ps.dat'), np.array(rData2[j]))