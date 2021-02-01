import matplotlib as mpl
mpl.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Set maximum iteration
maxIter = 50

# Set Dimension and delta
lenX = lenY = 20 #we set it rectangular
delta = 1

# Boundary conditions
Vtop = 100
Vbottom = 0
Vleft = 0
Vright = 0

# Initial guess of interior grid
Vguess = 25

# Set colour interpolation and colour map.
# colourMap = plt.cm.coolwarm
colorinterpolation = 50
colourMap = plt.cm.jet

# Set meshgrid
X, Y = np.meshgrid(np.arange(0, lenX), np.arange(0, lenY))

# Set array size and set the interior value with Vguess
V = np.empty((lenX, lenY))
V.fill(Vguess)

# Set Boundary condition
V[:1, :] = Vtop
V[(LenY-1):, :] = Vbottom
V[:, (lenX-1):] = Vright
V[:, :1] = Vleft

print(V)

# Iteration (We assume that the iteration is convergence in maxIter = 500)
print("Please wait for a moment")
for iteration in range(0, maxIter):
	for i in range(1, lenX-1, delta):
		for j in range(1, lenY-1, delta):
			V[i, j] = 0.25 * (V[i+1][j] + V[i-1][j] + V[i][j+1] + V[i][j-1])

print("Iteration finished")

# Configure the contour
plt.title("Electric Potential Distribution")
plt.contourf(X, Y, V, colorinterpolation, cmap=colourMap)

# Set Colorbar
plt.colorbar()

# Show the plot
plt.grid()
plt.show()
plt.savefig('Laplace1.png')
