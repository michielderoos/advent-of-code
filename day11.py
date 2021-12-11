from sys import maxsize
MINSIZE = -maxsize
STEPS_TO_TAKE = 100

def find_neighbor_points(point, grid):
    directions = [
        (point[0], point[1]-1) if ((point[1]-1 >= 0)) else None, # up
        (point[0], point[1]+1) if ((point[1]+1 < len(grid))) else None, # down
        (point[0]-1, point[1]) if ((point[0]-1 >= 0)) else None, # left
        (point[0]+1, point[1]) if (point[0]+1 < len(grid[point[1]])) else None, # right
        (point[0]-1, point[1]-1) if ((point[0]-1 >= 0) and (point[1]-1 >= 0)) else None, # up-left
        (point[0]-1, point[1]+1) if ((point[0]-1 >= 0) and (point[1]+1 < len(grid))) else None, # down-left
        (point[0]+1, point[1]-1) if ((point[0]+1 < len(grid[point[1]])) and (point[1]-1 >= 0)) else None, # up-right
        (point[0]+1, point[1]+1) if ((point[0]+1 < len(grid[point[1]])) and (point[1]+1 < len(grid))) else None, # up-right
    ]
    return directions
    
# Flashes point, and cascades flashes caused by flashes
def flash_point(point, grid):
    grid[point[1]][point[0]] = MINSIZE # 
    for point in find_neighbor_points(point, grid):
        if point:
            grid[point[1]][point[0]] += 1
            if grid[point[1]][point[0]] > 9:
                flash_point(point, grid)
def part_one(input):
    flash_count = 0
    grid = [[int(char.rstrip()) for char in line.strip()] for line in input]
    for _ in range(STEPS_TO_TAKE):
        # Iterate
        for y, y_line in enumerate(grid):
            for x, _ in enumerate(y_line): grid[y][x] += 1
        # Flash/Cascade Flashes
        for y, y_line in enumerate(grid):
            for x, value in enumerate(y_line):
                if value == 10: flash_point((x, y), grid)
        # Replace sentinel negative values
        for y, y_line in enumerate(grid):
            for x, value in enumerate(y_line):
                if value < 0:
                    grid[y][x] = 0
                    flash_count += 1
    return flash_count

def part_two(input):
    grid = [[int(char.rstrip()) for char in line.strip()] for line in input]
    flash_count = 0
    iteration_number = 0
    while flash_count != len(grid[0]) * len(grid):
        # Iterate
        iteration_number += 1
        for y, y_line in enumerate(grid):
            for x, _ in enumerate(y_line): grid[y][x] += 1
        # Flash/Cascade Flashes
        for y, y_line in enumerate(grid):
            for x, value in enumerate(y_line):
                if value == 10: flash_point((x, y), grid)
        # Replace sentinel negative values
        flash_count = 0
        for y, y_line in enumerate(grid):
            for x, value in enumerate(y_line):
                if value < 0:
                    grid[y][x] = 0
                    flash_count += 1
    return iteration_number

if __name__ == '__main__':
    with open('day11.input.txt', 'r') as input:
        print(f'Part 1: {part_one(input)} is the solution')

    with open('day11.input.txt', 'r') as input:
        print(f'Part 2: {part_two(input)} is the solution')
