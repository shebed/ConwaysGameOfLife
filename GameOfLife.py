"""
conway.py 
A simple Python/matplotlib implementation of Conway's Game of Life.
"""

import sys, argparse
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation


ON = 255
OFF = 0
vals = [ON, OFF]

totalBlocks = 0
totalBeehives = 0
totalLoaves = 0
totalBoats = 0
totalTubs = 0
totalBlinkers = 0
totalToads = 0
totalBeacons = 0
totalGliders = 0
totalLwsps = 0
totalShapes = 0


#Still lifes
block = np.array([[255, 255], 
                  [255, 255]])          


beehive = np.array([[0,     255, 255, 0], 
                   [255,     0,  0, 255], 
                   [0,      255, 255, 0]])                  
            
loaf = np.array([[0,    255, 255, 0], 
                 [255,   0,  0, 255], 
                 [0,  255,   0, 255],
                 [0,  0,   255, 0  ]])  

boat = np.array([[255,   255, 0], 
                 [255,   0, 255],
                 [0,  255,   0 ]])                 

tub = np.array([[0,    255, 0], 
                 [255,  0, 255], 
                 [0,  255, 0]])  

#Oscilators                  

blinker1 = np.array([[0, 255, 0], 
                    [0,  255, 0], 
                    [0,  255, 0]])          

blinker2 = np.array([[255, 255, 255]])   

toad1 = np.array([[0,   0, 255, 0], 
                 [255, 0,  0, 255], 
                 [255, 0,  0, 255],
                 [0,  255, 0, 0  ]])

toad2 = np.array([[0, 255, 255, 255],
                  [255, 255, 255, 0]])   

beacon1 = np.array([[255, 255, 0, 0], 
                    [255, 255, 0, 0],
                    [0, 0, 255, 255], 
                    [0, 0, 255, 255]])                                          


beacon2 = np.array([[255, 255, 0, 0], 
                    [255, 0, 0, 0],
                    [0, 0, 0, 255], 
                    [0, 0, 255, 255]]) 


#Spaceships
glider1 = np.array([[0,    255,  0], 
                   [0,  0,     255], 
                   [255,  255, 255]])

glider2 = np.array([[255,   0,  255], 
                    [0,   255,  255], 
                    [0,  255, 0]])                   

glider3 = np.array([[0,    0, 255], 
                   [255,  0, 255], 
                   [0,  255, 255]])

glider4 = np.array([[255,    0, 0], 
                    [0,  255, 255], 
                    [255,  255, 0]])

lwsp1 = np.array([[255,  0,  0, 255, 0], 
                  [0,  0,  0, 0,   255], 
                  [255, 0, 0, 0,   255],
                  [0, 255,  255, 255, 255]])

lwsp2 = np.array([[0,  0,  255, 255, 0], 
                  [255,  255,  0, 255,   255], 
                  [255, 255, 255, 255,   0],
                  [0, 255,  255, 0, 0]])                 

lwsp3 = np.array([[0,  255, 255, 255, 255], 
                  [255,  0,  0, 0,  255], 
                  [0, 0, 0, 0,   255],
                  [255, 0,  0, 255, 0]])                 

lwsp4 = np.array([[0,  0,  255, 255, 0], 
                  [0,  255,  255, 255,  255], 
                  [255, 255, 0, 255,   255],
                  [0, 0,  255, 255, 0]])

blinkers = [blinker1, blinker2]
toads = [toad1, toad2]
beacons = [beacon1, beacon2]
gliders = [glider1, glider2, glider3, glider4]
lwsps = [lwsp1, lwsp2, lwsp3, lwsp4]

patterns = {'block': block,
            'beehive': beehive,
            'loaf' : loaf,
            'boat' : boat,
            'tub' : tub,
            'blinker' : blinkers,
            'toad' : toads,
            'beacon' : beacons,
            'glider' :gliders,
            'lwsp': lwsps}                  
