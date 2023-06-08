import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import Formatter, AutoMinorLocator
import matplotlib.ticker as ticker 

# x_vals = np.linspace(-5, 5, 2000)
# y_vals = np.array([x**2 for x in x_vals])

# fig, ax = plt.subplots()
# ax.plot(x_vals, y_vals)
# plt.show()

# ============================ Example2 ========================================

# def f(x):
#     if x < 0:
#         return np.cos(x)
#     else:
#         return np.sin(x)

# x_vals = np.linspace(-2 * np.pi, 2 * np.pi, 2000)
# y_vals = np.array([f(x) for x in x_vals])

# fig, ax = plt.subplots()

# ax.plot(x_vals, y_vals)
# ax.grid()
# ax.set_xlabel('xlabel')
# ax.set_ylabel('ylabel')
# ax.set_title('2nd example')
# ax.yaxis.set_minor_locator(AutoMinorLocator(4))


# plt.show()


# ============================ Example3 ========================================

# x_vals = np.arange(6)
# y_vals = np.random.uniform(1, 2, len(x_vals))

# fig, ax = plt.subplots()
# ax.stem(x_vals, y_vals)

# ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
#        ylim=(0, 8), yticks=np.arange(1, 8))


# plt.show()

# ============================ Example4 ========================================

def f(x):
    return np.cos(x)

def format_func(value, tick_number):
    # find number of multiples of pi/2
    N = int(np.round(2 * value / np.pi))
    if N == 0:
        return "0"
    elif N == 1:
        return r"$\pi/2$"
    elif N == 2:
        return r"$\pi$"
    elif N % 2 > 0:
        return r"${0}\pi/2$".format(N)
    else:
        return r"${0}\pi$".format(N // 2)


x_vals = np.linspace(0, 2 * np.pi, 2000)
y_vals = np.array([f(x) for x in x_vals])

x_vals2 = np.linspace(0, 2 * np.pi, 10)
y_vals2 = np.array([f(x) for x in x_vals2])

x_vals3 = np.linspace(0, 2 * np.pi)
y_vals3 = np.array([1 for x in x_vals3])


fig, ax = plt.subplots()
fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()


ax.plot(x_vals, y_vals, 'blue')
ax1.stem(x_vals2, y_vals2, 'red')
ax2.plot(x_vals3, y_vals3, 'green')

ax.axhline(0, color='black', lw=2)
ax.axvline(0, color='black', lw=2)

ax.xaxis.set_major_locator(plt.MultipleLocator(np.pi / 2))
ax.yaxis.set_major_locator(plt.MultipleLocator(0.25))
ax.xaxis.set_major_formatter(plt.FuncFormatter(format_func))

ax.grid()
plt.show()

# ============================ Example5 (two curves in one figure) ========================================

# x_vals = [1, 2, -1]
# y_vals = [2, 8, 5]

# x_vals2 = [-1, 4, -1]
# y_vals2 = [0, 4, 8]


# fig, ax = plt.subplots()
# ax.plot(x_vals, y_vals)
# ax.plot(x_vals2, y_vals2)
# ax.grid()

# plt.show()




