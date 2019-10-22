from control import bode, tf
from matplotlib import pyplot

sys = tf([1., 1.7], [1., 1., 20])
mag, phase, omega = bode(sys)
pyplot.figure()
pyplot.plot(phase, mag, label='linear')
pyplot.show()