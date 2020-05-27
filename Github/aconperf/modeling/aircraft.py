"""Returns force and moment coefficients for total aircraft."""
from modeling.fuselage import parasite_drag_fuselage
from modeling.lifting_surface import aerodynamic_center, c_l_alpha_wing, d_epsilon_d_alpha, parasite_drag
from modeling.trapezoidal_wing import mac
from numpy import pi, deg2rad


def c_l_zero(aircraft, mach):
    """baseline lift coefficient."""
    wing = aircraft['wing']
    s_w = wing['planform']  # [ft^2]
    c_l_alpha_w = c_l_alpha_wing(wing, mach)  # [1/rad]
    ht = aircraft['horizontal']
    s_ht = ht['planform']  # [ft^2]
    c_l_alpha_ht = c_l_alpha_wing(ht, mach)  # [1/rad]
    c_l_0_w = c_l_alpha_w * (deg2rad(wing['incidence'] - wing['alpha_zero_lift']))  # []
    epsilon = 2 * c_l_0_w / (pi * wing['aspect_ratio'])  # [rad]
    c_l_0_ht = c_l_alpha_ht * s_ht / s_w * (deg2rad(ht['incidence'] - ht['alpha_zero_lift'] - epsilon))  # []
    c_l_0 = c_l_0_w + c_l_0_ht  # []
    return c_l_0


def c_l_alpha(aircraft, mach):
    """returns lift curve slope for aircraft."""
    wing = aircraft['wing']
    s_w = wing['planform']  # [ft^2]
    c_l_alpha_w = c_l_alpha_wing(wing, mach)  # [1/rad]
    ht = aircraft['horizontal']
    s_ht = ht['planform']  # [ft^2]
    c_l_alpha_ht = c_l_alpha_wing(ht, mach)  # [1/rad]
    downwash = d_epsilon_d_alpha(wing, ht, mach)  # []
    c_l_alpha_airplane = c_l_alpha_w + c_l_alpha_ht*s_ht/s_w*(1-downwash)  # [1/rad]
    return c_l_alpha_airplane


def c_l_delta_elevator(aircraft, mach):
    """returns lift curve of elevator wrt deflection angle."""
    ht = aircraft['horizontal']
    s_ht = ht['planform']  # [ft^2]
    wing = aircraft['wing']
    s_w = wing['planform']  # [ft^2]
    c_l_alpha_ht = c_l_alpha_wing(ht, mach)  # [1/rad]
    tau = aircraft['elevator']['chord_ratio']
    c_l_de = c_l_alpha_ht * s_ht / s_w * tau  # [1/rad]
    return c_l_de


def c_l_pitch_rate(aircraft, mach):
    """returns lift curve of elevator wrt pitch rate."""
    wing = aircraft['wing']
    s_w = wing['planform']  # [ft^2]
    c_bar = mac(wing['aspect_ratio'], s_w, wing['taper'])  # [ft]
    cg_bar = aircraft['weight']['cg'][0] / c_bar  # []
    ht = aircraft['horizontal']
    s_ht = ht['planform']  # [ft^2]
    c_l_alpha_ht = c_l_alpha_wing(ht, mach)  # [1/rad]
    x_ac_ht = aerodynamic_center(ht)  # [ft]
    x_ac_ht_bar = x_ac_ht / c_bar  # []
    c_l_q = 2 * c_l_alpha_ht * s_ht / s_w * (x_ac_ht_bar - cg_bar)
    return c_l_q


def c_l_alpha_dot(aircraft, mach):
    """returns lift curve of elevator wrt alpha rate."""
    wing = aircraft['wing']
    s_w = wing['planform']  # [ft^2]
    c_bar = mac(wing['aspect_ratio'], s_w, wing['taper'])  # [ft]
    cg_bar = aircraft['weight']['cg'][0] / c_bar  # []
    ht = aircraft['horizontal']
    s_ht = ht['planform']  # [ft^2]
    c_l_alpha_ht = c_l_alpha_wing(ht, mach)  # [1/rad]
    x_ac_ht = aerodynamic_center(ht)  # [ft]
    x_ac_ht_bar = x_ac_ht / c_bar  # []
    downwash = d_epsilon_d_alpha(wing, ht, mach)  # []
    c_l_adt = 2 * c_l_alpha_ht * s_ht / s_w * (x_ac_ht_bar - cg_bar) * downwash
    return c_l_adt


