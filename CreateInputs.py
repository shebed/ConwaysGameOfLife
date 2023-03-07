import sys, argparse
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation


ON = 255
OFF = 0
vals = [ON, OFF]

def printInputFile(grid, N, M, G):
    with open("inputSample.txt", 'a') as f:
        f.write(str(N) + " " + str(M) + " #Width Height \n")
        f.write(str(G) + " # Generations \n")
        for i in range(N):
          for j in range(M):
            if grid[i, j]:
              f.write(str(i) + " " +str(j) + "  Live Cell \n")

        f.close()  


def randomGrid(N, M):
    """returns a grid of NxN random values"""
    return np.random.choice(vals, N*M, p=[0.2, 0.8]).reshape(N, M)


def main():
    N = 50
    M = 100
    G = 200
    grid = np.array([])
    grid = randomGrid(N, M)
    printInputFile(grid, N, M, G)


if __name__ == '__main__':
    main()