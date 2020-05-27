from numpy import polymul
from control import tf, tf2ss
from controls.frequency_response import first_order_tf, second_order_tf


zeta_sp = 0.522
omega_sp = 1.619
zeta_ph = 0.0606
omega_ph = 0.1635
a_theta = -1.338
t_theta_1 = 16.529
t_theta_2 = 1.869
k_theta = -20

zeta_dr = 0.1096
omega_dr = 0.996
t_spiral = -76.92
t_roll = 0.892
# zeta_rs = 0.05
# omega_rs = 0.15
a_phi = -0.726
zeta_phi = 0.223
omega_phi = 0.943
k_phi = 8


def den_long():
    poly_sp = second_order_tf(zeta_sp, omega_sp)
    poly_ph = second_order_tf(zeta_ph, omega_ph)
    den = polymul(poly_ph, poly_sp)
    return den


def den_lat_dir():
    poly_dr = second_order_tf(zeta_dr, omega_dr)
    poly_sp = first_order_tf(t_roll)
    poly_rl = first_order_tf(t_spiral)
    # poly_rs = second_order_tf(zeta_rs, omega_rs)
    den = polymul(poly_rl, polymul(poly_sp, poly_dr))
    # den = polymul(poly_rs, poly_dr)
    return den


def num_theta():
    poly_t_1 = first_order_tf(t_theta_1)
    poly_t_2 = first_order_tf(t_theta_2)
    num = polymul(polymul(poly_t_1, poly_t_2), a_theta*k_theta)
    return num


def num_phi():
    poly_phi = second_order_tf(zeta_phi, omega_phi)
    num = polymul(poly_phi, a_phi*k_phi)
    return num


def sim_setup_theta():
    num = num_theta()
    den = den_long()
    sys = tf2ss(tf(num, den))
    n_axis = 1
    task = [5, 1, 2]
    t_task = [2, 5, 7, 10, 15]  # start_1, end_1, start_2, end_2, finish
    return sys, n_axis, task, t_task


def sim_setup_phi():
    num = num_phi()
    den = den_lat_dir()
    sys = tf2ss(tf(num, den))
    n_axis = 0
    task = [5, 2, 4]
    t_task = [2, 5, 7, 10, 15]  # start_1, end_1, start_2, end_2, finish
    return sys, n_axis, task, t_task
