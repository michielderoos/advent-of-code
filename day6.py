from typing import Deque
MIN_VAL = 0
RESET_VAL = 6
NEW_VAL = 8

def part_one(input):
    def simulate_fish(state, total_days):
        days = 0
        while days < total_days:
            state = [n-1 for n in state] # decrement State
            for idx, val in enumerate(state):
                if val < MIN_VAL:
                    state[idx] = RESET_VAL
                    state.append(NEW_VAL)
            days +=1
        return(len(state))
    input = [int(n) for n in input.readline().strip().split(',')]
    return simulate_fish(input, 18)

# Will also solve part one, but faster!
def part_two(input):
    def simulate_fish(input, total_days):
        state = [int(n) for n in input.readline().strip().split(',')]
        fish_on_day = Deque([0] * (NEW_VAL+1))
        for val in state: fish_on_day[val] = fish_on_day[val]+1
        for _ in range(total_days):
            zero_day_fish = fish_on_day[0]
            fish_on_day[NEW_VAL-1] += zero_day_fish
            fish_on_day.rotate(-1)
        return(sum(fish_on_day))
    return simulate_fish(input, 256)

if __name__ == '__main__':
    with open('day6.input.txt', 'r') as input:
        print(f'Part 1: {part_one(input)} is the solution')
    with open('day6.input.txt', 'r') as input:
        print(f'Part 2: {part_two(input)} is the solution')
