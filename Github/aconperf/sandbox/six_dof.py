from airplanes.hydrotransport.H21 import plane
from controls.equationsOfMotion import nonlinear_eom
from controls.forceModel import c_f_m
from controls.trim.trim_long import trim_alpha_de
from matplotlib import pyplot as plt
from numpy import arctan, interp, array, deg2rad, cos, pi, sin

aircraft = plane
altitude = 30000
v = 500
dt = 0.1
t = [x * dt for x in range(0, 100)]
out = trim_alpha_de(aircraft, v, altitude, 0)
AoA = deg2rad(out[0])
u = v*cos(AoA)
w = v*sin(AoA)
de = deg2rad(out[1])
t_u = [0, 1.99, 2, 4.99, 5, 7.99, 8, 20]
u_c = array([0, 0, -0.1, -0.1, 0.1, 0.1, 0, 0])+de
u_c = interp(t, t_u, u_c)
g = 32.174
c = array([0, 0, 0, 0, 0, 0])
j = aircraft['weight']['inertia']
m = aircraft['weight']['weight']/g
x = array([float(u), 0, float(w), 0, float(AoA), 0, 0, 0, 0, 0, 0, altitude])

v_x = []
alpha = []
theta = []
gamma = []
q = []

h = []
ii = 1
for it in t:
    dxdt = nonlinear_eom(x, m, j, c, g)
    x = x + dxdt * dt
    u = array([0, u_c[ii-1], 0])
    c = c_f_m(aircraft, x, u)
    v_x.append(x[1])
    alpha.append(180/pi*arctan(x[2]/x[0]))
    theta.append(180/pi*x[4])
    gamma.append(180/pi*(x[4]-arctan(x[2]/x[0])))
    q.append(180/pi*x[7])
    h.append(x[4])
    ii = ii + 1

plt.figure(figsize=(8, 8))
plt.subplot(4, 1, 1)
plt.plot(t, v_x)
plt.ylim((-50, 50))

plt.subplot(4, 1, 2)
plt.plot(t, alpha)
plt.plot(t, theta)
plt.plot(t, gamma)
plt.ylim((-10, 10))

plt.subplot(4, 1, 3)
plt.plot(t, q)
plt.ylim((-40, 40))

plt.subplot(4, 1, 4)
plt.plot(t, u_c)
plt.ylim((-0.5, 0.5))
plt.show()
