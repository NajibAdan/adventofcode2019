
def shortest(points):
    return min(abs(p[0])+abs(p[1]) for p in points)

def time_sensitive(intersetction,path1,path2):
    return min(path1[p]+path2[p] for p in intersetction)
def walk_the_wire(paths):
    current_pos = [0,0]
    points = {}
    step = 0
    for path in paths.split(','):
        dir = path[0]
        length = int(path[1:])
        for _ in range(length):
            if dir == 'U':
                current_pos = current_pos[0]+1, current_pos[1]
            elif dir == 'D':
                current_pos = current_pos[0]-1, current_pos[1]
            elif dir == 'R':
                current_pos = current_pos[0], current_pos[1]+1
            elif dir == 'L':
                current_pos = current_pos[0], current_pos[1]-1
            step+= 1
            if current_pos not in points:
                points[current_pos] = step
    return points

def read():
    path1 , path2 = open('input.txt','r').read().split('\n')
    wire1 = walk_the_wire(path1) 
    wire2 = walk_the_wire(path2)
    intersections = wire1.keys() & wire2.keys()
    print("Manhattan Distance from the Central Point "+ str(shortest(intersections)))
    print("Fewest combined steps: "+str(time_sensitive(intersections,wire1,wire2)))


read()
