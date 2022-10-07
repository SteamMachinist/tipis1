import matplotlib.pyplot as plt
import numpy as np


def phase(frequency, t, shift):
    return 2 * np.pi * frequency * t + shift


def harmonic_signal(a, frequency, shift, t):
    return a * np.sin(phase(frequency, t, shift))


def digital_signal(a, frequency, shift, t):
    return max(0, a * np.sign(np.sin(phase(frequency, t, shift))))

    # max(0, a * np.sign(np.sin(phase(frequency, t, shift))))
    # a * np.sign(np.sin(2 * np.pi * t * frequency + phi))
    # max(0, np.power(-1, np.floor(2 * frequency * t)))
    # np.where(abs(t) <= 0.5, 1, 0)


if __name__ == '__main__':
    graph_names = ['harmonic', 'digital', 'harmonic spectre', 'digital spectre']
    graph_types = 4
    graphs = dict.fromkeys(graph_names, ([], []))
    frequencies = [1, 2, 4, 8]
    t = np.linspace(0.0, 1.0, 10000)
    freq_x = np.fft.rfftfreq(len(t), d=1 / 10000)
    figure, axis = plt.subplots(graph_types, len(frequencies))

    for f_n, frequency in enumerate(frequencies):
        p = (1, frequency, 0)

        graphs['harmonic'] = t, [harmonic_signal(p[0], p[1], p[2], t1) for t1 in t]
        graphs['digital'] = t, [digital_signal(p[0], p[1], p[2], t1) for t1 in t]
        graphs['harmonic spectre'] = freq_x, np.fft.rfft(graphs['harmonic'][1])
        graphs['digital spectre'] = freq_x, np.fft.rfft(graphs['digital'][1])

        for g_n, (graph_name, (x, y)) in enumerate(graphs.items()):
            if g_n > 1:
                axis[g_n, f_n].set_xlim([-1 * frequency, 15 * frequency])
                axis[g_n, f_n].plot(x, np.abs(y))
            else:
                axis[g_n, f_n].plot(x, y)
            if g_n == 0:
                axis[g_n, f_n].set_title(f'{frequency} Hz')
            if f_n == 0:
                axis[g_n, f_n].set_ylabel(graph_name)

    plt.show()
