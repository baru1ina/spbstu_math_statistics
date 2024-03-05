import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import scipy.stats as stats
import math
import random

from scipy.stats import norm, cauchy, t, uniform, poisson, kurtosis

# Мощность выборки
sample_size1 = 20
sample_size2 = 100


def boxplot_t(distName, param=0):
     if distName == poisson:
          x20 = pd.Series(distName.rvs(mu=param, size=sample_size1))
          x100 = pd.Series(distName.rvs(mu=param, size=sample_size2))
          name = "Poisson distribution"
     elif distName == t:
          x20 = pd.Series(distName.rvs(df=param, size=sample_size1))
          x100 = pd.Series(distName.rvs(df=param, size=sample_size2))
          name = "Student's distribution"
     elif distName == uniform:
          x20 = pd.Series(distName.rvs(loc=-np.sqrt(3), scale=2*np.sqrt(3), size=sample_size1))
          x100 = pd.Series(distName.rvs(loc=-np.sqrt(3), scale=2*np.sqrt(3), size=sample_size2))
          name = "Uniform distribution"
     elif distName == "random_dist":
         name = "Random distribution"
         x20 = np.random.random(sample_size1)
         x100 = np.random.random(sample_size2)
     else:
          x20 = pd.Series(distName.rvs(size=sample_size1))
          x100 = pd.Series(distName.rvs(size=sample_size2))
          if distName == norm:
               name = "Normal distribution"
          else:
               name = "Cauchy distribution"

     if distName != "random_dist":
          d = {'20': x20,
               '100': x100}
          df = pd.DataFrame(d)

          sns.boxplot(data=df, flierprops={"marker": "o"}, orient="h", color='darkgrey')
          plt.title(name)
          plt.ylabel('n')
          plt.xlabel('x')
          plt.show()

     sizes = [sample_size1, sample_size2]

     # distribs = [x20.sort_values(ascending=True), x100.sort_values(ascending=True)]
     distribs = [x20, x100]

     # print(distribs)

     mu_bounds = []
     sigma_bounds = []

     ts = [2.09, 1.98]
     quantils = [8.91, 74.22, 32.9, 129.6]  # табличные значения

     if distName == norm:
         for i in range(len(sizes)):
             print("n = ", sizes[i])

             mean = np.mean(distribs[i])
             std = np.std(distribs[i])
             t_alpha = ts[i]

             left_bound_m = mean - ((std * t_alpha) / np.sqrt(sizes[i] - 1))
             right_bound_m = mean + ((std * t_alpha) / np.sqrt(sizes[i] - 1))

             mu_bounds.append(left_bound_m)
             mu_bounds.append(right_bound_m)

             print(left_bound_m, " < m < ", right_bound_m, "\n")

             left_bound_s = (np.sqrt(sizes[i]) * std) / np.sqrt(quantils[i + 2])
             right_bound_s = (np.sqrt(sizes[i]) * std) / np.sqrt(quantils[i])

             sigma_bounds.append(left_bound_s)
             sigma_bounds.append(right_bound_s)

             print(left_bound_s, " < σ < ", right_bound_s, "\n")

     else:
         for i in range(len(sizes)):
             print("n = ", sizes[i])
             mean = np.mean(distribs[i])
             std = np.std(distribs[i])
             e = kurtosis(distribs[i])

             u_alpha = stats.norm.ppf(1 - 0.05 / 2)

             left_bound_m = mean - ((std * u_alpha) / np.sqrt(sizes[i]))
             right_bound_m = mean + ((std * u_alpha) / np.sqrt(sizes[i]))

             mu_bounds.append(left_bound_m)
             mu_bounds.append(right_bound_m)

             print(left_bound_m, " < m < ", right_bound_m, "\n")

             left_bound_s = std * (1 - 0.5 * u_alpha * np.sqrt(e + 2) / np.sqrt(sizes[i]))
             right_bound_s = std * (1 + 0.5 * u_alpha * np.sqrt(e + 2) / np.sqrt(sizes[i]))

             sigma_bounds.append(left_bound_s)
             sigma_bounds.append(right_bound_s)

             print(left_bound_s, " < σ < ", right_bound_s, "\n")

             # LABEL = name + ": n = " + str(sizes[i])

             # plt.subplot(1, 2, i+1)
             #
             # plt.plot([left_bound_m - right_bound_s, left_bound_m - right_bound_s], [0, 0.8], '-o', color='b',
             #                 ms=5, label="min\μ - max\σ")
             # plt.plot([right_bound_m + right_bound_s, right_bound_m + right_bound_s], [0, 0.8], '-o', color='b',
             #                 ms=5, label="max\μ + max\σ")
             # plt.plot([left_bound_m, left_bound_m], [0, 0.8], '-o', color='m', ms=5, label='min\μ')
             # plt.plot([right_bound_m, right_bound_m], [0, 0.8], '-o', color='m', ms=5, label='max\μ')

    # 0 - left 20
    # 1 - right 20
    # 2 - left 100
    # 3 - right 100

     LABEL = name + ": n = 20"
     plt.subplot(1, 4, 1)
     plt.hist(x20, bins=15, density=True, color="lightblue", label=('hyst' + name))
     plt.plot([mu_bounds[0] - sigma_bounds[1], mu_bounds[0] - sigma_bounds[1]], [0, 0.8], '-o', color='b',
              ms=5, label="min\μ - max\σ")
     plt.plot([mu_bounds[1] + sigma_bounds[1], mu_bounds[1] + sigma_bounds[1]], [0, 0.8], '-o', color='b',
              ms=5, label="max\μ + max\σ")
     plt.plot([mu_bounds[0], mu_bounds[0]], [0, 0.8], '-o', color='m', ms=5, label='min\μ')
     plt.plot([mu_bounds[1], mu_bounds[1]], [0, 0.8], '-o', color='m', ms=5, label='max\μ')

     plt.title(LABEL)
     plt.legend()
     if distName != "random_dist":
        plt.ylim(0, 1.4)

     LABEL = name + ": n = 100"
     plt.subplot(1, 4, 2)
     plt.hist(x20, bins=15, density=True, color="lightblue", label=('hyst ' + name))
     plt.plot([mu_bounds[2] - sigma_bounds[3], mu_bounds[2] - sigma_bounds[3]], [0, 0.8], '-o', color='b',
              ms=5, label="min\μ - max\σ")
     plt.plot([mu_bounds[3] + sigma_bounds[3], mu_bounds[3] + sigma_bounds[3]], [0, 0.8], '-o', color='b',
              ms=5, label="max\μ + max\σ")
     plt.plot([mu_bounds[2], mu_bounds[2]], [0, 0.8], '-o', color='m', ms=5, label='min\μ')
     plt.plot([mu_bounds[3], mu_bounds[3]], [0, 0.8], '-o', color='m', ms=5, label='max\μ')

     plt.title(LABEL)
     plt.legend()
     if distName != "random_dist":
        plt.ylim(0, 1.4)

     LABEL = name
     plt.subplot(1, 4, 3)
     plt.plot([mu_bounds[0], mu_bounds[1]], [1.0, 1.0], '-o', color='b', ms=5, label="μ - interval: n = 20")
     plt.plot([mu_bounds[2], mu_bounds[3]], [1.1, 1.1], '-o', color='m', ms=5, label="μ - interval: n = 100")

     plt.title(LABEL)
     plt.legend()
     plt.ylim(0.9, 1.4)

     LABEL = name
     plt.subplot(1, 4, 4)
     plt.plot([sigma_bounds[0], sigma_bounds[1]], [1.0, 1.0], '-o', color='b', ms=5, label="σ - interval: n = 20")
     plt.plot([sigma_bounds[2], sigma_bounds[3]], [1.1, 1.1], '-o', color='m', ms=5, label="σ - interval: n = 100")

     plt.title(LABEL)
     plt.legend()
     plt.ylim(0.9, 1.4)

     plt.show()

     return 0

print("Рандомно сгенерированная выборка\n")
boxplot_t("random_dist")

print("Нормальное распределение (0,1)\n")
boxplot_t(norm)

print("Распределение Коши(0,1)\n")
boxplot_t(cauchy)

print("Распределение Стьюдента(0, 3)\n")
boxplot_t(t, 3)

print("Равномерное распределение (-(3^1/2),(3^1/2))\n")
boxplot_t(uniform)

print("Распределение Пуассона(5)\n")
boxplot_t(poisson, 5)
