def part_one(input):
    increased_count = 0
    prev_number = None
    for number in input:
        if not prev_number:
            prev_number = number
            continue
        if number > prev_number:
            increased_count += 1 
        prev_number = number  
    return increased_count

def part_two(input):
    WINDOW_LENGTH = 3
    windows = []
    for idx, number in enumerate(input):
        windows.append([])
        for n in range(WINDOW_LENGTH):
            window_index = idx - n 
            if window_index >= 0:
                windows[window_index].append(number)
    increased_count = 0
    prev_window = None
    for w in windows:
        if not prev_window:
            prev_window = w
            continue
        if sum(prev_window) < sum(w):
            increased_count += 1
        prev_window = w
    return increased_count

if __name__ == '__main__':
    input = open('day1.input.txt', 'r')
    input_numbers = []
    for line in input:
        input_numbers.append(int(line.rstrip()))
    print(f'Part 1: {part_one(input_numbers)} numbers have increased')
    print(f'Part 2: {part_two(input_numbers)} sliding windows have increased')
