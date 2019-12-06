import math
def getConsumption(mass):
    return math.floor(int(mass)/3)-2

def recursiveConsumption(mass):
    if math.floor(mass/3) >= 0:
        return mass + recursiveConsumption(getConsumption(mass))
    else:
        return 0
modules = open("./day01/input.txt",'r')
sum = 0
for module in modules:
    sum = sum + recursiveConsumption(getConsumption(module))

print(sum)