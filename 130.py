import numpy as np
import matplotlib.pyplot as plt

# Define Madelbrot functions
def mandelbrot(c,max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def render_mandelbrot(x_center, y_center, x_width, y_width, width, height, max_iter):
    x = np.linspace(x_center - x_width/2, x_center + x_width/2, width)
    y = np.linspace(y_center - y_width/2, y_center + y_width/2, height)
    C = np.array(np.meshgrid(x, y)).T.reshape(-1, 2)
    values = np.array([mandelbrot(complex(c[0], c[1]), max_iter) for c in C])
    return values.reshape(width, height)

# Define two points of interest in Elephant Valley
point1 = (0.275, 0.005)
point2 = (0.290, 0.017)

# Calculate 7 transition coordinates
x_transitions = np.linspace(point1[0], point2[0], 7)
y_transitions = np.linspace(point1[1], point2[1], 7)

# Combine starting point, transitions, and end point
x_coords = np.hstack(([point1[0]], x_transitions, [point2[0]]))
y_coords = np.hstack(([point1[1]], y_transitions, [point2[1]]))

# Plot the transitions
fig, axes = plt.subplots(3, 3, figsize=(10, 10))
for ax, x, y in zip(axes.ravel(), x_coords, y_coords):
    image = render_mandelbrot(x, y, 0.005, 0.005, 500, 500, 2000)  # Doubled the iterations
    ax.imshow(image, cmap='cubehelix_r', extent=[x-0.0025, x+0.0025, y-0.0025, y+0.0025])
    ax.set_title(f"x: {x:.5f}, y: {y:.5f}")
    ax.axis('off')

plt.tight_layout()
fig.suptitle("Transitions in Elephant Valley of Mandelbrot Set", fontsize=16, y=1.05)
plt.show()