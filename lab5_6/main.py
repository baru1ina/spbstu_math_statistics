import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats
import math

cov1 = np.array([[1, 0], [0, 1]])
cov2 = np.array([[1, 0.5], [0.5, 1]])
cov3 = np.array([[1, 0.9], [0.9, 1]])

sizes = [20, 60, 100]

def print_ellipsis():
    for i in range(len(sizes)):
        plt.subplot(1, 3, 1)
        pts = np.random.multivariate_normal([0, 0], cov1, size=sizes[i])
        plt.plot(pts[:, 0], pts[:, 1], '.', alpha=0.5)
        plt.title("size = " + str(sizes[i]) + "; p = " + str(cov1[0][1]))
        plt.axis('equal')

        plt.subplot(1, 3, 2)
        pts = np.random.multivariate_normal([0, 0], cov2, size=sizes[i])
        plt.plot(pts[:, 0], pts[:, 1], '.', alpha=0.5)
        plt.title("size = " + str(sizes[i]) + "; p = " + str(cov2[0][1]))
        plt.axis('equal')

        plt.subplot(1, 3, 3)
        pts = np.random.multivariate_normal([0, 0], cov3, size=sizes[i])
        plt.plot(pts[:, 0], pts[:, 1], '.', alpha=0.5)
        plt.title("size = " + str(sizes[i]) + "; p = " + str(cov3[0][1]))
        plt.axis('equal')

        plt.show()
    return 0

def prints(mean, mean_square, std):
    print("     Выборочное среднее = ", "{:12.4e}".format(mean))
    print("     Выборочное среднее значение квадрата = ", "{:12.4e}".format(mean_square))
    print("     Выборочная дисперсия = ", "{:12.4e}".format(std))
    print("\n")
    print("{:12.4e}".format(mean), " & ", "{:12.4e}".format(mean_square), " & ",
          "{:12.4e}".format(std), "\\\\ \\hline")
    print("\n")

def do_math(flag):
    if flag == 0:
        covs = [cov1, cov2, cov3]
        for size in sizes:
            for cov in covs:
                pirson_m = 0
                pirson_s = 0
                pirson_d = 0

                spearman_m = 0
                spearman_s = 0
                spearman_d = 0

                kendall_m = 0
                kendall_s = 0
                kendall_d = 0

                for i in range(1000):
                    pts = np.random.multivariate_normal([0, 0], cov, size=size)
                    df = pd.DataFrame(pts)

                    pirson_m += df[0].corr(df[1])
                    pirson_s += df[0].corr(df[1])**2

                    spearman_m += df[0].corr(df[1], method='spearman')
                    spearman_s += df[0].corr(df[1], method='spearman') ** 2

                    kendall_m += df[0].corr(df[1], method='kendall')
                    kendall_s += df[0].corr(df[1], method='kendall')**2

                pirson_m /= 1000
                pirson_s /= 1000
                pirson_d = pirson_s - pirson_m**2

                spearman_m /= 1000
                spearman_s /= 1000
                spearman_d = spearman_s - spearman_m**2

                kendall_m /= 1000
                kendall_s /= 1000
                kendall_d = kendall_s - kendall_m**2

                print("Размер выборки = ", size, " ρ = ", cov[0][1], "\n")

                print("Выборочный коэффициент корреляции Пирсона:")
                prints(pirson_m, pirson_s, pirson_d)
                print("Выборочный коэффициент корреляции Спирмена:")
                prints(spearman_m, spearman_s, spearman_d)
                print("Выборочный квадрантный коэффициент корреляции:")
                prints(kendall_m, kendall_s, kendall_d)

    else:
        cov4 = np.array([[10, -0.9], [-0.9, 10]])
        for i in range(len(sizes)):
            plt.subplot(1, 3, i+1)
            pts = (0.9 * (np.random.multivariate_normal([0, 0], cov3, size=sizes[i]))
                   + 0.1 * (np.random.multivariate_normal([0, 0], cov4, size=sizes[i])))
            plt.plot(pts[:, 0], pts[:, 1], '.', alpha=0.5)
            plt.title("size = " + str(sizes[i]))

            pirson_m = 0
            pirson_s = 0
            pirson_d = 0

            spearman_m = 0
            spearman_s = 0
            spearman_d = 0

            kendall_m = 0
            kendall_s = 0
            kendall_d = 0

            for j in range(1000):
                pts = (0.9 * (np.random.multivariate_normal([0, 0], cov3, size=sizes[i]))
                       + 0.1 * (np.random.multivariate_normal([0, 0], cov4, size=sizes[i])))
                df = pd.DataFrame(pts)

                pirson_m += df[0].corr(df[1])
                pirson_s += df[0].corr(df[1]) ** 2

                spearman_m += df[0].corr(df[1], method='spearman')
                spearman_s += df[0].corr(df[1], method='spearman') ** 2

                kendall_m += df[0].corr(df[1], method='kendall')
                kendall_s += df[0].corr(df[1], method='kendall') ** 2

            pirson_m /= 1000
            pirson_s /= 1000
            pirson_d = pirson_s - pirson_m ** 2

            spearman_m /= 1000
            spearman_s /= 1000
            spearman_d = spearman_s - spearman_m ** 2

            kendall_m /= 1000
            kendall_s /= 1000
            kendall_d = kendall_s - kendall_m ** 2

            print("Размер выборки = ", sizes[i], "\n")

            print("Выборочный коэффициент корреляции Пирсона:")
            prints(pirson_m, pirson_s, pirson_d)
            print("Выборочный коэффициент корреляции Спирмена:")
            prints(spearman_m, spearman_s, spearman_d)
            print("Выборочный квадрантный коэффициент корреляции:")
            prints(kendall_m, kendall_s, kendall_d)
        plt.show()


print("Нормальное двумерное распределение 𝑁(𝑥, 𝑦, 0, 0, 1, 1, 𝜌)\n")
do_math(flag=0)
print_ellipsis()
print("Cмесь нормальных двумерхых распределений 𝑓(𝑥, 𝑦) = 0.9*𝑁(𝑥, 𝑦, 0, 0, 1, 1, 0.9) + 0.1*𝑁(𝑥, 𝑦, 0, 0, 10, 10, −0.9)\n")
do_math(flag=1)

