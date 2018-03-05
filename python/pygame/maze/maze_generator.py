import random
import time
mx = 12; my = 12 # width and height of the maze
maze = [[0 for x in range(mx)] for y in range(my)]
dx = [0, 1, 0, -1]; dy = [-1, 0, 1, 0] # 4 directions to move in the maze
color = [(0,0, 0), (255, 255, 255)] # RGB colors of the maze
# start the maze from a random cell
cx = random.randint(0, mx - 1)
cy = random.randint(0, my - 1)
maze[cy][cx] = 'S'
stack = [(cx, cy, 0)] # stack element: (x, y, direction)

target_random_tile = random.randint(0, int((mx * my)/2))
print(target_random_tile)
visited = 1

while len(stack) > 0:   
    symbol = 1
    if visited == target_random_tile:
        print(visited)
        symbol = "E"
    (cx, cy, cd) = stack[-1]
    # to prevent zigzags:
    # if changed direction in the last move then cannot change again
    if len(stack) > 2:
        if cd != stack[-2][2]: dirRange = [cd]
        else: dirRange = range(4)
    else: dirRange = range(4)

    # find a new cell to add
    nlst = [] # list of available neighbors
    for i in range(4):
        nx = cx + dx[i]; ny = cy + dy[i]
        if nx >= 0 and nx < mx and ny >= 0 and ny < my:
            if maze[ny][nx] == 0:
                # of occupied neighbors must be 1
                ctr = 0
                for j in range(4):
                    ex = nx + dx[j]; ey = ny + dy[j]
                    if ex >= 0 and ex < mx and ey >= 0 and ey < my:
                        if maze[ey][ex] in [1, 'S', 'E']: ctr += 1
                if ctr == 1: nlst.append(i)
    # if 1 or more neighbors available then randomly select one and move
    if len(nlst) > 0:
        ir = nlst[random.randint(0, len(nlst) - 1)]
        cx += dx[ir]; cy += dy[ir]; maze[cy][cx] = symbol
        stack.append((cx, cy, ir))
    else: 
        stack.pop()
    visited += 1

print(maze)