'''
Block
Beehive
Loaf
Boat
Tub

Blinker
Toad
Beacon

Glider
Light-weight spaceship
'''


def randomGrid(N, M):
    """returns a grid of NxN random values"""
    return np.random.choice(vals, N*M, p=[0.2, 0.8]).reshape(N, M)



'''
def addGlider(i, j, grid):
    """adds a glider with top left cell at (i, j)"""
    glider = np.array([[0,    0, 255], 
                       [255,  0, 255], 
                       [0,  255, 255]])
    grid[i:i+3, j:j+3] = glider
'''
def findPatterns(N, M, grid):

    global totalBlocks
    global totalBeehives
    global totalLoaves 
    global totalBoats 
    global totalTubs
    global totalBlinkers 
    global totalToads
    global totalGliders 
    global totalLwsps
    global totalShapes 

    totalBlocks = 0
    totalBeehives = 0
    totalLoaves = 0
    totalBoats = 0
    totalTubs = 0
    totalBlinkers = 0
    totalToads = 0
    totalBeacons = 0
    totalGliders = 0
    totalLwsps = 0
    totalShapes = 0

    for i in range(N):
        for j in range(M):
            
            if grid[i,j]:                
                for p,k in patterns.items():
                    if str(p) == "block":
                        if np.array_equal(grid[i:i+2, j:j+2], k):
                            totalBlocks += 1
                            totalShapes += 1
                            
                    elif str(p) == "beehive":
                            if np.array_equal(grid[i:i+4, j:j+3], k):
                                totalBeehives += 1
                                totalShapes += 1
                    
                    elif str(p) == "loaf":
                            if np.array_equal(grid[i:i+4, j:j+4], k):
                                totalLoaves += 1
                                totalShapes += 1                    
                    
                    elif str(p) == "boat":
                            if np.array_equal(grid[i:i+3, j:j+3], k):
                                totalBoats += 1
                                totalShapes += 1
                    
                    elif str(p) == "tub":
                            if np.array_equal(grid[i:i+3, j:j+3], k):
                                totalTubs += 1
                                totalShapes += 1

                    elif str(p) == "blinker":
                        if np.array_equal(grid[i:i+3, j], k):
                            totalBlinkers += 1
                            totalShapes += 1
                    elif str(p) == "blinker":
                        if np.array_equal(grid[i:i, j+3], k):
                            totalBlinkers += 1
                            totalShapes += 1
                            
                    elif str(p) == "toad":
                            if np.array_equal(grid[i:i+4, j:j+4], k):
                                totalToads += 1
                                totalShapes += 1
                    elif str(p) == "toad":
                            if np.array_equal(grid[i:i+4, j:j+2], k):
                                totalToads += 1
                                totalShapes += 1        
                    
                    elif str(p) == "beacon":
                            if np.array_equal(grid[i:i+4, j:j+4], k):
                                totalBeacons += 1
                                totalShapes += 1                    
                    
                    elif str(p) == "glider":
                            if np.array_equal(grid[i:i+3, j:j+3], k):
                                totalGliders += 1
                                totalShapes += 1
                    
                    elif str(p) == "lwsp":
                            if np.array_equal(grid[i:i+5, j:j+4], k):
                                totalLwsps += 1
                                totalShapes += 1
    





def update(frameNum, img, grid, N, M):
    # copy grid since we require 8 neighbors for calculation
    # and we go line by line 
    newGrid = grid.copy()
    # TODO: Implement the rules of Conway's Game of Life
    for i in range(N):
        for j in range(M):
 
            # compute 8-neighbor sum
            # using toroidal boundary conditions - x and y wrap around
            # so that the simulation takes place on a toroidal surface.
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                         grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                         grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                         grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])/255)
 
            # apply Conway's rules
            if grid[i, j]  == ON:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = OFF
            else:
                if total == 3:
                    newGrid[i, j] = ON

    # update data    
    findPatterns(N, M, grid)
    printData()
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

