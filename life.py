import time
import numpy as np
import matplotlib.pyplot as plt

width = 100
height = 100

class Life:
	def __init__(self):
		self.cells = [[False]*width for i in xrange(height)]

		self.cells[2][3] = True
		self.cells[3][3] = True
		self.cells[4][3] = True
		self.cells[4][5] = True
		self.cells[3][4] = True

	def printCells(self):
		print ""
		for row in self.cells:
			print ""
			for cell in row:
				print "*" if cell else ".",

	def neighbors(self, y, x):
		coords = [(y+i, x+j) for i in xrange(-1, 2) for j in xrange(-1, 2) if i != 0 or j != 0]
		return sum([self.cells[j][i] for j, i in coords])

	def isAlive(self, y, x):
		n = self.neighbors(y, x)
		return n == 3 or (n == 2 and self.cells[y][x])

	def update(self):
		newCells = [[False]*width for i in xrange(height)]

		for i in range(1, height-1):
			for j in range(1, width-1):
				newCells[i][j] = self.isAlive(i, j)
		self.cells = newCells

def play():
	test = Life()
	plt.ion()
	plt.show()
	while True:
		test.update()
		array = np.array(test.cells)
		plt.imshow(array, interpolation='nearest')
		plt.draw()
play()