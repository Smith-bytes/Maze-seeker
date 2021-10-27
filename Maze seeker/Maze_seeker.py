# map seeker by Lee on 20211026
maze_map = []
maze_map = [
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 0, 1, 0, 1, 0, 0, 0, 0, 1], 
           [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],    
           [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],    
           [1, 0, 1, 0, 0, 1, 0, 0, 0, 1],    
           [1, 0, 1, 0, 0, 1, 0, 1, 0, 1],    
           [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],    
           [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],    
           [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],    
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],]
treasuremap = []
routemap = []
start = 1,1 #to be changed
end = 1,5  #to be changed 

        

def step_seeker(step): #To plot the step number in the corresponding location on treasure map (ex 2 after 1)
    global treasuremap
    for x in range(len(treasuremap)):
        for y in range(len(treasuremap[x])):
            if treasuremap[x][y] == step:
                if x > 0 and treasuremap[x-1][y] == 0 and maze_map[x-1][y] == 0: #To check whether the location is empty, without any wall or previous walkthrough
                    treasuremap[x-1][y] = step+1

                if y > 0 and treasuremap[x][y-1] == 0 and maze_map[x][y-1] == 0:
                    treasuremap[x][y-1] = step+1

                if x < len(treasuremap) -1 and treasuremap[x+1][y] == 0 and maze_map[x+1][y] == 0:
                    treasuremap[x+1][y] = step+1

                if y < len(treasuremap[x])-1 and treasuremap[x][y+1] == 0 and maze_map[x][y+1] == 0:
                    treasuremap[x][y+1] = step+1

def print_map(map):
    for c in map:
        print(c)
    
def dir_path(step): #transfer treasure map to route map
    global routemap
    global t
    global a
    routemap[t][a]= 1
    while step > 1:
       
        if t > 0 and treasuremap[t-1][a] == step -1: #to find a step which is -1 smaller than the current step at surrounding, until we reach starting point
            t -=1
           
            routemap[t][a]= 1
            step -= 1
        elif a > 0 and treasuremap[t][a-1] == step -1:
            a -= 1
            routemap[t][a]= 1
            step -= 1
        elif t < len(treasuremap) -1 and treasuremap[t+1][a] == step - 1:
            t += 1
            routemap[t][a]= 1
            step -= 1
        elif a < len(treasuremap[t])-1 and treasuremap[t][a+1] == step -1:
            a += 1
            routemap[t][a]= 1
            step -= 1


for i in range(len(maze_map)): #create an empty "treasuremap" with 1 at the start point 
   routemap.append([])
   treasuremap.append([])
   for j in range(len(maze_map[i])):
       routemap[-1].append(0)
       treasuremap[-1].append(0)
i, j = start 
treasuremap[i][j] = 1 #initiate starting point
step = 0 
print ("treasuremap dimention complete")
while treasuremap[end[0]][end[1]] == 0: #loop wont stop until the end point is reached, each loop step +1 
    step += 1
    step_seeker(step)

print_map(maze_map)

print("pathing completed")
print("total number of step:", step+1)

print_map(treasuremap)

t, a = end 
dir_path(step+1)
print("route map completed")
print_map(routemap)