import cell
import numpy as np
import sys
import os
import argparse

FILE_ALIVE = 'X'
FILE_DEAD = '-'

# error messages 
INVALID_FILETYPE_MSG = "Error: Invalid file format. %s must be a .txt file."
INVALID_PATH_MSG = "Error: Invalid file path/name. Path %s does not exist."
  
def validate_file(file_name): 
    ''' 
    validate file name and path. 
    '''
    if not valid_path(file_name): 
        print(INVALID_PATH_MSG%(file_name)) 
        quit() 
    elif not valid_filetype(file_name): 
        print(INVALID_FILETYPE_MSG%(file_name)) 
        quit() 
    return
      
def valid_filetype(file_name): 
    # validate file type 
    return file_name.endswith('.txt') 
  
def valid_path(path): 
    # validate file path 
    return os.path.exists(path)

def createEmptyBoard(dimension):
    return  [[False]*dimension for i in range(0, dimension)]

def createBoardFromFile(args):
     # get the file name/path 
    file = args.file[0] 
  
    # validate the file name/path 
    validate_file(file) 

    # read the file
    input = np.loadtxt(file, dtype='i', delimiter=',')
    for i in range(0, len(input)):
        for j in range(0, len(input[i])):
            if (input[i][j] == FILE_ALIVE):
                input[i][j] = True
            else:
                input[i][j] = False

    return input

def createBlinkerBoard(args):
    size = args.blinker[0]
    if (size < 5):
        size = 5

    grid = createEmptyBoard(size)
    grid[1][2] = True
    grid[2][2] = True
    grid[3][2] = True
    return grid

def createToadBoard(args):
    size = args.toad[0]
    if (size < 6):
        size = 6

    grid = createEmptyBoard(size)
    grid[2][2] = True
    grid[2][3] = True
    grid[2][4] = True
    grid[3][1] = True
    grid[3][2] = True
    grid[3][3] = True
    return grid

def createBeaconBoard(args):
    size = args.beacon[0]
    if (size < 6):
        size = 6

    grid = createEmptyBoard(size)    
    grid[1][1] = True
    grid[1][2] = True
    grid[2][1] = True
    grid[2][2] = True

    grid[3][3] = True
    grid[3][4] = True
    grid[4][3] = True
    grid[4][4] = True
    return grid

def createGliderBoard(args):
    size = args.glider[0]
    if (size < 6):
        size = 6

    grid = createEmptyBoard(size)    
    grid[0][2] = True
    grid[1][2] = True
    grid[1][0] = True
    grid[2][2] = True
    grid[2][1] = True
    return grid

def printBoardOnConsole(grid):
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if (grid[i][j]):
                    print(FILE_ALIVE, end=" ")
                else:
                    print(FILE_DEAD, end=" ")
            print()

def main(): 
    # create parser object 
    parser = argparse.ArgumentParser(description = "A python implementation of Conway's Game of Life!") 
  
    # defining arguments for parser object 
    parser.add_argument("-b", "--blinker", type = int, nargs = 1, 
                        metavar = 'boardsize',
                        help = "Creates a blinker board.") 
      
    parser.add_argument("-t", "--toad", type = int, nargs = 1, 
                        metavar = 'boardsize',
                        help = "Creates a toad board.") 
      
    parser.add_argument("-e", "--beacon", type = int, nargs = 1,
                        metavar = 'boardsize', 
                        help = "Creates a beacon board.") 
      
    parser.add_argument("-g", "--glider", type = int, nargs = 1,
                        metavar = 'boardsize',
                        help = "Creates a glider board.") 
      
    parser.add_argument("-f", "--file", type = str, nargs = 1, 
                        metavar = "path", 
                        help = "Reads a board from a file.") 
  
    # parse the arguments from standard input 
    args = parser.parse_args() 
      
    # calling functions depending on type of argument 
    if args.blinker != None: 
        grid = createBlinkerBoard(args) 
    elif args.toad != None: 
        grid = createToadBoard(args) 
    elif args.beacon !=None: 
        grid = createBeaconBoard(args) 
    elif args.glider != None: 
        grid = createGliderBoard(args) 
    elif args.file != None: 
        grid = createBoardFromFile(args) 
    else:
        print('Invalid Input!\n"python board.py -h" for further information.')
        return
    
    while(True):
        # print(np.matrix(grid))
        printBoardOnConsole(grid)
        grid = cell.getNextGrid(grid)
        i = input("Press Enter to continue, 'e' to exit...")
        if (i == 'e'):
            return
            
if __name__ == "__main__":
    main()