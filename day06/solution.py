def getDepth(object,orbit):
    if object == 'COM':
        return 0
    else:
        new = orbit[object]
        return 1 + getDepth(new,orbit)

def partOne(orbit):
    sum = 0
    for x in orbit:
        sum += getDepth(x,orbit)
    return sum

def partTwo(orbit):
    current_you = "YOU"
    current_san = "SAN"
    you_chain = []
    san_chain = []
    while(current_you != 'COM'):
        you_chain.append(orbit[current_you])
        current_you = orbit[current_you]
    while(current_san != 'COM'):
        san_chain.append(orbit[current_san])
        current_san = orbit[current_san]
    return len(set(you_chain) ^ set(san_chain))
mappings = open('input.txt','r')
orbit = {}
for map in mappings:
    left,right = map.strip().split(')')
    orbit[right] = left


print(partOne(orbit))
print(partTwo(orbit))