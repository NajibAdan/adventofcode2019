code ="""1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,9,1,19,1,19,5,23,1,23,6,27,2,9,27,31,1,5,31,35,1,35,
        10,39,1,39,10,43,2,43,9,47,1,6,47,51,2,51,6,55,1,5,55,59,2,59,10,63,1,9,63,67,1,9,67,71,
        2,71,6,75,1,5,75,79,1,5,79,83,1,9,83,87,2,87,10,91,2,10,91,95,1,95,9,99,2,99,9,103,2,10,
        103,107,2,9,107,111,1,111,5,115,1,115,2,119,1,119,6,0,99,2,0,14,0"""

def add(operandA,operandB):
    return operandA+operandB

def multiply(operandA,operandB):
    return operandA * operandB

def reset():
    return list(map(int,code.split(sep=',')))

def computer(y,z):
    opcode_dup = reset()
    opcode_dup[1] = y
    opcode_dup[2] = z
    for x in range(0,len(opcode_dup),4):
        if opcode_dup[x] == 1:
            opcode_dup[opcode_dup[x+3]] = add(opcode_dup[opcode_dup[x+1]],opcode_dup[opcode_dup[x+2]])
        elif opcode_dup[x] == 2:
            opcode_dup[opcode_dup[x+3]] = multiply(opcode_dup[opcode_dup[x+1]],opcode_dup[opcode_dup[x+2]])
        elif opcode_dup[x] == 99:
            return opcode_dup[0]
        else:
            return

def guess():
    for x in range(0,100):
        for y in range(0,100):
            if computer(x,y) == 19690720 :
                return 100*x+y

# Part One
print(computer(12,2))

# Part Two
print(guess())