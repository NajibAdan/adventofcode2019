def add(operandA,operandB):
    return operandA+operandB

def multiply(operandA,operandB):
    return operandA * operandB

opcode = list(map(int,open('input.txt','r').read().split(sep=',')))

for x in range(0,len(opcode),4):
    if opcode[x] == 1:
        opcode[opcode[x+3]] = add(opcode[opcode[x+1]],opcode[opcode[x+2]])
    elif opcode[x] == 2:
        opcode[opcode[x+3]] = multiply(opcode[opcode[x+1]],opcode[opcode[x+2]])
    elif opcode[x] == 99:
        break

print(opcode)