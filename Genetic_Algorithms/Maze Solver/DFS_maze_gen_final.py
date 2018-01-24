# cpt
# Maze Building Algorithm
# author: Aniekan Umoren
# date: 2015-12-31

import random

# Structure of "database" [[dir_row,dir_col,wall_index]...]    
db = [[-1,0,0], [0,1,1], [1,0,2], [0,-1,3]]
# Structure of "database" [[dir_x,dir_y,wall_index]...]
#inverted: start down and rotate anti-clockwise
db = [[0,-1,0], [1,0,1], [0,1,2], [-1,0,3]]
# @param - curr (the cell)
# @param - maxi (the maximum num that can appear in neighbours list)
# Returns a list of coordinates of valid neighbours
def get_neighbours(curr, maxi):
    result = []
    # Looping through "db" to find possible neighbours
    for i in range(4):
        temp = []
        # A new neighbour is formed by perfroming operation on the 'curr' cell's pos
        temp.extend([curr[0] + db[i][0], curr[1] + db[i][1], db[i][2]])
        result.append(temp)
    i = 0
    # Getting rid of invalid neighbours
    # If it's -1 or maxi[0]/maxi[1] then the neighbour is off-grid
    while i < len(result):
        temp = result[i]
        if (-1 in temp) or (maxi[0] is temp[0]) or (maxi[1] is temp[1]):
            result.remove(temp)
        else:
            i += 1
    return result

def maze_gen(curr, maze, sf = [False,False]):
    # Mark current cell as visited and turn wall into a path
    maze[curr[0]][curr[1]][1] = 1
    if sf[0] is True:
        # Removing the 4th (left) wall if it is starting point
        maze[curr[0]][curr[1]][0][3] = 0
    elif sf[1] is True:
        # Removing the 2nd (right) wall if it is finsih point
        maze[curr[0]][curr[1]][0][1] = 0
    maxi = [len(maze),len(maze[0])]
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
    '''UPDATE NEIGHBOURS OR ELSE YOU HAVE EMPTY SPACES'''
    random.shuffle(neighbours)       
    for nxt in neighbours:
        # nxt structure [row,col,wall]
        # Config. walls for 'curr' cell and 'nxt' cell
        if maze[nxt[0]][nxt[1]][1] == 1 : continue # update
        maze[curr[0]][curr[1]][0][nxt[2]] = 0
        try:
            maze[nxt[0]][nxt[1]][0][nxt[2]+2] = 0
        except:
            maze[nxt[0]][nxt[1]][0][nxt[2]-2] = 0
        if nxt[:2] == [len(maze)-1, len(maze[0])-1]:
            sf = [False,False]
        else: sf = [False, False]            
        maze = maze_gen(nxt[:2], maze, sf)
    return maze

def Generate(width, height):
    #rows = int(input("Enter # rows: "))
    #columns = int(input("Enter # columns: "))
    maze = []

    # Structure of cells [[wall_data],visit]
    for x in range(width):
        TempRow = []
        for y in range(height):
            # Structure of w
            TempRow.append([[1,1,1,1],0])
        maze.append(TempRow)
        
    maze = maze_gen([0,0],maze,sf = [False,False])

    #Printing the Maze
    '''for r in range(rows):
        for c in range(columns):
            print(maze[r][c], end='')
        print(end = '\n')'''
    return maze

if __name__ == "__main__":
    width = 10
    height = 10
    maze = Generate(width, height)
    for y in range(height):
        for x in range(width):
            print(maze[x][y], end='')
        print(end = '\n')

