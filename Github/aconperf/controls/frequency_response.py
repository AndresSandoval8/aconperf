from control import bode as bode_values, root_locus
from matplotlib import pyplot
from numpy import arccos, log10, pi, tan


def bode(sys):
    """return bode plot."""
    pyplot.style.use('fivethirtyeight')
    mag, phase, w = bode_values(sys)
    pyplot.subplot(2, 1, 1)
    pyplot.semilogx(w, 20 * log10(mag))
    pyplot.ylabel('Magnitude')
    pyplot.subplot(2, 1, 2)
    pyplot.semilogx(w, phase * 180 / pi)
    pyplot.ylabel('Phase')
    pyplot.xlabel('Frequency')


def root_locus_design(sys):
    """return root locus."""
    pyplot.style.use('fivethirtyeight')
    root_locus(sys)
    damping_ratio = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

    for i in damping_ratio:
        x = [-100, 0]
        phi = arccos(i)
        y_pos = [100 * tan(phi), 0]
        y_neg = [-100 * tan(phi), 0]
        pyplot.plot(x, y_pos, 'k--', linewidth=1)
        pyplot.plot(x, y_neg, 'k--', linewidth=1)


def second_order_tf(zeta, omega):
    poly_coef = [1, 2*zeta*omega, omega**2]
    return poly_coef


def first_order_tf(t):
    poly_coef = [1, 1/t]
    return poly_coef