def c_m_zero(aircraft, mach, altitude):
    """baseline lift coefficient."""
    wing = aircraft['wing']
    s_w = wing['planform']  # [ft^2]
    c_l_alpha_w = c_l_alpha_wing(wing, mach)  # [1/rad]
    ht = aircraft['horizontal']
    s_ht = ht['planform']  # [ft^2]
    c_l_alpha_ht = c_l_alpha_wing(ht, mach)  # [1/rad]
    vt = aircraft['vertical']
    s_vt = vt['planform']  # [ft^2]

    c_bar = mac(wing['aspect_ratio'], s_w, wing['taper'])  # [ft]
    cg_bar = aircraft['weight']['cg'][0] / c_bar  # []
    z_cg = aircraft['weight']['cg'][2]

    x_ac_w = aerodynamic_center(wing)  # [ft]
    x_ac_w_bar = x_ac_w / c_bar  # []

    x_ac_ht = aerodynamic_center(ht)  # [ft]
    x_ac_ht_bar = x_ac_ht / c_bar  # []

    c_l_0_w = c_l_alpha_w * (deg2rad(wing['incidence'] - wing['alpha_zero_lift']))  # []
    c_m_0_w = c_l_0_w * (cg_bar - x_ac_w_bar)
    epsilon = 2 * c_l_0_w / (pi * wing['aspect_ratio'])  # [rad]
    c_l_0_ht = c_l_alpha_ht * s_ht / s_w * (deg2rad(ht['incidence'] - ht['alpha_zero_lift'] - epsilon))  # []

    z_w = (z_cg - wing['waterline']) / c_bar
    z_ht = (z_cg - ht['waterline']) / c_bar
    z_vt = (z_cg - vt['waterline']) / c_bar
    z_f = (z_cg - aircraft['fuselage']['height'] / 2) / c_bar

    c_m_0_w_d = - parasite_drag(wing, mach, altitude) * z_w
    c_m_0_ht_d = - parasite_drag(ht, mach, altitude) * s_ht / s_w * z_ht
    c_m_0_vt_d = - parasite_drag(vt, mach, altitude) * s_vt / s_w * z_vt
    c_m_0_f_d = - parasite_drag_fuselage(aircraft, mach, altitude) * z_f
    c_m_0_ht = c_l_0_ht * (x_ac_ht_bar - cg_bar)
    c_m_0 = (wing['airfoil_cm0'] + ht['airfoil_cm0'] + c_m_0_w + c_m_0_ht
             + c_m_0_w_d + c_m_0_ht_d + c_m_0_vt_d + c_m_0_f_d)  # []
    return c_m_0


def c_m_alpha(aircraft, mach):
    """returns pitching moment curve slope for aircraft."""
    wing = aircraft['wing']
    s_w = wing['planform']  # [ft^2]
    c_bar = mac(wing['aspect_ratio'], s_w, wing['taper'])  # [ft]
    cg_bar = aircraft['weight']['cg'][0] / c_bar  # []
    x_ac_w = aerodynamic_center(wing)  # [ft]
    x_ac_w_bar = x_ac_w / c_bar  # []
    ht = aircraft['horizontal']
    s_ht = ht['planform']  # [ft^2]
    c_l_alpha_ht = c_l_alpha_wing(ht, mach)  # [1/rad]
    downwash = d_epsilon_d_alpha(wing, ht, mach)  # []
    c_l_alpha_w = c_l_alpha_wing(wing, mach)  # [1/rad]
    x_ac_ht = aerodynamic_center(ht)  # [ft]
    x_ac_ht_bar = x_ac_ht / c_bar  # []
    c_m_alpha_w = c_l_alpha_w * (cg_bar - x_ac_w_bar)  # [1/rad]
    c_m_alpha_ht = c_l_alpha_ht * s_ht / s_w * (1 - downwash) * (x_ac_ht_bar - cg_bar)  # [1/rad]
    c_m_alpha_airplane = c_m_alpha_w - c_m_alpha_ht  # [1/rad]
    return c_m_alpha_airplane


