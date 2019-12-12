import math

def deg(point,data):
    degrees = []
    for p in data:
        if point != p:
            new = (point[0]-p[0],point[1]-p[1])
            degrees.append(math.atan2(new[1],new[0]))
    return len(set(degrees)), degrees
    
def nuker(data,point):
	final_angle = -1e-100
	for count in range(1,201):
		nukedx,nukedy = 0,0
		nuked_dist = 1e99
		angle = 10
		for x,y in data:
			new_angle = math.atan2(point[0]-x,point[1]-y)
			if new_angle < 0:
				new_angle += (2 *math.pi)
			if new_angle != 0:
				new_angle = 2 * math.pi - new_angle
			if new_angle > final_angle:
				distance = (x-point[0])**2 + (y-point[1])**2
				if new_angle < angle or (new_angle == angle and distance < nuked_dist):
					nukedx,nukedy = x,y
					nuked_dist,angle = distance,new_angle
		if angle == 10:
			final_angle = -1e-100
			count -=1
			continue
		data.remove((nukedx,nukedy))
		final_angle = angle
	return nukedx*100+nukedy

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
    number,degrees = deg(point,co)
    count[point] = number
pl = list(count.keys())[list(count.values()).index(max(count.values()))]
# Part One
print(pl,max(count.values()))

# Part Two
co.remove(pl)

print(nuker(set(co),pl))

