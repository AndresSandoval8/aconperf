"""Contains aerodynamic calculations."""
from numpy import pi, sqrt, tan


def polhamus(c_l_alpha, ar, mach, sweep_le):
    """returns lift curve slope using Polhamus method."""
    if ar < 4:
        k = 1 + ar * (1.87 - 0.000233 * sweep_le * pi / 180) / 100
    else:
        k = 1 + ((8.2 - 2.3 * sweep_le * pi / 180) - ar * (0.22 - 0.153 * sweep_le)) / 100
    sweep_2 = 0

    if mach < 1:
        beta = sqrt(1 - mach ** 2)
        root = 4 + ((ar ** 2 * beta ** 2) / (k ** 2) * (1 + (tan(sweep_2 * pi / 180) ** 2) / (beta ** 2)))
        c_l_alpha_wing = c_l_alpha * ar / (2 + sqrt(root))
    else:
        beta = sqrt(mach ** 2 - 1)
        c_l_alpha_wing = 4/beta

    return c_l_alpha_wing
