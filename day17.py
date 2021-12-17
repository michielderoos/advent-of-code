import re

# One of the rare times I was clever for part 1 and brute-force for part 2

ABOVE = 'ABOVE'
BELOW = 'BELOW'
LEFT = 'LEFT'
RIGHT = 'RIGHT'
INSIDE = 'INSIDE'

def is_in_square(point, top_left, bottom_right):
    if point[1] > top_left[1]: return ABOVE
    if point[1] < bottom_right[1]: return BELOW
    if point[0] < top_left[0]: return LEFT
    if point[0] > bottom_right[0]: return RIGHT
    return INSIDE

def plot_trajectory(velocity):
    x_velocity, y_velocity = velocity
    point = list(velocity)
    yield tuple(point)
    while True:
        y_velocity -= 1
        if x_velocity != 0: x_velocity -= 1
        point[0] += x_velocity
        point[1] += y_velocity
        yield tuple(point)

def will_land_in_square(velocity, top_left, bottom_right):
    for point in plot_trajectory(velocity):
        relative_pos = is_in_square(point, top_left, bottom_right)
        if relative_pos == RIGHT or relative_pos == BELOW: return False
        if relative_pos == INSIDE: return True

def part_one(input):
    input = input.readline()
    input = re.split('\.|\=|\,', input) # I should be arrested for this
    top_left_point = (int(input[1]), int(input[7]))
    bottom_right_point = (int(input[3]), int(input[5]))
    trajectory = [1, 1]
    # Once we go straight from above to below once, enter peck mode.
    # At this point, there will be one band of successful throws left
    # The last of highest of these landing inside the target will be the highest 
    peck_mode = False 
    in_pecking_band = False
    while True:
        prev_relative_pos = ABOVE
        peak_y = 0
        for pos in plot_trajectory(trajectory):
            if pos[1] > peak_y: peak_y = pos[1]
            relative_pos = is_in_square(pos, top_left_point, bottom_right_point)
            if relative_pos == BELOW and prev_relative_pos == LEFT: # Throw farther forward
                trajectory[0] += 1
                break
            if relative_pos == INSIDE: # Good throw! Now go for more height
                if peck_mode: 
                    in_pecking_band = True
                trajectory[1] += 1
                break
            if relative_pos == BELOW and prev_relative_pos == RIGHT: # Overshot, throttle back
                trajectory[0] -= 1
                break
            if relative_pos == BELOW and prev_relative_pos == ABOVE: # Going too fast
                peck_mode = True
                trajectory[1] += 1
                if in_pecking_band:
                    return old_peak_y
                break
            prev_relative_pos = relative_pos
        old_peak_y = peak_y

def part_two(input):
    input = input.readline()
    input = re.split('\.|\=|\,', input) # I should be arrested for this
    top_left_point = (int(input[1]), int(input[7]))
    bottom_right_point = (int(input[3]), int(input[5]))

    valid_points = 0
    min_y = bottom_right_point[1]
    max_y = abs(bottom_right_point[1]) + 1  # Discovered this to be the case in step 1
    min_x = 0
    max_x = bottom_right_point[0] + 1
    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            if will_land_in_square((x, y), top_left_point, bottom_right_point):
                valid_points += 1
    return valid_points


if __name__ == '__main__':
    with open('day17.input.txt', 'r') as input:
        print(f'Part 1: {part_one(input)} is the solution')

    with open('day17.input.txt', 'r') as input:
        print(f'Part 2: {part_two(input)} is the solution')
