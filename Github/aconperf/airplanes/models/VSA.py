from numpy import polymul


def denominator_longitudinal():
    """longitudinal denominator."""
    zeta_sp = 0.5
    omega_sp = 2
    zeta_ph = 0.05
    omega_ph = 0.15

    poly_sp = [1, 2 * zeta_sp * omega_sp, omega_sp ** 2]
    poly_ph = [1, 2 * zeta_ph * omega_ph, omega_ph ** 2]

    den = polymul(poly_ph, poly_sp)
    return den


def numerator_theta():
    """pitch angle numerator."""
    a_theta = -1.5
    t_theta_1 = 15
    t_theta_2 = 2
    k_theta = -1

    poly_theta_1 = [1, 1 / t_theta_1]
    poly_theta_2 = [1, 1 / t_theta_2]
    num_theta = polymul(polymul(poly_theta_1, poly_theta_2), a_theta * k_theta)
    return num_theta
