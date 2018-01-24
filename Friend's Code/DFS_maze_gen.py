# cpt
# Maze Building Algorithm
# author: Aniekan Umoren
# date: 2015-12-31

import random

"USE THE STACK AND YOU'RE DONE!!!!!"
class Stack(list):
    def push(self, item):
        self.append(item)
    def isEmpty(self):
        return not self
# Structure of "database" [[dir_row,dir_col,wall_index]...]    
db = [[-1,0,0], [0,1,1], [1,0,2], [0,-1,3]]
# @param - curr (the cell)
# @param - maxi (the maximum num that can appear in neighbours list)
# Returns a list of coordinates of valid neighbours
def get_neighbours(curr, maxi):
    result = []
    for i in range(4):
        temp = []
        temp.extend([curr[0] + db[i][0], curr[1] + db[i][1], db[i][2]])
        result.append(temp)
    i = 0
    while i < len(result):
        temp = result[i]
        if -1 in temp or maxi in temp:
            result.remove(temp)
        else:
            i += 1
    return result

def maze_gen(curr, maze, sf = [False,False]):
    # Mark current cell as visited and turn wall into a path
    maze[curr[0]][curr[1]][1] = 1
    if sf[0] is True:
        # Removing the 4th (left) wall
        maze[curr[0]][curr[1]][0][3] = 0
    elif sf[1] is True:
        # Removing the 2nd (right) wall
        maze[curr[0]][curr[1]][0][1] = 0
    maxi = len(maze)
    neighbours = get_neighbours(curr, maxi)
    
    # Removing cells that have already been visited
    i = 0
    while i < len(neighbours):
        cell = neighbours[i]
        # Executes if this cell has been visited
        if maze[cell[0]][cell[1]][1] == 1:
                neighbours.remove(cell)
        else:
            i += 1
    random.shuffle(neighbours)       
    if len(neighbours) is 0:
        return maze
    else:
        for nxt in neighbours:
            # nxt structure [row,col,wall]
            # Config. walls for 'curr' cell and 'nxt' cell
            maze[curr[0]][curr[1]][0][nxt[2]] = 0
            try:
                maze[nxt[0]][nxt[1]][0][nxt[2]+2] = 0
            except:
                maze[nxt[0]][nxt[1]][0][nxt[2]-2] = 0
            return maze_gen(nxt[:2], maze)
        return maze

def Generate(rows, columns):
    #rows = int(input("Enter # rows: "))
    #columns = int(input("Enter # columns: "))
    maze = []

    # Structure of cells [[wall_data],visit]
    for r in range(rows):
        temp_row = []
        for c in range(columns):
            # Structure of w
            temp_row.append([[1,1,1,1],0])
        maze.append(temp_row)
        
    maze = maze_gen([0,0],maze,sf = [True,False])
    
    #Printing the Maze
    '''for r in range(rows):
        for c in range(columns):
            print(maze[r][c], end='')
        print(end = '\n')'''
    return maze

Generate()
