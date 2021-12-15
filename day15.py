import time

START_POINT = (0, 0)
END_POINT = (9, 9)

def find_neighbor_points(point, grid):
    directions = [
        (point[0], point[1]+1) if ((point[1]+1 < len(grid))) else None, # down
        (point[0]+1, point[1]) if (point[0]+1 < len(grid[point[1]])) else None, # right
    ]
    return directions

def get_point_value(point, grid):
    if point: return grid[point[1]][point[0]]

def get_cheapest_point(points, grid):
    lowest_value = float('inf')
    lowest_point = None
    for point in points:
        if point:
            point_val = get_point_value(point, grid)
            if point_val <= lowest_value:
                lowest_value = point_val
                lowest_point = point
    return lowest_point

def find_neighbor_points(point, grid):
    directions = [
        (point[0], point[1]-1) if ((point[1]-1 >= 0)) else None, # up
        (point[0], point[1]+1) if ((point[1]+1 < len(grid))) else None, # down
        (point[0]-1, point[1]) if ((point[0]-1 >= 0)) else None, # left
        (point[0]+1, point[1]) if (point[0]+1 < len(grid[point[1]])) else None, # right
    ]
    return directions


def part_one(input):
    grid = [[int(char.rstrip()) for char in line.strip()] for line in input]
    END_POINT = (len(grid[0])-1 , len(grid)-1)

    lowest_value_to_point = {}
    # If this is the most efficient way to get to a point so far, return true
    def handle_lowest_value(point, cost):
        if point not in lowest_value_to_point:
            lowest_value_to_point[point] = cost
            return True
        elif lowest_value_to_point[point] > cost: 
            lowest_value_to_point[point] = cost
            return True
        else:
            return False

    # These two could be zipped, but that would make some min() logic slightly more complicated later on
    # I'm busy, so just pretend for today :)
    paths = [[START_POINT]]
    path_costs = [0]
    while True:
        # Figure out the cheapest path so-far
        cheapest_path_index = path_costs.index(min(path_costs))
        cheapest_path = paths[cheapest_path_index]
        # Find the cheapest neighbor, then keep it aside for a mintue
        neighbors = find_neighbor_points(cheapest_path[-1], grid)
        cheapest_neighbor_point = get_cheapest_point(neighbors, grid)
        neighbors.remove(cheapest_neighbor_point)

        # First handle all non-cheapest points
        for point in neighbors:
            cost_to_point = get_point_value(point, grid)
            if cost_to_point:
                if handle_lowest_value(point, cost_to_point + path_costs[cheapest_path_index]):
                    new_path = cheapest_path.copy()
                    new_path.append(point)
                    paths.append(new_path)
                    path_costs.append(cost_to_point + path_costs[cheapest_path_index])

        # Then add the cheapest neighbor to the current cheapest path (if it's optimal)
        cost_to_point = get_point_value(cheapest_neighbor_point, grid) 
        if cost_to_point:
            if handle_lowest_value(cheapest_neighbor_point, cost_to_point + path_costs[cheapest_path_index]):
                cheapest_path.append(cheapest_neighbor_point)
                path_costs[cheapest_path_index] += cost_to_point
            else:
                cost = path_costs[cheapest_path_index]
                del paths[cheapest_path_index]
                del path_costs[cheapest_path_index]
                # I don't know why this works
                if not path_costs:
                    return cost
        if cheapest_neighbor_point == END_POINT:
            return path_costs[cheapest_path_index]


def part_two(input):
    STRETCH_X = 5
    STRETCH_Y = 5

    def find_neighbor_points(point, grid):
        directions = [
            (point[0], point[1]-1) if ((point[1]-1 >= 0)) else None, # up
            (point[0], point[1]+1) if ((point[1]+1 < len(grid))) else None, # down
            (point[0]-1, point[1]) if ((point[0]-1 >= 0)) else None, # left
            (point[0]+1, point[1]) if (point[0]+1 < len(grid[point[1]])) else None, # right
        ]
        return directions

    grid = [[int(char.rstrip()) for char in line.strip()] for line in input]
    
    # Stretch X axis
    for idx, row in enumerate(grid):
        new_row = row
        for _ in range(STRETCH_X - 1):
            new_row = [x+1 if x+1 != 10 else 1 for x in new_row]
            grid[idx] = grid[idx] + new_row
    # Stretch Y axis
    last_row = grid.copy()
    for _ in range(STRETCH_Y -  1):
        for idx, row in enumerate(last_row):
            last_row[idx] = [x+1 if x+1 != 10 else 1 for x in row]
        for row in last_row:
            grid.append(row)


    END_POINT = (len(grid[0])-1 , len(grid)-1)

    lowest_value_to_point = {}
    # If this is the most efficient way to get to a point so far, return true
    def handle_lowest_value(point, cost):
        if point not in lowest_value_to_point:
            lowest_value_to_point[point] = cost
            return True
        elif lowest_value_to_point[point] > cost: 
            lowest_value_to_point[point] = cost
            return True
        else:
            return False

    # These two could be zipped, but that would make some min() logic slightly more complicated later on
    # I'm busy, so just pretend for today :)
    paths = [[START_POINT]]
    path_costs = [0]
    while True:
        # Figure out the cheapest path so-far
        cheapest_path_index = path_costs.index(min(path_costs))
        cheapest_path = paths[cheapest_path_index]
        # Find the cheapest neighbor, then keep it aside for a mintue
        neighbors = find_neighbor_points(cheapest_path[-1], grid)
        cheapest_neighbor_point = get_cheapest_point(neighbors, grid)
        neighbors.remove(cheapest_neighbor_point)

        # First handle all non-cheapest points
        for point in neighbors:
            cost_to_point = get_point_value(point, grid)
            if cost_to_point:
                if handle_lowest_value(point, cost_to_point + path_costs[cheapest_path_index]):
                    new_path = cheapest_path.copy()
                    new_path.append(point)
                    paths.append(new_path)
                    path_costs.append(cost_to_point + path_costs[cheapest_path_index])

        # Then add the cheapest neighbor to the current cheapest path (if it's optimal)
        cost_to_point = get_point_value(cheapest_neighbor_point, grid) 
        if cost_to_point:
            if handle_lowest_value(cheapest_neighbor_point, cost_to_point + path_costs[cheapest_path_index]):
                cheapest_path.append(cheapest_neighbor_point)
                path_costs[cheapest_path_index] += cost_to_point
            else:
                cost = path_costs[cheapest_path_index]
                del paths[cheapest_path_index]
                del path_costs[cheapest_path_index]
                # I don't know why this works
                if not path_costs:
                    return cost
        if cheapest_neighbor_point == END_POINT:
            return path_costs[cheapest_path_index]

if __name__ == '__main__':
    with open('day15.input.txt', 'r') as input:
        print(f'Part 1: {part_one(input)} is the solution')

    with open('day15.input.txt', 'r') as input:
        print(f'Part 2: {part_two(input)} is the solution')

