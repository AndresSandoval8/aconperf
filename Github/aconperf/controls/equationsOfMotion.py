# File containing Equations of Motion
from numpy import array, concatenate, cos, cross, dot, linalg, sin, transpose
from common.rotation_matrix import angular_rate, ned_to_body


def nonlinear_eom(x, m, j, c, g):
    """contains nonlinear equations of motion."""
    # x = [u v w phi theta psi p q r p_n p_e h]
    # m = mass of the system
    # j = inertia of the system
    # c = [f_x f_y f_z m_x m_y m_z]
    external_forces = c[0:3]
    external_moments = c[3:6]
    weight = g * array([-sin(x[4]), cos(x[4]) * sin(x[3]), cos(x[4]) * cos(x[3])])
    v = x[0:3]
    omega = x[6:9]
    euler = x[3:6]

    # linear momentum equations
    linear_momentum = external_forces / m + weight - cross(omega, v)

    # kinematics equations
    b_euler = angular_rate(euler[0], euler[1])
    kinematics = b_euler @ omega

    # angular momentum equations
    angular_momentum = linalg.inv(j) @ transpose(external_moments - cross(omega, dot(j, omega)))

    # navigation equations
    b_body = ned_to_body(euler[0], euler[1], euler[2])
    navigation = b_body.transpose() @ v
    dx_dt = concatenate((concatenate((concatenate((linear_momentum, kinematics)), angular_momentum)), navigation))
    return dx_dt
