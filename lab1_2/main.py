import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math

from scipy.stats import norm
from scipy.stats import cauchy
from scipy.stats import t
from scipy.stats import uniform
from scipy.stats import poisson

# Мощность выборки
sample_size1 = 20
sample_size2 = 100
sample_size3 = 500

# Нормальное распределение (Гаусс)
# Сгенерировать выборки размером 20, 100 и 500 элементов.
# random_var = norm
#
# x1 = random_var.rvs(size=sample_size1)
# x2 = random_var.rvs(size=sample_size2)
# x3 = random_var.rvs(size=sample_size3)
#
# n_linspace1 = np.linspace(x1.min(), x1.max(), sample_size1)
# n_linspace2 = np.linspace(x2.min(), x2.max(), sample_size2)
# n_linspace3 = np.linspace(x3.min(), x3.max(), sample_size3)
#
# plt.plot(n_linspace1, stats.norm.pdf(n_linspace1, 0, 1), label='Probability density function')
# plt.hist(x1, bins=20, density=True, color="lightblue", label='Histogram of distribution')
# plt.title("Normal distribution n=20")
# plt.xlabel("normalNumbers")
# plt.ylabel("Density")
# plt.legend(loc='best')
# plt.show()
#
# plt.plot(n_linspace2, stats.norm.pdf(n_linspace2, 0, 1), label='Probability density function')
# plt.hist(x2, bins=25, density=True, color="lightblue", label='Histogram of distribution')
# plt.title("Normal distribution n=100")
# plt.xlabel("normalNumbers")
# plt.ylabel("Density")
# plt.legend(loc='best')
# plt.show()
#
# plt.plot(n_linspace3, stats.norm.pdf(n_linspace3, 0, 1), label='Probability density function')
# plt.hist(x3, bins=50, density=True, color="lightblue", label='Histogram of distribution')
# plt.title("Normal distribution n=500")
# plt.xlabel("normalNumbers")
# plt.ylabel("Density")
# plt.legend(loc='best')
# plt.show()


#Коши
# random_var = cauchy
#
# x1 = random_var.rvs(size=sample_size1)
# x2 = random_var.rvs(size=sample_size2)
# x3 = random_var.rvs(size=sample_size3)
#
# n_linspace1 = np.linspace(x1.min(), x1.max(), sample_size1)
# n_linspace2 = np.linspace(x2.min(), x2.max(), sample_size2)
# n_linspace3 = np.linspace(x3.min(), x3.max(), sample_size3)
#
# plt.plot(n_linspace1, stats.cauchy.pdf(n_linspace1), label='Probability density function')
# plt.hist(x1, bins=20, density=True, color="lightblue", label='Histogram of distribution')
# plt.title("Cauchy distribution n=20")
# plt.xlabel("cauchyNumbers")
# plt.ylabel("Density")
# plt.legend(loc='best')
# plt.show()
#
# plt.plot(n_linspace2, stats.cauchy.pdf(n_linspace2), label='Probability density function')
# plt.hist(x2, bins=50, density=True, color="lightblue", label='Histogram of distribution')
# plt.title("Cauchy distribution n=100")
# plt.xlabel("cauchyNumbers")
# plt.ylabel("Density")
# plt.legend(loc='best')
# plt.show()
#
# plt.plot(n_linspace3, stats.cauchy.pdf(n_linspace3), label='Probability density function')
# plt.hist(x3, bins=100, density=True, color="lightblue", label='Histogram of distribution')
# plt.title("Cauchy distribution n=500")
# plt.xlabel("cauchyNumbers")
# plt.ylabel("Density")
# plt.legend(loc='best')
# plt.show()

