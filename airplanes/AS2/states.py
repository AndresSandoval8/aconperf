"""Provides states for aircraft model."""
from numpy import linspace

mach = linspace(0.001, 0.1, 20)
alpha = linspace(-5, 15, 21)
beta = linspace(-15, 15, 11)

p = linspace(-0.1, 0.1, 3)
q = linspace(-0.001, 0.001, 3)
r = linspace(-0.01, 0.01, 3)
