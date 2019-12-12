import math

def deg(point,data):
    degrees = []
    for p in data:
        if point != p:
            new = (point[0]-p[0],point[1]-p[1])
            degrees.append(math.atan2(new[1],new[0]))
    return len(set(degrees))
    
co = []
file = open('input.txt')
x,y = 0,0
for line in file:
    for point in line:
        if point == '#':
            co.append((x,y))
        x+=1
    y+=1
    x=0

count = {}
for point in co:
    count[point] = deg(point,co)

print(list(count.keys())[list(count.values()).index(max(count.values()))],max(count.values())) 


