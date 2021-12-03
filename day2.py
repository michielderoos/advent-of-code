def part_one(input):
    horizontal = 0
    vertical = 0
    for line in input:
        direction, distance = line.rstrip().split(' ')
        distance = int(distance)
        if direction == 'forward':
            horizontal+= distance
        elif direction == 'up':
            vertical -= distance
        elif direction == 'down':
            vertical += distance
    return horizontal * vertical

def part_two(input):
    horizontal = 0
    vertical = 0
    aim = 0
    for line in input:
        direction, distance = line.rstrip().split(' ')
        distance = int(distance)
        if direction == 'forward':
            horizontal+= distance
            vertical += distance * aim
        elif direction == 'up':
            aim -= distance
        elif direction == 'down':
            aim += distance
    return horizontal * vertical
    
if __name__ == '__main__':
    input = open('day2.input.txt', 'r')
    print(f'Part 1: {part_one(input)} is the solution')
    input = open('day2.input.txt', 'r')
    print(f'Part 2: {part_two(input)} is the solution')
