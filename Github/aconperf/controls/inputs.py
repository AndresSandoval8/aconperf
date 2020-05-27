from numpy import array, linspace, pi, sin


def linear_chirp(f_initial, f_final, amplitude, period):
    """return linear chirp outputs."""
    t = array(linspace(0, period, 10000))
    c = (f_final - f_initial) / period
    x = amplitude * sin(2 * pi * (c / 2 * t ** 2 + f_initial * t))
    return x
