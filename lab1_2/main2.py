import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math

from scipy.stats import norm
from scipy.stats import cauchy
from scipy.stats import t
from scipy.stats import uniform
from scipy.stats import poisson

random_var = norm
def calcGMean(distName, sample_size, param = 0):
    summary = [0, 0]
    for i in range(1000):
        x = []
        if distName == poisson:
            x = distName.rvs(mu=param, size=sample_size)
        elif distName == t:
            x = distName.rvs(df=param, size=sample_size)
        else:
            x = distName.rvs(size=sample_size)
        mean = 0
        for j in x:
            mean += j
        mean = mean / sample_size
        summary[0] += mean
        summary[1] += mean**2
    summary[0] /= 1000
    summary[1] = summary[1]/1000 - (summary[0])**2
    return summary

def calcGMed(distName, sample_size, param = 0):
    summary = [0, 0]
    for i in range(1000):
        x = []
        if distName == poisson:
            x = distName.rvs(mu=param, size=sample_size)
        elif distName == t:
            x = distName.rvs(df=param, size=sample_size)
        else:
            x = distName.rvs(size=sample_size)
        if (sample_size) % 2 != 0:
            med = x[sample_size//2]
        else:
            med = (x[sample_size//2] + x[sample_size//2 - 1]) / 2
        summary[0] += med
        summary[1] += med**2
    summary[0] /= 1000
    summary[1] = summary[1] / 1000 - (summary[0]) ** 2
    return summary

def calcZ_R(distName, sample_size, param = 0):
    summary = [0, 0]
    for i in range(1000):
        x = []
        if distName == poisson:
            x = distName.rvs(mu=param, size=sample_size)
        elif distName == t:
            x = distName.rvs(df=param, size=sample_size)
        else:
            x = distName.rvs(size=sample_size)
        z_R = (x[0] + x[sample_size-1]) / 2
        summary[0] += z_R
    summary[0] /= 1000
    summary[1] = summary[1] / 1000 - (summary[0]) ** 2
    return summary


def calcZ_Q(distName, sample_size, param=0):
    summary = [0, 0]
    for i in range(1000):
        x = []
        if distName == poisson:
            x = distName.rvs(mu=param, size=sample_size)
        elif distName == t:
            x = distName.rvs(df=param, size=sample_size)
        else:
            x = distName.rvs(size=sample_size)
        p_arr = [0.25, 0.75]
        z_p = 0
        z_Q = 0
        for p in p_arr:
            if isinstance(sample_size*p, int):
                z_p = x[sample_size*p-1]
            else:
                z_p = x[int(sample_size*p)]
            z_Q += z_p
        summary[0] += z_Q/2
        summary[1] = (z_Q/2) ** 2
    summary[0] /= 1000
    summary[1] = summary[1] / 1000 - (summary[0]) ** 2
    return summary

def calcZ_tr(distName, sample_size, param = 0):
    r = int(sample_size/4)
    summary = [0, 0]
    for i in range(1000):
        x = []
        if distName == poisson:
            x = distName.rvs(mu=param, size=sample_size)
        elif distName == t:
            x = distName.rvs(df=param, size=sample_size)
        else:
            x = distName.rvs(size=sample_size)
        s = 0
        for i in range(r, sample_size-r-1):
            s += x[i]
        s = 1/(sample_size-2*r)*s
        summary[0] += s
        summary[0] += s**2
    summary[0] /= 1000
    summary[1] = summary[1] / 1000 - (summary[0]) ** 2
    return summary


def output(distName, param=0):
    sample_size = [10, 100, 1000]
    for i in sample_size:
        mean = calcGMean(norm, i, param)
        print("n = ", i, " выборочное среднее E(z) = ", '%.5f' % mean[0])
        print("n = ", i, " выборочное среднее D(z) = ", '%.5f' % mean[1])
        med = calcGMed(norm, i, param)
        print("n = ", i, " медиана E(z) = ", '%.5f' % med[0])
        print("n = ", i, " медиана D(z) = ", '%.5f' % med[1])
        z_R = calcZ_R(norm, i, param)
        print("n = ", i, " полусумма экстремальных выборочных элементов E(z) = ", '%.5f' % z_R[0])
        print("n = ", i, " полусумма экстремальных выборочных элементов D(z) = ", '%.5f' % z_R[1])
        z_Q = calcZ_Q(norm, i, param)
        print("n = ", i, " полусумма квартилей E(z) = ", '%.5f' % z_Q[0])
        print("n = ", i, " полусумма квартилей D(z) = ", '%.5f' % z_Q[1])
        z_tr = calcZ_tr(norm, i, param)
        print("n = ", i, " усечённое среднее E(z) = ", '%.5f' % z_tr[0])
        print("n = ", i, " усечённое среднее D(z) = ", '%.6f' % z_tr[1])
        print('\n')

print("Нормальное распределение (0,1)\n")
output(norm)

print("Распределение Коши(0,1)\n")
output(cauchy)

print("Равномерное распределение (-(3^1/2),(3^1/2))\n")
output(uniform)

print("Распределение Стьюдента(0, 3)\n")
output(t, 3)

print("Распределение Пуассона(5)\n")
output(poisson, 5)