def printData():
    global totalBlocks
    global totalBeehives
    global totalLoaves 
    global totalBoats 
    global totalTubs
    global totalBlinkers 
    global totalToads
    global totalGliders 
    global totalLwsps
    global totalShapes 

    with open("outputs.txt", 'a') as f:
        f.write("--------------------------------\n")
        f.write("|            | Count | Percent |\n")
        f.write("|------------+-------+---------|\n")
        
        f.write("|Block       |  " + str(totalBlocks) +"   |   "+ str(totalBlocks / totalShapes * 100) +"    |\n")
        f.write("|Beehive     |  "+ str(totalBeehives)+"   |   "+ str(totalBeehives / totalShapes * 100) +"    |\n") 
        f.write("|Loaf        |  "+ str(totalLoaves)+"   |   "+ str(totalLoaves / totalShapes * 100) +"    |\n")
        f.write("|Boat        |  "+ str(totalBoats)+"   |   "+ str(totalBoats / totalShapes * 100) +"    |\n")
        f.write("|Tub         |  "+ str(totalTubs)+"   |   "+ str(totalTubs / totalShapes * 100) +"    |\n")
        f.write("|Blinker     |  "+ str(totalBlinkers)+"   |   "+ str(totalBlinkers /  totalShapes * 100) +"    |\n")
        f.write("|Toad        |  "+ str(totalToads)+"   |   "+ str(totalToads / totalShapes * 100) +"    |\n")
        f.write("|Beacon      |  "+ str(totalBeacons)+"   |   "+ str(totalBeacons / totalShapes * 100) +"    |\n")
        f.write("|Glider      |  "+ str(totalGliders)+"   |   "+ str(totalGliders / totalShapes * 100) +"    |\n")
        f.write("|LG sp ship  |  "+ str(totalLwsps)+"   |   "+ str(totalLwsps / totalShapes * 100) +"    |\n")
        
        f.write("|------------+--------+----------|\n")
        f.write("|Total       |   "+ str(totalShapes) + " |                     \n")
        f.write("\n\n\n")
        f.close()  





def readFile(file, data):
    with open(file, 'r') as f:
        txt = f.readline()
        sp = txt.split()
        N = int(sp[0])
        M = int(sp[1])    
        
        txt = f.readline()
        sp = txt.split()
        G= int(sp[0])
        

        while True:
            txt = f.readline()
            if not txt:
                break
            sp = txt.split()
            data.append([int(sp[0]),int(sp[1])])          

    f.close()  
    
    return N, M, G

def initGrid(grid, data):
    for d in data:
        #print("Live cell at X:" + str(d[0]) + " Y:" + str(d[1]) )
        grid[d[0], d[1]] = ON
        



# main() function
def main():
    # Command line args are in sys.argv[1], sys.argv[2] ..
    # sys.argv[0] is the script name itself and can be ignored
    # parse arguments
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life system.py.")
    # TODO: add arguments

    data = []
    N, M, G= readFile("inputSample05.txt", data)

    # declare grid
    grid = np.zeros(N * M).reshape(N, M)
    initGrid(grid, data)
    # set grid size
    #N = 100
    #M = 200

    # set animation update interval
    updateInterval = 500


    # populate grid with random on/off - more off than on
    #grid = randomGrid(N, M)
    # Uncomment lines to see the "glider" demo
    #grid = np.zeros(N*N).reshape(N, N)
    #addGlider(1, 1, grid)

    # set up animation
    fig, ax = plt.subplots()
    #plt.text(0, 0, "Poop", fontdict=None, fontsize = 22, bbox = dict(facecolor = 'red', alpha = 0.5))
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, M),
                                  frames = G,
                                  interval=updateInterval,
                                  repeat_delay= 5000)

    plt.show()

# call main
if __name__ == '__main__':
    main()