from itertools import combinations
from copy import deepcopy
from math import gcd
position = []
velocity = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
def clean(string):
    if string[0] == '<':
        return int(string [3:])
    elif string[-1] == '>':
        return int(string [2:-1])
    else:
        return int(string[2:])

def calculate_gravity(planetA_co,planetB_co,velocity_a,velocity_b):
    for x in range(len(planetA_co)):
        if planetA_co[x] > planetB_co[x]:
            velocity_a[x] -= 1
            velocity_b[x] += 1
        elif planetB_co[x] > planetA_co[x]:
            velocity_a[x] += 1
            velocity_b[x] -= 1
        else:
            velocity_a[x] += 0
            velocity_b[x] += 0
    return velocity_b,velocity_a

def apply_velocity(planet,vel):
    for x in range(len(planet)):
        planet[x] += vel[x] 
    return planet

def find_energy(planet,velocity):
    return sum([abs(x) for x in planet]) * sum([abs(x) for x in velocity])

def lcm(x, y):
    return x // gcd(x, y) * y

def tick():
    for x in list(combinations(position,2)):
        pos_a = position.index(x[0])
        pos_b = position.index(x[1])
        velocity[pos_b],velocity[pos_a] = calculate_gravity(x[0],x[1],velocity[pos_a],velocity[pos_b])
    for x in range(len(position)):
        position[x] = apply_velocity(position[x],velocity[x])
with open('input.txt','r') as file:
    for line in file:
        position.append([clean(x) for x in line.strip().split(', ')])
old_position = deepcopy(position)
old_velocity = deepcopy(velocity)

# Part One
for _ in range(1000):
    tick()
print(sum([find_energy(position[x],velocity[x]) for x in range(4)]))

# Part Two
position = old_position
velocity = old_velocity
intial_state = [[[old_position[i][j] for i in range(4)], [0, 0, 0, 0]] for j in range(3)]
min_cycle = [0,0,0]
found = [True,True,True]
t = 0
while all(found):
    tick()
    t+=1
    for i in range(3):
        if found[i]:
            min_cycle[i] += 1
            state = [[old_position[j][i] for j in range(4)], [old_velocity[k][i] for k in range(4)]]
            if state == intial_state[i]:
                    found[i] = False

print("Part One",lcm(lcm(min_cycle[0],min_cycle[1]),min_cycle[2]))