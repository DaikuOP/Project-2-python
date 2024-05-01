import matplotlib.pyplot as plt

from random_walk import RandomWalk
fig, ax = plt.subplots(figsize = (15, 9), dpi = 110)


rw = RandomWalk(5000)
rw.fill_walk()
print(rw.x_values, rw.y_values)
plt.style.use("seaborn-v0_8-pastel")
points = range(rw.num_points)

#Starting point and end point
ax.scatter(0, 0, c='blue', edgecolors = 'none', s = 100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='green', edgecolors = 'none', s = 100)

ax.plot(rw.x_values, rw.y_values, c='grey', linewidth = 1)

ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.savefig('Molecular motion.png')
plt.show()