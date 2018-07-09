import matplotlib.pyplot as plt
import numpy as np
import random

def powerGraph():
    y = np.arange(0,100)
    prayud = []
    somsri = []
    for i in y:
        tmp = i * 0.8
        if tmp % 3 == 0:
            tmp *= 1.2
        if tmp % 4 == 0:
            tmp *= 2
        prayud.append(tmp)

        tmp = i * 0.6
        if tmp % 4 == 0:
            tmp *= 1.1
        if tmp % 7 == 0:
            tmp *= 0.5
        if tmp % 6 == 0:
            tmp *= 2.5
        somsri.append(tmp)


    plt.plot(y,somsri,'-', label='Grandma Somsri')
    plt.plot(y,prayud, '-', label='Grandpa Prayud')
    plt.title("Power Graph")
    plt.xlabel('100 %')
    plt.ylabel('Power')

    plt.legend()

    plt.show()

powerGraph()