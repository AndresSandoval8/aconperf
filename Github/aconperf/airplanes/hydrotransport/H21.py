"""airplane geometry file."""
plane = {
    'wing': {
        'type': 'wing',
        'planform': 2884,  # [ft^2]
        'aspect_ratio': 8,  # []
        'sweep_LE': 15,  # [deg]
        'taper': 0.5,  # []
        'dihedral': 3,  # [deg]
        'station': 42.6,  # [ft]
        'buttline': 0,  # [ft]
        'waterline': 0.198,  # [ft]
        'incidence': 0,  # [deg]
        'c_l_alpha': 5,  # [1/rad]
        'alpha_zero_lift': -1,  # [deg]
        'airfoil_thickness': 0.15,  # []
        'airfoil_cm0': 0  # []
    },
    'horizontal': {
        'type': 'wing',
        'planform': 300,  # [ft^2]
        'aspect_ratio': 3.5,  # []
        'sweep_LE': 30,  # [deg]
        'taper': 0.465,  # []
        'dihedral': 0,  # [deg]
        'station': 135,  # [ft]
        'buttline': 0,  # [ft]
        'waterline': 10,  # [ft]
        'incidence': 0,  # [deg]
        'c_l_alpha': 5,  # [1/rad]
        'alpha_zero_lift': 0,  # [deg]
        'airfoil_thickness': 0.1,  # []
        'airfoil_cm0': 0  # []
    },
    'vertical': {
        'type': 'vertical',
        'planform': 150,  # [ft^2]
        'aspect_ratio': 4,  # []
        'sweep_LE': 30,  # [deg]
        'taper': 0.5,  # []
        'station': 125,  # [ft]
        'buttline': 0,  # [ft]
        'waterline': 0.3,  # [ft]
        'airfoil_thickness': 0.15  # []
    },
    'elevator': {
        'type': 'control_surface',
        'parent': 'horizontal',
        'limits': [-15, 15],  # [deg]
        'chord_ratio': 0.37,  # []
    },
    'aileron_l': {
        'type': 'control_surface',
        'parent': 'wing',
        'limits': [-15, 15]  # [deg]
    },
    'aileron_r': {
        'type': 'control_surface',
        'parent': 'wing',
        'limits': [-15, 15]  # [deg]
    },
    'rudder': {
        'type': 'control_surface',
        'parent': 'vertical',
        'limits': [-15, 15],  # [deg]
        'chord_ratio': 0.2  # []
    },
    'fuselage': {
        'length': 140,  # [ft]
        'width': 10,  # [ft]
        'height': 10  # [ft]
    },
    'weight': {
        'weight': 150826,  # [lb]
        'inertia': [[3000000, 0, 28000], [0, 290000, 0], [28000, 0, 5500000]],  # [slug*ft^2]
        'cg': [55, 0, 0.18]  # [ft]
    }
}
