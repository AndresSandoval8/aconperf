from airplanes.models.DC8 import sim_setup_phi, den_lat_dir, num_phi
from control import TransferFunction, forced_response, tf
from controls.frequency_response import bode, root_locus_design
from numpy import interp, pi
from matplotlib import pyplot


num = num_phi()
den = den_lat_dir()
sys = TransferFunction(num, den)

t = [x * 0.01 for x in range(0, 2000)]
t_u = [0, 1.99, 2, 4.99, 5, 7.99, 8, 20]
u_c = [0, 0, -1, -1, 1, 1, 0, 0]
u = interp(t, t_u, u_c)
tout, y, x = forced_response(sys, t, u)
pyplot.plot(t, y[2][:]*180/pi)

bode(sys)
root_locus_design(sys)

num = [[[1., 2.], [3., 4.]], [[5., 6.], [7., 8.]]]
den = [[[9., 8., 7.], [6., 5., 4.]], [[3., 2., 1.], [-1., -2., -3.]]]
sys1 = tf(num, den)


def a(e):
    b = 1+e
    c = 2+e+5
    d = e*2
    return b, c, d
