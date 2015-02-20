import time
import numpy as np
import matplotlib.pyplot as plt

width = 100
height = 100

class Life:
	def __init__(self):
		self.cells = []
		for i in range(height):
			self.cells.append([])
			for j in range(width):
				self.cells[i].append(False)

		self.cells[2][3] = True
		self.cells[3][3] = True
		self.cells[4][3] = True
		self.cells[4][5] = True
		self.cells[3][4] = True

	def printCells(self):
		print ""
		for i in range(1, height-1):
			print ""
			for j in range(1, width-1):
				if self.cells[i][j] == True:
					print "*",
				else:
					print ".",

	def neighbors(self, y, x):
		neighbors = 0
		for i in range(-1,2):
			for j in range(-1,2):
				if not(i==0 and j == 0):
					if self.cells[y+i][x+j] == True:
						neighbors += 1
		return(neighbors)

	def isAlive(self, y, x):
		n = self.neighbors(y, x)
		if self.cells[y][x] == True:
			if n < 2:
				return(False)
			elif n > 3:
				return(False)
			else:
				return(True)
		else:
			if n == 3:
				return(True)
			else:
				return(False)

	def update(self):
		newCells = []
		for i in range(height):
			newCells.append([])
			for j in range(width):
				newCells[i].append(False)

		for i in range(1, height-1):
			for j in range(1, width-1):
				newCells[i][j] = self.isAlive(i, j)
		self.cells = newCells

def play():
	test = Life()
	plt.ion()
	plt.show()
	while(True):
		test.update()
		array = np.array(test.cells)
		plt.imshow(array, interpolation='nearest')
		plt.draw()
play()