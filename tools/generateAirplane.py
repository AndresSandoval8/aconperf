import importlib
from modeling.lifting_surface import lift


def get_aerodynamics(plane_string):
    """get aircraft aerodynamics model."""
    airplane_name = "airplanes.%s.aircraft" % plane_string
    state_name = "airplanes.%s.states" % plane_string
    airplane_module = importlib.import_module(airplane_name)
    states = importlib.import_module(state_name)
    airplane = airplane_module.plane

    c_l = []
    for iM in states.mach:
        for iA in states.alpha:
            c_l_wing = lift(airplane['wing'], iM, iA/57.3)
            c_l.append(c_l_wing)

    return c_l
