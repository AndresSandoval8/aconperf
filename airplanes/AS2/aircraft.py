"""AS squared airplane geometry file."""
plane = {
    'wing': {
        'type': 'wing',
        'planform': 5,
        'aspect_ratio': 5,
        'sweep_LE': 0,
        'taper': 1,
        'dihedral': 3,
        'station': 1,
        'buttline': 0,
        'waterline': 0.1,
        'incidence': 0,
        'c_l_alpha': 6.28,
        'alpha_zero_lift': 0
    },
    'horizontal': {
        'type': 'wing',
        'planform': 1,
        'aspect_ratio': 3,
        'sweep_LE': 30,
        'taper': 0.5,
        'dihedral': 0,
        'station': 4,
        'buttline': 0,
        'waterline': 0.3,
        'incidence': 0,
    },
    'vertical': {
        'type': 'vertical',
        'planform': 1,
        'aspect_ratio': 3,
        'sweep_LE': 30,
        'taper': 0.5,
        'station': 4,
        'buttline': 0,
        'waterline': 0.3,
    },
    'elevator': {
        'type': 'control_surface',
        'parent': 'horizontal',
        'limits': [-15, 15]
    },
    'aileron_l': {
        'type': 'control_surface',
        'parent': 'wing',
        'limits': [-15, 15]
    },
    'aileron_r': {
        'type': 'control_surface',
        'parent': 'wing',
        'limits': [-15, 15]
    },
    'flap_l': {
        'type': 'control_surface',
        'parent': 'wing',
        'limits': [-30, 0]
    },
    'flap_r': {
        'type': 'control_surface',
        'parent': 'wing',
        'limits': [-30, 0]
    },
    'spoiler_l': {
        'type': 'control_surface',
        'parent': 'wing',
        'limits': [0, 70]
    },
    'spoiler_r': {
        'type': 'control_surface',
        'parent': 'wing',
        'limits': [0, 70]
    },
    'rudder': {
        'type': 'control_surface',
        'parent': 'vertical',
        'limits': [-15, 15]
    }
}
