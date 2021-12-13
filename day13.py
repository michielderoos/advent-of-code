X = 'X'
Y = 'Y'
# Returns string with plotted grid
def plot(grid):
    s = []
    s.append('\n')
    # I could calculate the grid size, but can't be bothered
    for x in range(10):
        for y in range(40):
            if (y, x) in grid: s.append('#')
            else: s.append('.')
        s.append('\n')
    return ''.join(s)


def part_one(input):
    dots = [] # [(3, 4), (5, 2)] where tuples are (x, y)
    folds = [] # [(5, Y), (3, X)...]
    for line in input:
        if 'fold along y=' in line: 
            folds.append((int(line.replace('fold along y=', '').rstrip()), Y))
            continue
        if 'fold along x=' in line: 
            folds.append((int(line.replace('fold along x=', '').rstrip()), X))
            continue
        elif not line.rstrip(): continue
        else: 
            dot = tuple([int(l.rstrip()) for l in line.split(',')])
            dots.append(dot)
    # This doesn't really have to be a loop because part one only cares about the first fold
    # Whatever though.
    for fold in folds:
        folded_dots = []
        for dot in dots:
            if fold[1] == Y:
                if fold[0] == dot[1]: continue
                if fold[0] < dot[1]: folded_dots.append((dot[0], abs(dot[1] - fold[0]*2)))
                else: folded_dots.append(dot)
            if fold[1] == X:
                if fold[0] == dot[0]: continue
                if fold[0] < dot[0]: folded_dots.append((abs(dot[0] - fold[0]*2), dot[1]))
                else: folded_dots.append(dot)
        dots = folded_dots
        return len(set(dots))

def part_two(input):
    dots = [] # [(3, 4), (5, 2)] where tuples are (x, y)
    folds = [] # [(5, Y), (3, X)...]
    for line in input:
        if 'fold along y=' in line: 
            folds.append((int(line.replace('fold along y=', '').rstrip()), Y))
            continue
        if 'fold along x=' in line: 
            folds.append((int(line.replace('fold along x=', '').rstrip()), X))
            continue
        elif not line.rstrip(): continue
        else: 
            dot = tuple([int(l.rstrip()) for l in line.split(',')])
            dots.append(dot)
    
    for fold in folds:
        folded_dots = []
        for dot in dots:
            if fold[1] == Y:
                if fold[0] == dot[1]: continue
                if fold[0] < dot[1]: folded_dots.append((dot[0], abs(dot[1] - fold[0]*2)))
                else: folded_dots.append(dot)
            if fold[1] == X:
                if fold[0] == dot[0]: continue
                if fold[0] < dot[0]: folded_dots.append((abs(dot[0] - fold[0]*2), dot[1]))
                else: folded_dots.append(dot)
        dots = folded_dots
    return plot(folded_dots)

if __name__ == '__main__':
    with open('day13.input.txt', 'r') as input:
        print(f'Part 1: {part_one(input)} is the solution')

    with open('day13.input.txt', 'r') as input:
        print(f'Part 2: {part_two(input)} is the solution')
