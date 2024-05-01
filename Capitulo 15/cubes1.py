import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.tick_params(axis= "both", labelsize=14)

#Primeros 5000
x_values = range(1, 5000)
y_values = [ _**3 for _ in x_values]

ax.scatter(x_values, y_values, c='red', 
#cmap=plt.cm.Reds
)
# Set the range for each axis.
ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)
plt.style.use('seaborn-v0_8-pastel')


plt.savefig('cubes_plot.png')
plt.show()