def c_m_delta_elevator(aircraft, mach):
    """returns pitching moment curve of elevator wrt deflection angle."""
    wing = aircraft['wing']
    s_w = wing['planform']  # [ft^2]
    c_bar = mac(wing['aspect_ratio'], s_w, wing['taper'])  # [ft]
    cg_bar = aircraft['weight']['cg'][0] / c_bar  # []
    ht = aircraft['horizontal']
    s_ht = ht['planform']  # [ft^2]
    c_l_alpha_ht = c_l_alpha_wing(ht, mach)  # [1/rad]
    downwash = d_epsilon_d_alpha(wing, ht, mach)  # []
    x_ac_ht = aerodynamic_center(ht)  # [ft]
    x_ac_ht_bar = x_ac_ht / c_bar  # []
    tau = aircraft['elevator']['chord_ratio']
    c_m_de = - c_l_alpha_ht * s_ht / s_w * (1 - downwash) * (x_ac_ht_bar - cg_bar) * tau  # [1/rad]
    return c_m_de


def c_m_pitch_rate(aircraft, mach):
    """returns pitching moment curve of elevator wrt pitch rate."""
    wing = aircraft['wing']
    s_w = wing['planform']  # [ft^2]
    c_bar = mac(wing['aspect_ratio'], s_w, wing['taper'])  # [ft]
    cg_bar = aircraft['weight']['cg'][0] / c_bar  # []
    ht = aircraft['horizontal']
    s_ht = ht['planform']  # [ft^2]
    c_l_alpha_ht = c_l_alpha_wing(ht, mach)  # [1/rad]
    x_ac_ht = aerodynamic_center(ht)  # [ft]
    x_ac_ht_bar = x_ac_ht / c_bar  # []
    c_m_q = - 2 * c_l_alpha_ht * s_ht / s_w * (x_ac_ht_bar - cg_bar) ** 2
    return c_m_q


def c_m_alpha_dot(aircraft, mach):
    """returns pitch moment curve of elevator wrt alpha rate."""
    wing = aircraft['wing']
    s_w = wing['planform']  # [ft^2]
    c_bar = mac(wing['aspect_ratio'], s_w, wing['taper'])  # [ft]
    cg_bar = aircraft['weight']['cg'][0] / c_bar  # []
    ht = aircraft['horizontal']
    s_ht = ht['planform']  # [ft^2]
    c_l_alpha_ht = c_l_alpha_wing(ht, mach)  # [1/rad]
    x_ac_ht = aerodynamic_center(ht)  # [ft]
    x_ac_ht_bar = x_ac_ht / c_bar  # []
    downwash = d_epsilon_d_alpha(wing, ht, mach)  # []
    c_m_adt = - 2 * c_l_alpha_ht * s_ht / s_w * downwash * (x_ac_ht_bar - cg_bar) ** 2
    return c_m_adt


def c_d_zero(aircraft, mach, altitude):
    wing = aircraft['wing']
    s_w = wing['planform']  # [ft^2]
    ht = aircraft['horizontal']
    s_ht = ht['planform']  # [ft^2]
    vt = aircraft['vertical']
    s_vt = vt['planform']  # [ft^2]
    c_d_0_w = parasite_drag(wing, mach, altitude)
    c_d_0_ht = parasite_drag(ht, mach, altitude) * s_ht / s_w
    c_d_0_vt = parasite_drag(vt, mach, altitude) * s_vt / s_w
    c_d_0_f = parasite_drag_fuselage(aircraft, mach, altitude)
    c_d_0 = c_d_0_w + c_d_0_ht + c_d_0_vt + c_d_0_f
    return c_d_0
