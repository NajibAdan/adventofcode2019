import math
def getConsumption(mass):
    return math.floor(int(mass)/3)-2
modules = open("./day01/input.txt",'r')
sum = 0
for module in modules:
    sum = sum + getConsumption(module)

print(sum)