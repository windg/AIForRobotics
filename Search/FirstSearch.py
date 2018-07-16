# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space
from math import *
import copy
grid = [[0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0]]
heuristic = [[9, 8, 7, 6, 5, 4],
             [8, 7, 6, 5, 4, 3],
             [7, 6, 5, 4, 3, 2],
             [6, 5, 4, 3, 2, 1],
             [5, 4, 3, 2, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def Astar(grid,init,goal,cost,heuristic):
    copyGrid = copy.deepcopy(grid)
#    copyGrid = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
#    copyGrid[:] = grid[:]
    openList = [[0, 0] + init]
    expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    action = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    policy = [['' for row in range(len(grid[0]))] for col in range(len(grid))]
    count = 0
    found = 0
    expand[init[0]][init[1]]= count
    copyGrid[init[0]][init[1]] = 2
    while len(openList):
        curr = min(openList)
        openList.remove(curr)
        count += 1
        expand[curr[2]][curr[3]] = count
        for i in range(len(delta)):
            nextstep = [(x+y) for x, y in zip(curr,[0 , cost] + delta[i])]
           
#            nextstep[0] =  nextstep[1] + heuristic[nextstep[2]][nextstep[3]]
            
            
            if nextstep[2:] == goal:
                nextstep[0] =  nextstep[1] + heuristic[nextstep[2]][nextstep[3]]
                copyGrid[nextstep[2]][nextstep[3]] = 2
                count += 1
                expand[nextstep[2]][nextstep[3]] = count
                action[nextstep[2]][nextstep[3]] = i
                found = True
                print('found')
                break
            if 0<=nextstep[2]<len(grid)\
                and 0<=nextstep[3]<len(grid[0])\
                and not copyGrid[nextstep[2]][nextstep[3]]:
                    nextstep[0] =  nextstep[1] + heuristic[nextstep[2]][nextstep[3]]
                    print(nextstep)
                    copyGrid[nextstep[2]][nextstep[3]] = 2
                    openList.append(nextstep)
                    
                    action[nextstep[2]][nextstep[3]] = i
        if found:
            break
    if found:
        pivot = copy.deepcopy(goal)
        policy[pivot[0]][pivot[1]] = '*'
        while pivot != init:
            pivot = [(x-y) for x, y in zip(pivot, delta[action[pivot[0]][pivot[1]]])]
            policy[pivot[0]][pivot[1]] =  delta_name[action[pivot[0]][pivot[1]]]
    
        return expand
    else:
        return 'failed'

result = search(grid,init,goal,cost,heuristic)