from statistics import median

def part_one(input):
    positions = [int(n) for n in input.readline().strip().split(',')]
    target_pos = median(positions)
    total_fuel = 0
    for p in positions:
        total_fuel += abs(p - target_pos)
    return int(total_fuel)

# Brute force, but with an average n/2 optimization
def part_two(input):
    summation = lambda n : (n * (n + 1))/2
    crab_positions = [int(n) for n in input.readline().strip().split(',')]
    potential_positions = range(min(crab_positions), max(crab_positions))
    prev_total_fuel = None
    for pos in potential_positions:
        total_fuel = 0
        for p in crab_positions:
            total_fuel += summation(abs(p - pos))
        if not prev_total_fuel: prev_total_fuel = total_fuel
        # If the sequence starts to increase, we've got the optimum point
        if total_fuel > prev_total_fuel:
            return int(prev_total_fuel)
        prev_total_fuel = total_fuel
    
if __name__ == '__main__':
    with open('day7.input.txt', 'r') as input:
        print(f'Part 1: {part_one(input)} is the solution')

    with open('day7.input.txt', 'r') as input:
        print(f'Part 2: {part_two(input)} is the solution')
