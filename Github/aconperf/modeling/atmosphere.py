"""Standard atmosphere model."""
from numpy import exp, sqrt
gas_constant = 1716.5  # ft*lb/(slug*R)
gamma = 1.4  # []


def air_density(altitude):
    """return air density wrt altitude."""
    p = pressure(altitude)  # psf
    t = temperature(altitude)  # R
    rho = p/(gas_constant*t)  # lb/ft3
    return rho


def pressure(altitude):
    """return ambient pressure wrt altitude."""
    t = temperature(altitude)  # R
    if altitude <= 36152:
        p = 2116*(t/518.6)**5.256  # psf
    else:
        p = 473.1*exp(1.73-0.000048*altitude)  # psf
    return p


def speed_of_sound(altitude):
    """return speed of sound wrt altitude."""
    t = temperature(altitude)  # R
    a = sqrt(gamma*gas_constant*t)  # [ft/s]
    return a


def temperature(altitude):
    """return ambient temperature wrt altitude."""
    if altitude <= 36152:
        t = 59-0.00356*altitude  # deg F
    else:
        t = -70  # deg F
    t = t + 459.7  # R
    return t


def viscosity(altitude):
    """return dynamic viscosity of air wrt altitude."""
    t_ref = temperature(0)  # R
    t = temperature(altitude)  # R
    s = 198.72  # R
    mu_ref = 3.737 * 10 ** (-7)  # [slug/(ft*s)]
    mu = mu_ref*((t/t_ref)**(3/2))*(t_ref + s)/(t + s)  # [slug/(ft*s)]
    return mu