#Стьюдента
# random_var = t
# df = 3
#
# x1 = random_var.rvs(df, size=sample_size1)
# x2 = random_var.rvs(df, size=sample_size2)
# x3 = random_var.rvs(df, size=sample_size3)
#
# n_linspace1 = np.linspace(x1.min(), x1.max(), sample_size1)
# n_linspace2 = np.linspace(x2.min(), x2.max(), sample_size2)
# n_linspace3 = np.linspace(x3.min(), x3.max(), sample_size3)
#
# plt.plot(n_linspace1, stats.t.pdf(n_linspace1, df), label='Probability density function')
# plt.hist(x1, bins=20, density=True, color="lightblue", label='Histogram of distribution')
# plt.title("Student's t-distribution n=20")
# plt.xlabel("studentsNumbers")
# plt.ylabel("Density")
# plt.legend(loc='best')
# plt.show()
#
# plt.plot(n_linspace2, stats.t.pdf(n_linspace2, df), label='Probability density function')
# plt.hist(x2, bins=30, density=True, color="lightblue", label='Histogram of distribution')
# plt.title("Student's t-distribution n=100")
# plt.xlabel("studentsNumbers")
# plt.ylabel("Density")
# plt.legend(loc='best')
# plt.show()
#
# plt.plot(n_linspace3, stats.t.pdf(n_linspace3, df), label='Probability density function')
# plt.hist(x3, bins=60, density=True, color="lightblue", label='Histogram of distribution')
# plt.title("Student's t-distribution n=500")
# plt.xlabel("studentsNumbers")
# plt.ylabel("Density")
# plt.legend(loc='best')
# plt.show()

#Равномерное
# random_var = uniform
#
# x1 = random_var.rvs(size=sample_size1)
# x2 = random_var.rvs(size=sample_size2)
# x3 = random_var.rvs(size=sample_size3)
#
# n_linspace1 = np.linspace(-math.sqrt(3), math.sqrt(3), sample_size1)
# n_linspace2 = np.linspace(-math.sqrt(3), math.sqrt(3), sample_size2)
# n_linspace3 = np.linspace(-math.sqrt(3), math.sqrt(3), sample_size3)
#
# plt.plot(n_linspace1, stats.uniform.pdf(n_linspace1), label='Probability density function')
# plt.hist(x1, bins=20, density=True, color="lightblue", label='Histogram of distribution')
# plt.title("Uniform distribution n=20")
# plt.xlabel("uniformNumbers")
# plt.ylabel("Density")
# plt.legend(loc='best')
# plt.show()
#
# plt.plot(n_linspace2, stats.uniform.pdf(n_linspace2), label='Probability density function')
# plt.hist(x2, bins=25, density=True, color="lightblue", label='Histogram of distribution')
# plt.title("Uniform distribution n=100")
# plt.xlabel("uniformNumbers")
# plt.ylabel("Density")
# plt.legend(loc='best')
# plt.show()
#
# plt.plot(n_linspace3, stats.uniform.pdf(n_linspace3), label='Probability density function')
# plt.hist(x3, bins=30, density=True, color="lightblue", label='Histogram of distribution')
# plt.title("Uniform distribution n=500")
# plt.xlabel("uniformNumbers")
# plt.ylabel("Density")
# plt.legend(loc='best')
# plt.show()


#Пуассона
random_var = poisson
mu = 5

x1 = random_var.rvs(mu, size=sample_size1)
x2 = random_var.rvs(mu, size=sample_size2)
x3 = random_var.rvs(mu, size=sample_size3)
print(x1)
n_linspace1 = np.arange(x1.min(), x1.max())
n_linspace2 = np.arange(x2.min(), x2.max())
n_linspace3 = np.arange(x3.min(), x3.max())

# plt.plot(n_linspace1, stats.poisson.pmf(n_linspace1, mu), label='Probability mass function')
# plt.hist(x1, bins=10, density=True, color="lightblue", label='Histogram of distribution')
# plt.title("Poisson distribution n=20")
# plt.xlabel("poissonNumbers")
# plt.ylabel("Density")
# plt.legend(loc='best')
# plt.show()
#
# plt.plot(n_linspace2, stats.poisson.pmf(n_linspace2, mu), label='Probability mass function')
# plt.hist(x2, bins=15, density=True, color="lightblue", label='Histogram of distribution')
# plt.title("Poisson distribution n=100")
# plt.xlabel("poissonNumbers")
# plt.ylabel("Density")
# plt.legend(loc='best')
# plt.show()
#
# plt.plot(n_linspace3, stats.poisson.pmf(n_linspace3, mu), label='Probability mass function')
# plt.hist(x3, bins=20, density=True, color="lightblue", label='Histogram of distribution')
# plt.title("Poisson distribution n=500")
# plt.xlabel("poissonNumbers")
# plt.ylabel("Density")
# plt.legend(loc='best')
# plt.show()
