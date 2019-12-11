
def partion(data,size):
    return [data[i:i+size] for i in range(0, len(data),size)]
def decode(data):
    size = 25 * 6
    parts = partion(data,size)
    print("Part One: ",checksum([group(part) for part in parts],parts))
    print("Part Two:")
    print(print_image(image(data,size),25,6))
    return 0

def group(segment):
    return segment.count('0')

def checksum(number_of_zeroes,data):
    position = number_of_zeroes.index(min(number_of_zeroes))
    return data[position].count('1') * data[position].count('2')

def image(data,size):
    output = ''
    for i in range(size):
        for j in range(size):
            if data[i + j * size] != '2':
                output += data[i+j*size]
                break
    return output

def print_image(image,width,height):
    for row in partion(image,width):
        for pixel in row:
            if pixel == '1':
                glyph = '\u2591'
            else:
                glyph = ' '
            print(glyph, end="")
        print()
        
with open('input.txt') as file:
    data = file.readline().strip()

decode(data)