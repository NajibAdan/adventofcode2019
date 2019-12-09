from collections import defaultdict
code = open('input.txt','r').readline()
def add(operandA,operandB):
    return operandA+operandB

def multiply(operandA,operandB):
    return operandA * operandB

def computer(values,input):
    opcode_dup = defaultdict(int, [(i, values[i]) for i in range(len(values))])
    outputs = []
    x = 0
    while True:
        c_ode = opcode_dup[x] % 100
        position1 = (opcode_dup[x] // 100 % 10) == 0
        position2 = (opcode_dup[x] // 1000 % 10) == 0
        
        if position1 is True:
            arg1=opcode_dup[opcode_dup[x+1]]
        else:
            arg1 = opcode_dup[x+1]
        
        if position2 is True:
            arg2 = opcode_dup[opcode_dup[x+2]]
        else:
            arg2 = opcode_dup[x+2]

        if c_ode == 1:
            opcode_dup[opcode_dup[x+3]] = add(arg1,arg2)
            x+=4
        elif c_ode == 2:
            opcode_dup[opcode_dup[x+3]] = multiply(arg1,arg2)
            x+=4
        elif c_ode == 3:
            opcode_dup[opcode_dup[x+1]] = input.pop(0)
            x+=2
        elif c_ode == 4:
            outputs.append(arg1)
            x += 2
        elif c_ode == 5:
            if arg1 != 0:
                x = arg2
            else:
                x+=3
        elif c_ode == 6:
            if arg1 == 0:
                x = arg2
            else:
                x+=3
        elif c_ode == 7:
            if arg1 < arg2:
                opcode_dup[opcode_dup[x + 3]] = 1
            else:
                opcode_dup[opcode_dup[x + 3]] = 0
            x+=4
        elif c_ode == 8:
            if arg1 == arg2:
                opcode_dup[opcode_dup[x + 3]] = 1
            else:
                opcode_dup[opcode_dup[x + 3]] = 0
            x+=4
        elif c_ode == 99:
            break
    return outputs

# Part One
print(computer(list(map(int,code.split(sep=','))),[1]))

# Part Two
print(computer(list(map(int,code.split(sep=','))),[5]))