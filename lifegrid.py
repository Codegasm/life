import copy

class LifeGrid:

  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.reset()

  def count_neighbors(self, x, y):
    neighbors = 0

    for diffX in range(-1, 2):
      for diffY in range(-1, 2):
        nX = x + diffX
        nY = y + diffY
        
        if nX >= 0 and nY >= 0 and nX < self.width and nY < self.height:
          if self.matrix[nY][nX] == 1 and not (diffX == 0 and diffY == 0):
            neighbors += 1

    return neighbors

  def step(self):
    nextGen = copy.deepcopy(self.matrix)

    for y, row in enumerate(self.matrix):
      for x, cell in enumerate(row):
        neighbors = self.count_neighbors(x, y)

        if cell == 1 and (neighbors < 2 or neighbors > 3):
          nextGen[y][x] = 0
        elif cell == 0 and neighbors == 3:
          nextGen[y][x] = 1
    
    self.matrix = nextGen

  def reset(self):
    self.matrix = [[0 for col in range(self.height)] for row in range(self.width)]

