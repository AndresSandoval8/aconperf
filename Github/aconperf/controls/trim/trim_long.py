"""Trim aircraft longitudinally."""
from modeling.aircraft import c_l_alpha, c_l_delta_elevator, c_l_zero, c_m_zero, c_m_alpha, c_m_delta_elevator
from modeling.atmosphere import air_density, speed_of_sound
from numpy import array, cos, deg2rad, linalg, rad2deg


def trim_alpha_de(aircraft, speed, altitude, gamma):
    """trim aircraft with angle of attack and elevator"""
    a = speed_of_sound(altitude)  # [ft/s]
    rho = air_density(altitude)  # [slug / ft^3]
    mach = speed / a  # []
    c_l_a = c_l_alpha(aircraft, mach)  # [1/rad]
    c_l_de = c_l_delta_elevator(aircraft, mach)  # [1/rad]
    c_m_a = c_m_alpha(aircraft, mach)  # [1/rad]
    c_m_de = c_m_delta_elevator(aircraft, mach)  # [1/rad]
    c_l_0 = c_l_zero(aircraft, mach)  # []
    a = array([[c_l_a, c_l_de], [c_m_a, c_m_de]])
    w = aircraft['weight']['weight']  # [lb]
    q_bar = 0.5 * rho * speed ** 2  # [psf]
    s_w = aircraft['wing']['planform']  # [ft^2]
    c_l_1 = w * cos(deg2rad(gamma)) / (s_w * q_bar)  # []
    c_m_0 = c_m_zero(aircraft, mach, altitude)
    b = array([[c_l_1 - c_l_0], [- c_m_0]])
    c = linalg.solve(a, b)  # [rad]
    return rad2deg(c)
