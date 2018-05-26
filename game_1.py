from graphics import *

def makeCube(x1, y1, x2, y2):
    return Rectangle(Point(x1, y1), Point(x2, y2))

class Cross:
    def __init__(self, x1, y1, x2, y2):
        self.line_one = Line(Point(x1, y1), Point(x2, y2))
        self.line_one.setFill(color_rgb(0, 255, 0))
        self.line_two = Line(Point(x1, y2), Point(x2, y1))
        self.line_two.setFill(color_rgb(0, 255, 0))

    def draw(self, win):
        self.line_one.draw(win)
        self.line_two.draw(win)

class Table:
    def __init__(self, size, win):
        self.table = []
        self.size = size
        W = win.width
        H = win.height
        self.w = W / size
        self.h = H / size

        for i in range(size):
            str = '0' * size
            self.table.append(str)
        self.setDrawing()

    def setDrawing(self):
        self.allDrawing = []
        for i in range(self.size):
            for j in range(self.size):
                cube = makeCube(i * self.h, j * self.w, (i + 1) * self.h, (j + 1) * self.w)
                cube.setOutline(color_rgb(0, 0, 0))
                self.allDrawing.append(cube)
                if self.table[i][j] == 'x':
                    cross = Cross(i * self.h, j * self.w, (i + 1) * self.h, (j + 1) * self.w)
                    self.allDrawing.append(cross)
                if self.table[i][j] == 'o':
                    circle = Circle(Point(i * self.h + self.h // 2, j * self.w + self.w // 2), min(self.w, self.h) // 2)
                    circle.setOutline(color_rgb(0, 255, 0))
                    self.allDrawing.append(circle)

    def changeTable(self, x, y, id):
        if self.table[x][y] == '0':
            self.table[x] = self.table[x][:y] + id + self.table[x][y + 1:]
            print(self.table[x])
            self.setDrawing()
            return True
        else:
            return False

    def checkTable(self, id):
        maxOfId = 0
        positionOfMaxId = [-1, -1]
        nOfMaxId = 0
        for i in range(self.size):
            count = 0
            j = 0
            while j < self.size:
                if self.table[i][j] == id:
                    count += 1
                else:
                    if maxOfId < count:
                        maxOfId = count
                        positionOfMaxId[0] = i
                        positionOfMaxId[1] = j - 1
                        nOfMaxId = 1
                    count = 0
                if j == self.size - 1:
                    if maxOfId < count:
                        maxOfId = count
                        positionOfMaxId[0] = i
                        positionOfMaxId[1] = j
                        nOfMaxId = 1
                j += 1

        for j in range(self.size):
            count = 0
            i = 0
            while i < self.size:
                if self.table[i][j] == id:
                    count += 1
                else:
                    if maxOfId < count:
                        maxOfId = count
                        positionOfMaxId[0] = i - 1
                        positionOfMaxId[1] = j
                        nOfMaxId = 2
                    count = 0
                if i == self.size - 1:
                    if maxOfId < count:
                        maxOfId = count
                        positionOfMaxId[0] = i
                        positionOfMaxId[1] = j
                        nOfMaxId = 2
                i += 1

        ans = []
        ans.append(maxOfId)
        ans.append(positionOfMaxId)
        ans.append(nOfMaxId)
        return ans

    def draw(self, win):
        for i in range(len(self.allDrawing)):
            self.allDrawing[i].draw(win)



class Game:
    def __init__(self, size, win):
        my_table = Table(size, win)
        finalStr = ""

        while True:
            flagFirst = False
            flagSecond = False
            my_table.draw(win)
            while not flagFirst:
                pt = win.getMouse()
                x = pt.getX() // my_table.h
                y = pt.getY() // my_table.w
                print(str(x) + " " + str(y) + ' x')
                flagFirst = my_table.changeTable(int(x), int(y), 'x')
            print("First OK")
            tmp = my_table.checkTable('x')
            if tmp[0] == 5:
                finalStr = "First gamer win!"
                break

            my_table.draw(win)
            while not flagSecond:
                pt = win.getMouse()
                x = pt.getX() // my_table.h
                y = pt.getY() // my_table.w
                print(str(x) + " " + str(y) + ' o')
                flagSecond = my_table.changeTable(int(x), int(y), 'o')
            print("Second OK")
            tmp = my_table.checkTable('o')
            if tmp[0] == 5:
                finalStr = "Second gamer win!"
                break


        txt = Text(Point(250, 250), finalStr + "\nClick anywhere.")
        txt.setSize(30)
        txt.setTextColor(color_rgb(0, 0, 255))
        txt.draw(win)



def main() :
    win = GraphWin("My Game", 500, 500)
    win.setBackground(color_rgb(255, 0, 0))

    game = Game(10, win)

    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()
