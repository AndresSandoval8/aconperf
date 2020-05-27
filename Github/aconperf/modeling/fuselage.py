"""Returns force and moment coefficients for fuselages."""
from modeling.aerodynamics import friction_coefficient


def parasite_drag_fuselage(aircraft, mach, altitude):
    """return parasitic drag coefficient of the fuselage."""
    fuselage = aircraft['fuselage']
    s_w = aircraft['wing']['planform']
    s_wet_s = 2 * (fuselage['length'] * fuselage['width']
                   + fuselage['length'] * fuselage['height']
                   + fuselage['height'] * fuselage['width']) / s_w  # []
    c_f = friction_coefficient(mach, altitude, fuselage['length'])  # []
    c_d_0 = 1.25 * c_f * s_wet_s  # []
    return c_d_0
