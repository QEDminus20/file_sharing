import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set parameters
A = 1        # Amplitude
lambda_ = 2  # Wavelength
f = 0.01     # Frequency
k = 2 * np.pi / lambda_  # Wave number
omega = 2 * np.pi * f  # Angular frequency

# Define spatial range and time
x = np.linspace(0, 7, 1000)
t_vals = np.linspace(0, 2 * np.pi / f, 400)  # Time sequence

# Create the figure and axes
fig, ax = plt.subplots()
line1, = ax.plot([], [], lw=2, color='r')  # Forward wave (Red)
line2, = ax.plot([], [], lw=2, color='b')  # Backward wave (Blue)
line3, = ax.plot([], [], lw=2, color='g')  # Resulting wave (Green)

ax.set_xlim(0, 7)
ax.set_ylim(-2*A, 2*A)
ax.set_xlabel('x')
ax.set_ylabel('Amplitude y')
ax.set_title('Standing Wave')

# Custom x and y ticks
ax.set_xticks([i * lambda_ / 2 for i in range(8)])  # [0, lambda/2, lambda, ..., 5lambda]
ax.set_xticklabels(['0' if i == 0 else f'${i * lambda_ / 4:.1f}\\lambda$' for i in range(8)])
# Y-axis labels as -2A, -A, 0, A, 2A
ax.set_yticks([-2*A, -A, 0, A, 2*A])  # [-2A, -A, 0, A, 2A]
ax.set_yticklabels(['-2A', '-A', '0', 'A', '2A'])

# Initialization function
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    line3.set_data([], [])
    return line1, line2, line3

# Update function
def update(t):
    # Forward wave (sin(kx - omega*t))
    y1 = A * np.sin(k * x - omega * t)
    # Backward wave (sin(kx + omega*t))
    y2 = A * np.sin(k * x + omega * t)
    # Resulting standing wave
    y3 = y1 + y2

    # Update the data for the three lines
    line1.set_data(x, y1)
    line2.set_data(x, y2)
    line3.set_data(x, y3)

    return line1, line2, line3

# Create the animation
ani = FuncAnimation(fig, update, frames=t_vals, init_func=init, blit=True, interval=50)

# Save the animation as a GIF
ani.save('standing_wave.gif', writer='ffmpeg', fps=20)
