import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import Formatter, AutoMinorLocator
import matplotlib.ticker as ticker 


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



def signal(amplitude, frequency, phase, t):
    return amplitude * np.cos(2 * np.pi * frequency * t + phase)

def draw_main_signal(amplitude, frequency, phase, duration):


amplitude = 2
frequency = 0.3
phase = np.pi / 4

duration = 3 * np.pi
sample_rate = 3 # Take a single sample each two seconds



draw_main_signal(amplitude, frequency, phase, duration)


t_vals = np.linspace(0, duration, 2000)
y_vals = np.array([signal(amplitude, frequency, phase, t) for t in t_vals])
t_samples = [x for x in range(0, int(np.ceil(duration)), sample_rate)]
y_samples = np.array([signal(amplitude, frequency, phase, t) for t in t_samples])

fg_main_signal, ax_main_signal = plt.subplots()
fg_main_sampling, ax_main_sampling = plt.subplots()

ax_main_signal.plot(t_vals, y_vals, 'blue')

ax_main_sampling.plot(t_vals, y_vals, 'blue')
ax_main_sampling.stem(t_samples, y_samples, 'red')

ax_main_signal.axhline(0, color='black', lw=2)
ax_main_signal.axvline(0, color='black', lw=2)

ax_main_sampling.axhline(0, color='black', lw=2)
ax_main_sampling.axvline(0, color='black', lw=2)

ax_main_signal.xaxis.set_major_locator(plt.MultipleLocator(np.pi / 2))
ax_main_signal.yaxis.set_major_locator(plt.MultipleLocator(0.25))
ax_main_signal.xaxis.set_major_formatter(plt.FuncFormatter(format_func))

ax_main_sampling.xaxis.set_major_locator(plt.MultipleLocator(np.pi / 2))
ax_main_sampling.yaxis.set_major_locator(plt.MultipleLocator(0.25))
ax_main_sampling.xaxis.set_major_formatter(plt.FuncFormatter(format_func))


ax_main_sampling.grid()
ax_main_signal.grid()

plt.show()


