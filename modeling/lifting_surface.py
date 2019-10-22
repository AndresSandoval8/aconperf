"""Returns force and moment coefficients for lifting surfaces."""
from tools.aerodynamics import polhamus


def lift(wing, mach, alpha):
    c_l_alpha = wing['c_l_alpha']
    ar = wing['aspect_ratio']
    sweep_le = wing['sweep_LE']
    alpha_zero_lift = wing['alpha_zero_lift']
    c_l_alpha_wing = polhamus(c_l_alpha, ar, mach, sweep_le)
    c_l = c_l_alpha_wing * (alpha + alpha_zero_lift)
    return c_l


def drag(wing, mach, alpha):
    return 1


def pitch_moment(mach, alpha):
    return 1


def side_force(mach, alpha):
    return 1


def roll_moment():
    return 1


def yaw_moment():
    return 1
