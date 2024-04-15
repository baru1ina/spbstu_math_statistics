import numpy as np
import scipy.stats as sps
import math
import matplotlib.pyplot as plt
import matplotlib.colors


def mnk(x: list, y: list):
    avg_x = np.average(x)
    avg_y = np.average(y)

    # print(avg_x, avg_y)

    x_sqrt = [x[i] * x[i] for i in range(len(x))]
    xy = [x[i] * y[i] for i in range(len(x))]

    avg_x_sqrt = np.average(x_sqrt)
    avg_xy = np.average(xy)

    b_eval = (avg_xy - avg_x * avg_y) / (avg_x_sqrt - avg_x ** 2)
    a_eval = avg_y - avg_x * b_eval

    print("МНК  &", '%.3f' % a_eval, "&", '%.3f' % abs(a_eval - 2), "&", '%.2f' % (abs(a_eval - 2)/2 * 100),
          "&", '%.3f' % b_eval, "&", '%.3f' % abs(b_eval - 2),  "&", '%.2f' % (abs(b_eval - 2)/2 * 100), "\\\\ \\hline")
    return a_eval, b_eval


def mnm(x: list, y: list):
    med_x = np.median(x)
    med_y = np.median(y)

    r_q_list = [np.sign(x[i] - med_x) * np.sign(y[i] - med_y) for i in range(len(x))]

    r_Q = np.average(r_q_list)

    n = len(x)
    i, d = math.modf(n / 4)
    if n / 4 == d:
        l = int(n / 4) - 1
    else:
        l = int(d)

    j = n - l - 1

    sort_x = np.sort(x)
    sort_y = np.sort(y)

    k_n = 1.491
    q_y = (sort_y[j] - sort_y[l])

    q_x = (sort_x[j] - sort_x[l])

    b_eval_R = r_Q * q_y / q_x

    a_eval_R = med_y - b_eval_R * med_x

    # print("МНМ  &", "{:12.4e}".format(a_eval_R), "&", "{:12.4e}".format(abs(a_eval_R - 2)),
    #       "&", "{:12.4e}".format(b_eval_R), "&", "{:12.4e}".format(abs(b_eval_R - 2)), "\\\\ \\hline")

    print("МНМ  &", '%.3f' % a_eval_R, "&", '%.3f' % abs(a_eval_R - 2), "&", '%.2f' % (abs(a_eval_R - 2)/2 * 100),
          "&", '%.3f' % b_eval_R, "&", '%.3f' % abs(b_eval_R - 2), "&", '%.2f' % (abs(b_eval_R - 2)/2 * 100), "\\\\ \\hline")

    return a_eval_R, b_eval_R


x = np.linspace(-1.8, 2, 20)
e = sps.norm.rvs(size=20)
y = [2 + 2 * x[i] + e[i] for i in range(len(x))]

print("Без возмущений: ")
a_eval, b_eval = mnk(list(x), y)
a_eval_R, b_eval_R = mnm(list(x), y)

y_mnk = [a_eval + b_eval * x[i] + e[i] for i in range(len(x))]
y_mnm = [a_eval_R + b_eval_R * x[i] + e[i] for i in range(len(x))]

plt.subplot(2, 2, 1)
plt.plot(x, y, color='crimson',  label="эталонная зависимость")
plt.plot(x, y_mnk, '--', color='cornflowerblue', label="робастная оценка МНК")
plt.plot(x, y_mnm, '--', color='yellowgreen', label="робастная оценка МНМ")
plt.title("Без возмущений")
plt.legend()
plt.xlabel(r'$x_i$')
plt.ylabel(r'$y_i = a + b * x_i + e_i$')
plt.annotate(f"a_mnk = {'%.3f' % a_eval}, \nb_mnk = {'%.3f' % b_eval}, "
             f"\na_mnm = {'%.3f' % a_eval_R}, \nb_mnm = {'%.3f' % b_eval_R}", xy=(0.5, min(y)))


y[0] = y[0] + 10
y[19] = y[19] - 10

print("\nС возмущениями: ")
a_eval_D, b_eval_D = mnk(list(x), y)
a_eval_R_D, b_eval_R_D = mnm(list(x), y)

y_mnk_D = [a_eval_D + b_eval_D * x[i] + e[i] for i in range(len(x))]
y_mnm_D = [a_eval_R_D + b_eval_R_D * x[i] + e[i] for i in range(len(x))]

plt.subplot(2, 2, 2)
plt.plot(x, y, color='crimson',  label="эталонная зависимость")
plt.plot(x, y_mnk_D, '--', color='cornflowerblue', label="робастная оценка МНК")
plt.plot(x, y_mnm_D, '--', color='yellowgreen', label="робастная оценка МНМ")
plt.title("С возмущениями")
plt.legend()
plt.xlabel(r'$x_i$')
plt.ylabel(r'$y_i = a + b * x_i + e_i$')
plt.annotate(f"a_mnk = {'%.3f' % a_eval_D},\nb_mnk = {'%.3f' % b_eval_D},"
             f" \na_mnm = {'%.3f' % a_eval_R_D},\nb_mnm = {'%.3f' % b_eval_R_D}", xy=(0.0, min(y)))

y = [2 + 2 * x[i] for i in range(len(x))]

y_mnk = [a_eval + b_eval * x[i] for i in range(len(x))]
y_mnm = [a_eval_R + b_eval_R * x[i] for i in range(len(x))]

plt.subplot(2, 2, 3)
plt.plot(x, y, color='crimson',  label="эталонная зависимость")
plt.plot(x, y_mnk, '--', color='cornflowerblue', label="робастная оценка МНК")
plt.plot(x, y_mnm, '--', color='yellowgreen', label="робастная оценка МНМ")
plt.title("Без возмущений линейная лависимость без ошибки")
plt.legend()
plt.xlabel(r'$x_i$')
plt.ylabel(r'$y_i = a + b * x_i$')
plt.annotate(f"a_mnk = {'%.3f' % a_eval}, \nb_mnk = {'%.3f' % b_eval}, "
             f"\na_mnm = {'%.3f' % a_eval_R}, \nb_mnm = {'%.3f' % b_eval_R}", xy=(0.5, min(y)))


y_mnk_D = [a_eval_D + b_eval_D * x[i] for i in range(len(x))]
y_mnm_D = [a_eval_R_D + b_eval_R_D * x[i] for i in range(len(x))]

plt.subplot(2, 2, 4)
plt.plot(x, y, color='crimson',  label="эталонная зависимость")
plt.plot(x, y_mnk_D, '--', color='cornflowerblue', label="робастная оценка МНК")
plt.plot(x, y_mnm_D, '--', color='yellowgreen', label="робастная оценка МНМ")
plt.title("С возмущениями линейная лависимость без ошибки")
plt.legend()
plt.xlabel(r'$x_i$')
plt.ylabel(r'$y_i = a + b * x_i$')
plt.annotate(f"a_mnk = {'%.3f' % a_eval_D},\nb_mnk = {'%.3f' % b_eval_D},"
             f" \na_mnm = {'%.3f' % a_eval_R_D},\nb_mnm = {'%.3f' % b_eval_R_D}", xy=(0.0, min(y)))


plt.show()
