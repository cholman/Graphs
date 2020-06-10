#Connected Components
#-----------------

#parts of the graph taht are connected, but disjoint from other parts of the graph.

# for each node:
#     if not not visited:
#         traverse from that node
#         increment counter
# Graph:
#              t  t  t  t  t  t  t  t  t  t  t  t
#     nodes = [1, 2, 3, 4, 5, 6, 7, a, b, c, d, e]
#                                                  i

#     edges = [(a, b), (b, c) ... ]

# counter = 3

# Linked List:
#     nodes = [1,    2,      3,       4     , 5]
#     edges = [(1, 2), (2, 3), (3, 4), (4, 5)]


islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

#for each node:
#   if node not visited and the node is "land":
#       traverse from that node
#       increment counter

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

def get_neighbors(row, col, matrix):
    neighbors = []
    #check north
    if row > 0 and matrix[row-1][col] == 1:
        neighbors.append((row-1, col))
    #check south
    if row < len(matrix) and matrix[row+1][col] == 1:
        neighbors.append((row+1, col))
    #check west
    if col > 0 and matrix([row][col-1]) == 1:
        neighbors.append((row, col-1))
    #check east
    if col < len(matrix[0]) and matrix([row][col+1]) == 1:
        neighbors.append((row, col+1))

def dft(row, col, matrix, visisted):
    s = Stack()

    s.push((row, col))

    while s.size() > 0:
        row, col = s.pop()

        if not visisted[row][col]:
            visisted[row][col] = True

            for neighbor in get_neighbors(row, col, matrix):
                s.push(neighbor)

def island_counter(matrix): #matrix is a 2d array
    island_count = 0
    # create a visited matrix
    visisted = []

    for _ in range(len(matrix)):
        visisted.append([False] * len(matrix[0]))

    # walk through each cell in the matrix
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            # if it's not visited
            if not visisted[row][col]:
                # if it's a "1"
                if matrix[row][col] == 1:
                    # do DFT and mark them as visited
                    dft(row, col, matrix, visisted)
                    # increment counter by 1\
                    island_count += 1
            
        return island_count
island_counter(islands)