import numpy as np
import matplotlib.pyplot as plt
import os

cntps = 3
# в первом 4205
# cntwj = 10000  # change for 10000 if you want to generate all sets
# nset = 'set' + input('Choose the number of set (1..10)\n')
# dirData = 'dataFilterZXY'
# C:\Users\Asus\Desktop\science\data_for_ML\code\
# dirData = 'new_dataFilterZXY'
dirData = 'large_not_filteredZXY'
# dirData = 'large_resolution'
is_large = False
do_prorezh = True


for numbset in range(1, 2):
    # nset = 'set' + str(numbset)
    nset =  'large_set' + str(numbset)
    print(nset)
    newDir = os.path.join('.', 'large_pictures_skip', nset)
    # newDir = os.path.join('.', 'good_pictures', nset)
    # newDir = os.path.join('.', 'dataFilterZXY_illustrations', nset)

    if not os.path.exists(newDir):
        os.makedirs(newDir)

    wData = np.genfromtxt(os.path.join('.', dirData, (nset + '_W' + '.dat')))
    jData = np.genfromtxt(os.path.join('.', dirData, (nset + '_J' + '.dat')))
    iData = []
    rData = []

    cntwj = wData.size
    # cntwj = 10
    # cntwj = 10
    print(cntwj)
    snz10 = []
    if (not is_large):

        for i in range(1, cntps + 1):
            iData.append(np.genfromtxt(os.path.join('.', dirData, (nset + '_Ipsi_' + str(i) + 'ps' + '.dat'))))
            # iData.append(np.genfromtxt(os.path.join('.', dirData, (nset + '_Ipsi_' + str(i) + 'ps' + '.txt'))))
            rData.append(np.genfromtxt(os.path.join('.', dirData, (nset + '_Rpsi_' + str(i) + 'ps' + '.dat'))))
            # rData.append(np.genfromtxt(os.path.join('.', dirData, (nset + '_Rpsi_' + str(i) + 'ps' + '.txt'))))
        # print(rData[0])
        print(len(iData))
        print(iData[0].shape)
        print(len(rData))
        print(rData[0].shape)

        snz10 = []
        for nps in range(cntps):
            snz = []
            for i in range(cntwj):
                ssnz = []
                for k in range(0, 128, 2):
                    # print(nps, i, k)
                    fiPlus = (iData[nps][i][k] ** 2 + rData[nps][i][k] ** 2) ** 0.5
                    fiMinus = (iData[nps][i][k + 1] ** 2 + rData[nps][i][k + 1] ** 2) ** 0.5
                    snzi = (fiPlus ** 2 - fiMinus ** 2) / (fiPlus ** 2 + fiMinus ** 2)
                    ssnz.append(snzi)
                snz.append(ssnz)
            snz10.append(snz)

    else:
        snz10.append(np.genfromtxt(os.path.join('.', dirData, (nset + '_Zpsi_1ps' + '.dat'))))
        snz10.append(np.genfromtxt(os.path.join('.', dirData, (nset + '_Zpsi_2ps' + '.dat'))))
        snz10.append(np.genfromtxt(os.path.join('.', dirData, (nset + '_Zpsi_3ps' + '.dat'))))

    print("finish read")
    setni = []
    if (do_prorezh):
        zData = snz10.copy()
        print("prorezhivanie")
        i = 0
        j = 0
        snz10 = []
        for ps in range(3):
            snz10.append([])
        print(snz)
        jData1 = []
        wData1 = []

        for cur in range(397 * 397):
            if (i % 20 == 0 and j % 20 == 0):
                # print(cur)
                zz = []
                for ps in range(3):
                    print(zData[ps][cur])
                    snz10[ps].append(zData[ps][cur])
                    # zz.append()
                jData1.append(jData[cur])
                wData1.append(wData[cur])
                setni.append(cur + 1)
            j = (j + 1) % 397
            if ((cur + 1) % 397 == 0):
                i += 1
        print("finish prorezh")
        wData = wData1.copy()
        jData = jData1.copy()
    else:
        setni = [i for i in range(1, cntwj + 1)]
    cntwj = len(wData)
    print(cntwj)
    print(len(snz10))
    print(len(snz10[0]))
    print(len(snz10[0][0]))
    # print(snz10[0].shape)
    xar = np.arange(1, cntps + 1, 1)
    yy = []
    xx = []
    for i in range(1, 9):
        for j in range(1, 9):
            xx.append(i)
            yy.append(j)
    for jwk in range(cntwj):
        # if (cntwj < 5400)
        # for jwk in range(10):
        WJDir = os.path.join(newDir, str(setni[jwk]))
        print(jwk, setni[jwk])
        # WJDir = newDir

        if not os.path.exists(WJDir):
            os.makedirs(WJDir)

        yar = []
        for j in range(64):
            jar = []
            for i in range(cntps):
                jar.append(snz10[i][jwk][j])
            yar.append(np.array(jar))
        # 10 pictures plotting
        for i in range(cntps):
            plt.figure()
            plt.scatter(xx, yy, c=snz10[i][jwk], s=500, cmap='inferno', vmin=-1, vmax=1)
            plt.colorbar()
            plt.axis('off')
            plt.savefig(os.path.join(WJDir, ('plot_wj' + str(setni[jwk]) + '_' + str(i + 1) + 'ps' + '.png')))
            plt.close()
        # todo почему меняется точность???
        plt.figure()
        plt.title('J = ' + str(jData[jwk]) + ', W = ' + str(wData[jwk]))
        plt.xlabel('t(ps)')
        plt.ylabel('Snz')
        plt.ylim(-1, 1)
        for j in range(64):
            plt.plot(xar, yar[j], c='black')
        plt.savefig(os.path.join(WJDir, ('plot_wj' + str(jwk + 1) + '.png')))
        plt.close()