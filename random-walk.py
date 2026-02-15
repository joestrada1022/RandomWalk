import matplotlib.pyplot as plt
import numpy as np

# np.random.seed(12)

def random_walk1D(num_steps):
    y = 0
    t = np.arange(num_steps + 1)
    positions = [y]
    directions = [-1, 1]
    for _ in range(num_steps):
        step = np.random.choice(directions)

        y += step

        positions.append(y)
    
    return t, positions



fig, ax = plt.subplots(2)

# generate unique colors
colors1 = plt.cm.viridis(np.linspace(0, 1, 30000))
colors2 = plt.cm.viridis(np.linspace(0, 1, 50))

for i in range(30000):
    walk = random_walk1D(50)
    ax[0].plot(walk[0], walk[1], color=colors1[i])

for i in range(50):
    walk = random_walk1D(30000)
    ax[1].plot(walk[0], walk[1], color=colors2[i])

fig.suptitle('More Walk vs. More Step')
plt.show()