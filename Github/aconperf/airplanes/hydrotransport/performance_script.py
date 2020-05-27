from numpy import array
from performance.constraint import master_constraint, takeoff, stall_speed
from airplanes.hydrotransport.H21 import plane
from matplotlib import pyplot as plt

wing_loading = array([20, 30, 40, 50, 60, 70, 80, 90])
aircraft = plane

cruise_mach = 0.8
cruise_alt = 20000
stall_mach = 0.18
turn_mach = 0.5
n_max = 2.5
gamma_max = 10
v_gamma = 0.3
c_l_max = 1.4

t_w_c = master_constraint(aircraft, wing_loading, cruise_mach, cruise_alt, 1, 0, 0)
t_w_g = master_constraint(aircraft, wing_loading, v_gamma, cruise_alt, 1, gamma_max, 0)
t_w_t = master_constraint(aircraft, wing_loading, turn_mach, cruise_alt, n_max, 0, 0)
w_s_s = stall_speed(stall_mach,  0, c_l_max, 1, 0)
t_w_to = takeoff(aircraft, wing_loading, 3000, 0, 0.02)

plt.plot(wing_loading, t_w_c, label='cruise')
plt.plot(wing_loading, t_w_g, label='climb')
plt.plot(wing_loading, t_w_t, label='turn')
plt.plot(wing_loading, t_w_to, label='takeoff')
plt.plot([w_s_s, w_s_s], [0, 1], label='stall')
plt.ylabel('Thrust Loading')
plt.xlabel('Wing Loading [lb/sqft]')
plt.legend()
plt.show()
