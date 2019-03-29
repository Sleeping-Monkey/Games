from graphics import *

def makeCube(x1, y1, x2, y2) :
	return Rectangle(Point(x1, y1), Point(x2, y2))

def makeCircle(x, y, r) :
	return Circle(Point(x, y), r)

class Field:

	def __init__(self, fileName, win):
		self.setTable(fileName)
		self.setDraw(win)

	def setTable(self, fileName) :
		f = open(fileName, 'r')
		strings = f.read().split('\n')
		n = len(strings)
		self.table = []
		for i in range(n - 1) :
			self.table.append(strings[i])
		for i in range(len(self.table)) :
			print(self.table[i])

	def getCountOfCell(self) :
		return len(self.table)
		
	def setDraw(self, win) :
		self.flagOfDrawing = False
		W = win.width
		H = win.height
		n = len(self.table)
		w = W // n
		h = H // n
		size = min(w, h)
		self.allDraw = []
		for i in range(n) :
			for j in range(n) :
				cube = makeCube(j * h, i * w, (j + 1) * h, (i + 1) * w)
				if self.table[i][j] == 'x' :
					cube.setFill(color_rgb(0, 0, 255))
					cube.setOutline(color_rgb(0, 0, 255))
				else :
					cube.setFill(color_rgb(0, 0, 0))
					cube.setOutline(color_rgb(0, 0, 0))
				self.allDraw.append(cube)
#			cube.draw(win)
	def getPositionOfPerson(self) :
		n = len(self.table)
		for i in range(n) :
			for j in range(n) :
				if self.table[i][j] == 's' :
					return [i, j]	

	def getPositionOfDoor(self) :
		n = len(self.table)
		for i in range(n) :
			for j in range(n) :
				if self.table[i][j] == 'f' :
					return [i, j]
	
	def draw(self, win) :
		if self.flagOfDrawing == True :
			return
		self.flagOfDrawing = True
		m = len(self.allDraw)
		for i in range(m) :
			self.allDraw[i].draw(win)

class Character :

	def setPositionPerson(self, x, y) :
		self.flagOfDrawing = False
		self.personX = x
		self.personY = y

	def setPositionDoor(self, x, y) :
		self.doorX = x
		self.doorY = y

	def setDraw(self, countOfCell, win) :
		W = win.width
		H = win.height
		w = W // countOfCell
		h = H // countOfCell
		size = min(w, h)
		self.person = makeCircle(self.personY * h + size // 2, self.personX * w + size // 2, size // 2)
		self.person.setOutline(color_rgb(0, 255, 0))
		self.person.setFill(color_rgb(0, 255, 0))
		dist = countOfCell // 4
		self.door = makeCube(self.doorY * h + dist, self.doorX * w + dist, (self.doorY + 1) * h - dist, (self.doorX + 1) * w - dist)
		self.door.setOutline(color_rgb(255, 0, 0))
		self.door.setFill(color_rgb(255, 0, 0))

	def draw(self, win) :
		if self.flagOfDrawing == True :
			return
		self.flagOfDrawing = True
		self.person.draw(win)
		self.door.draw(win)

class Game :

	def __init__(self, fileName, win):
		self.setField(fileName, win)
		self.setPerson()
		self.setDraw(win)

	def setField(self, fileName, win) :
		self.field = Field(fileName, win)

	def setPerson(self) :
		x, y = self.field.getPositionOfPerson()
		self.hero = Character()
		self.hero.setPositionPerson(x, y)
		x, y = self.field.getPositionOfDoor()
		self.hero.setPositionDoor(x, y) 

	def setDraw(self, win) :
		self.field.setDraw(win)
		count = self.field.getCountOfCell()
		self.hero.setDraw(count, win)

	def changePositionOfPerson(self, key, win) :
		if key == 'Up' :
			if self.field.table[self.hero.personX - 1][self.hero.personY] == 'f' :
				self.hero.setPositionPerson(self.hero.personX - 1, self.hero.personY)
				self.setDraw(win)
				return False
				#finish game
			elif not self.field.table[self.hero.personX - 1][self.hero.personY] == 'x' :
				self.hero.setPositionPerson(self.hero.personX - 1, self.hero.personY)
				self.setDraw(win)
		if key == 'Down' :
			if self.field.table[self.hero.personX + 1][self.hero.personY] == 'f' :
				self.hero.setPositionPerson(self.hero.personX + 1, self.hero.personY)
				self.setDraw(win)
				return False
				#finish game
			elif not self.field.table[self.hero.personX + 1][self.hero.personY] == 'x' :
				self.hero.setPositionPerson(self.hero.personX + 1, self.hero.personY)
				self.setDraw(win)
		if key == 'Right' :
			if self.field.table[self.hero.personX][self.hero.personY + 1] == 'f' :
				self.hero.setPositionPerson(self.hero.personX, self.hero.personY + 1)
				self.setDraw(win)
				return False
				#finish game
			elif not self.field.table[self.hero.personX][self.hero.personY + 1] == 'x' :
				self.hero.setPositionPerson(self.hero.personX, self.hero.personY + 1)
				self.setDraw(win)
		if key == 'Left' :
			if self.field.table[self.hero.personX][self.hero.personY - 1] == 'f' :
				self.hero.setPositionPerson(self.hero.personX, self.hero.personY - 1)
				self.setDraw(win)
				return False
				#finish game
			elif not self.field.table[self.hero.personX][self.hero.personY - 1] == 'x' :
				self.hero.setPositionPerson(self.hero.personX, self.hero.personY - 1)
				self.setDraw(win)
		return True

	def draw(self, win) :
		self.field.draw(win)
		self.hero.draw(win)


def main():
	win = GraphWin("My Game", 500, 500)
	win.setBackground(color_rgb(255, 0, 0))
	
	game = Game('table.in', win)
	game.draw(win)

	flag = True

	while flag:
		key = win.getKey()
		print(key)
		flag = game.changePositionOfPerson(key, win)
		game.draw(win)

	win.setBackground(color_rgb(255, 0, 0))
	txt = Text(Point(250, 250), "You win!\n Click anywhere.")
	txt.setSize(30)
	txt.setTextColor(color_rgb(255, 0, 100))
	txt.draw(win)

	win.getMouse() # Pause to view result
	win.close()    # Close window when done

main()
