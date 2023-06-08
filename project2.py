import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import Formatter, AutoMinorLocator
import matplotlib.ticker as ticker 


def signal(amplitude, frequency, phase, t):
    return amplitude * np.cos(2 * np.pi * frequency * t + phase)


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




def draw_main_signal():
    fg_main_signal, ax_main_signal = plt.subplots()
    
    ax_main_signal.plot(t_vals, y_vals, 'blue')

    ax_main_signal.axvline(0, color='black', lw=2)
    ax_main_signal.axhline(0, color='black', lw=2)

    ax_main_signal.xaxis.set_major_locator(plt.MultipleLocator(np.pi / 2))
    ax_main_signal.yaxis.set_major_locator(plt.MultipleLocator(0.25))
    ax_main_signal.xaxis.set_major_formatter(plt.FuncFormatter(format_func))

    ax_main_signal.grid()
    
    return [fg_main_signal, ax_main_signal]

def draw_sampling_signal():
    fg_main_sampling, ax_main_sampling = draw_main_signal()


    t_samples = [x for x in range(0, int(np.ceil(duration)), sample_rate)]
    y_samples = np.array([signal(amplitude, frequency, phase, t) for t in t_samples])


    # ax_main_sampling.plot(t_vals, y_vals, 'blue')
    ax_main_sampling.stem(t_samples, y_samples, 'red')

    ax_main_sampling.axhline(0, color='black', lw=2)
    ax_main_sampling.axvline(0, color='black', lw=2)

    ax_main_sampling.xaxis.set_major_locator(plt.MultipleLocator(np.pi / 2))
    ax_main_sampling.yaxis.set_major_locator(plt.MultipleLocator(0.25))
    ax_main_sampling.xaxis.set_major_formatter(plt.FuncFormatter(format_func))

    return [fg_main_sampling, ax_main_sampling]

def draw_horizontal_levels():
    fg_levels_signal_sampling, ax_levels_signal_sampling = draw_sampling_signal()

    levels_xs = np.linspace(0, duration)
    levels_ys = np.linspace(start=-1 * amplitude,stop=amplitude, num=number_of_levels , endpoint=True)

    
    for i in range(0, number_of_levels):
        y_vals = np.array([levels_ys[i] for x in levels_xs])
        ax_levels_signal_sampling.plot(levels_xs, y_vals)
        binary_stram = produce_binary_stream(number_of_bits, i)
        ax_levels_signal_sampling.annotate(binary_stram, xy=(duration/2, y_vals[i]))
    
    return [fg_levels_signal_sampling, ax_levels_signal_sampling]
    
def produce_binary_stream(number_of_bits, decimal_number):
    output = ''

    binary_str = bin(decimal_number)[2:]
    num_of_zeros_must_be_added = number_of_bits - len(binary_str)
    for i in range(0, num_of_zeros_must_be_added):
        output += '0'
    output += binary_str

    return output


if __name__ == '__main__':

    duration = 4 * np.pi
    amplitude = 1
    frequency = 0.3
    phase = np.pi / 4
    number_of_bits = 3
    number_of_levels = 2 ** number_of_bits
    sample_rate = 1 # Take a single sample each two seconds

    t_vals = np.linspace(0, duration, 2000)
    y_vals = np.array([signal(amplitude, frequency, phase, t) for t in t_vals])


    draw_main_signal()
    draw_sampling_signal()
    draw_horizontal_levels()

    plt.show()


    # x_test = np.linspace(0, duration)
    # y_test = np.linspace(-8, 8, 4, endpoint=True)

    # number_of_horizontal_lines = len(y_test)

    # fig, ax = plt.subplots()
    # ax.grid()

    # for i in range(0, number_of_horizontal_lines):
    #     y_vals = np.array([y_test[i] for x in x_test])
    #     ax.plot(x_test, y_vals)
    #     ax.annotate('0001', xy=(duration/2, y_test[i]))
    
    # plt.show()

    # Till Here


    # binary_str = bin(1)[2:]

    # num = 3
    # str_my = ''
    # for num in range(0, num):
    #     str_my += '0'
    # str_my += binary_str

    # print(str_my)
    



