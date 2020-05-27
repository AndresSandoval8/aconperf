import matplotlib.pyplot as plt
import pygame
import time
from numpy import matrix, zeros, max, min

from airplanes.models.DC8 import sim_setup_theta
sys, n_axis, task, t_task = sim_setup_theta()

pygame.init()
# Loop until the user clicks the close button.
done = False

# Initialize the joysticks.
pygame.joystick.init()

# -------- Main Program Loop -----------
in_tf = []
t = []
out = []
u = []
axis = [0, 0]
x = matrix(zeros((sys.A.shape[0], 1)))
t_0 = time.time()
plt.style.use('fivethirtyeight')
joystick = pygame.joystick.Joystick(0)
joystick.init()
plt.figure(figsize=(8, 8))

while not done:
    t.append(time.time() - t_0)
    for event in pygame.event.get():  # User did something.
        if event.type == pygame.QUIT:  # If user clicked close.
            done = True  # Flag that we are done so we exit this loop.
        elif event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        elif event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")

    axis[0] = joystick.get_axis(0)
    axis[1] = joystick.get_axis(1)

    in_tf.append(axis[n_axis])

    if len(t) == 1:
        out.append(0)
    else:
        u = in_tf[-1]
        dxdt = sys.A @ x + sys.B * u
        dt = t[-1] - t[-2]
        x = x + dxdt * dt
        y = sys.C @ x + sys.D * u
        out.append(y)

    plt.subplot(2, 1, 1)
    plt.cla()
    plt.plot(t, out)
    plt.plot([0, 500], [task[0], task[0]], 'g--', linewidth=1)
    plt.plot([0, 500], [task[0]-task[1], task[0]-task[1]], 'y--', linewidth=1)
    plt.plot([0, 500], [task[0] + task[1], task[0] + task[1]], 'y--', linewidth=1)
    plt.plot([0, 500], [task[0] - task[2], task[0] - task[2]], 'r--', linewidth=1)
    plt.plot([0, 500], [task[0] + task[2], task[0] + task[2]], 'r--', linewidth=1)
    plt.plot([0, 500], [0, 0], 'k--', linewidth=1)
    plt.ylim((min([-5, min(out)])-3,
              max([15, max(out)])+3))
    plt.xlim((t[-1]-10, t[-1]+10))

    plt.subplot(2, 1, 2)
    plt.cla()
    plt.plot(t, in_tf)
    plt.ylim((min([0, min(in_tf)])-0.5, max([0, max(in_tf)])+0.5))
    plt.xlim((t[-1] - 10, t[-1] + 10))
    plt.pause(0.000001)

pygame.quit()
