
import matplotlib.pyplot as plt 
import numpy 
try: 
    f = open("maze.txt", "r") # opens .txt in read 
    counter = sum(1 for lines in f) # creates a count of total number of element:2601 
    sqrootc = int(numpy.sqrt(counter)) # sqrt counter to get dimension of maze 
    f.close() # close file 
except:
    print("file does not exist")
    exit(0)
 
f = open("maze.txt", "r") # opens .txt in read 
lines = f.readlines() # returns a list containing each line in the file as string 
linesres = [ele == "True\n" for ele in lines] # convert str list to boolean list   

for q in range(len(linesres)):
    linesres[q]=int(linesres[q])

f.close() # close file 
 
arr = numpy.array(linesres) # converts the boolean list into a array 
m = arr.reshape((sqrootc,sqrootc)) # give array 51Row by 51Column  

maze_map = []
maze_map = m
treasuremap = []
routemap = []
start = 1,1 #to be changed
end = 1,47  #to be changed 

def step_seeker(step): #To plot the step number in the corresponding location on treasure map (ex 2 after 1)
    global treasuremap
    for x in range(len(treasuremap)):
        for y in range(len(treasuremap[x])):
            if treasuremap[x][y] == step:
                if x > 0 and treasuremap[x-1][y] == 0 and maze_map[x-1, y] == 0 : #To check whether the location is empty, without any wall or previous walkthrough
                    treasuremap[x-1][y] = step+1

                if y > 0 and treasuremap[x][y-1] == 0 and maze_map[x, y-1] == 0 :
                    treasuremap[x][y-1] = step+1

                if x < len(treasuremap) -1 and treasuremap[x+1][y] == 0 and maze_map[x+1, y] == 0:
                    treasuremap[x+1][y] = step+1

                if y < len(treasuremap[x])-1 and treasuremap[x][y+1] == 0 and maze_map[x, y+1] == 0:
                    treasuremap[x][y+1] = step+1

def print_map(map):
    for c in map:
        print(c)
    
def dir_path(step): #transfer treasure map to route map
    global routemap
    global t
    global a
    routemap[t][a]= 2
    while step > 1:
       
        if t > 0 and treasuremap[t-1][a] == step -1: #to find a step which is -1 smaller than the current step at surrounding, until we reach starting point
            t -=1
           
            routemap[t][a]= 2
            step -= 1
        elif a > 0 and treasuremap[t][a-1] == step -1:
            a -= 1
            routemap[t][a]= 2
            step -= 1
        elif t < len(treasuremap) -1 and treasuremap[t+1][a] == step - 1:
            t += 1
            routemap[t][a]= 2
            step -= 1
        elif a < len(treasuremap[t])-1 and treasuremap[t][a+1] == step -1:
            a += 1
            routemap[t][a]= 2
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

print("pathing completed")
print("total number of step:", step+1)

t, a = end 
dir_path(step+1)
print("route map completed")

G = numpy.array(routemap)
m = m + G
plt.imshow(m.T, cmap=plt.cm.viridis_r) #plot the transpose of m
plt.show()
