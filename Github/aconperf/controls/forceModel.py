from modeling.aircraft import c_d_zero, \
    c_l_zero, c_l_alpha, c_l_alpha_dot, c_l_pitch_rate, c_l_delta_elevator, \
    c_m_zero, c_m_alpha, c_m_alpha_dot, c_m_pitch_rate, c_m_delta_elevator
from modeling.lifting_surface import mac
from modeling.aerodynamics import dynamic_pressure
from modeling.atmosphere import speed_of_sound
from numpy import array, arctan, sqrt


def c_f_m(aircraft, x, u):
    s = aircraft['wing']['planform']
    altitude = x[-1]
    a = speed_of_sound(altitude)
    v = sqrt(x[0]**2 + x[1]**2 + x[2]**2)
    mach = v/a
    alpha = arctan(x[2]/x[0])
    c_bar = mac(aircraft['wing']['aspect_ratio'], s, aircraft['wing']['taper'])
    q_hat = x[7]*c_bar/(2*v)
    alpha_dot = 0
    d_elevator = u[1]
    f_x = force_x(aircraft, mach, altitude, alpha, alpha_dot, q_hat, d_elevator)
    f_y = 0
    f_z = force_z(aircraft, mach, altitude, alpha, alpha_dot, q_hat, d_elevator)
    m_x = 0
    m_y = moment_y(aircraft, mach, altitude, alpha, alpha_dot, q_hat, d_elevator)
    m_z = 0
    c = array([f_x, f_y, f_z, m_x, m_y, m_z])
    return c


def force_x(aircraft, mach, altitude, alpha, alpha_dot, q_hat, d_elevator):
    """returns x axis force."""
    q_bar = dynamic_pressure(mach, altitude)
    s = aircraft['wing']['planform']
    # c_x = -(c_d_zero(aircraft, mach, altitude) +
    #        (c_l_alpha(aircraft, mach) * alpha +
    #        c_l_alpha_dot(aircraft, mach) * alpha_dot +
    #        c_l_pitch_rate(aircraft, mach) * q_hat +
    #        c_l_delta_elevator(aircraft, mach) * d_elevator) * 2)
    c_x = 0
    return q_bar * s * c_x


def force_y():
    """returns y axis force."""
    return 0


def force_z(aircraft, mach, altitude, alpha, alpha_dot, q_hat, d_elevator):
    """returns z axis force."""
    q_bar = dynamic_pressure(mach, altitude)
    s = aircraft['wing']['planform']
    c_z = -(c_l_zero(aircraft, mach) +
            c_l_alpha(aircraft, mach) * alpha +
            c_l_alpha_dot(aircraft, mach) * alpha_dot +
            c_l_pitch_rate(aircraft, mach) * q_hat +
            c_l_delta_elevator(aircraft, mach) * d_elevator)
    return q_bar * s * c_z


def moment_x():
    """returns x axis moment."""
    return 0


def moment_y(aircraft, mach, altitude, alpha, alpha_dot, q_hat, d_elevator):
    """returns y axis moment."""
    q_bar = dynamic_pressure(mach, altitude)
    s = aircraft['wing']['planform']
    c_bar = mac(aircraft['wing']['aspect_ratio'], s, aircraft['wing']['taper'])
    c_my = (c_m_zero(aircraft, mach, altitude) +
            c_m_alpha(aircraft, mach) * alpha +
            c_m_alpha_dot(aircraft, mach) * alpha_dot +
            c_m_pitch_rate(aircraft, mach) * q_hat +
            c_m_delta_elevator(aircraft, mach) * d_elevator)
    return q_bar * s * c_bar * c_my


def moment_z():
    """returns z axis moment."""
    return 0
