from numpy import polymul
from control import tf, tf2ss
from controls.frequency_response import first_order_tf, second_order_tf


zeta_sp = 0.6
omega_sp = 2.77
zeta_ph = 0.1177
omega_ph = 0.0752
a_theta = -11.33
t_theta_1 = 110.011
t_theta_2 = 2.336
k_theta = -3

zeta_dr = 0.0625
omega_dr = 3.47
t_spiral = 226.757
t_roll = 1.188


def den_long():
    poly_sp = second_order_tf(zeta_sp, omega_sp)
    poly_ph = second_order_tf(zeta_ph, omega_ph)
    den = polymul(poly_ph, poly_sp)
    return den


def den_lat_dir():
    poly_dr = second_order_tf(zeta_dr, omega_dr)
    poly_sp = first_order_tf(t_roll)
    poly_rl = first_order_tf(t_spiral)
    den = polymul(poly_rl, polymul(poly_sp, poly_dr))
    return den


def num_theta():
    poly_t_1 = first_order_tf(t_theta_1)
    poly_t_2 = first_order_tf(t_theta_2)
    num = polymul(polymul(poly_t_1, poly_t_2), a_theta*k_theta)
    return num


def sim_setup_theta():
    num = num_theta()
    den = den_long()
    sys = tf2ss(tf(num, den))
    n_axis = 1
    task = [5, 1, 2]
    return sys, n_axis, task
