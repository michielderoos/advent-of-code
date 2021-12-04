# ---This is a 3am solution. Please don't judge it too harshly---

def part_one(input):
    drawn_numbers = [int(n) for n in input.readline().rstrip().split(',')]
    boards = []
    for line in input:
        if line == '\n': boards.append([])
        else: boards[-1].append([int(n) for n in line.strip().replace('  ', ' ').split(' ')])

    transposed_boards = [list(map(list, zip(*board))) for board in boards] # Now we only need to check rows, at the expense of some memory

    for num in drawn_numbers:
        for board in boards + transposed_boards: 
            for row in board:
                if num in row: row.remove(num)
                if not row: return sum(map(sum, board)) * num

def part_two(input):
    drawn_numbers = [int(n) for n in input.readline().rstrip().split(',')]
    boards = []
    for line in input:
        if line == '\n': boards.append([])
        else: boards[-1].append([int(n) for n in line.strip().replace('  ', ' ').split(' ')])

    transposed_boards = [list(map(list, zip(*board))) for board in boards] # Now we only need to check rows, at the expense of some memory
    winning_boards = []
    winning_board_indexes = []
    for num in drawn_numbers:
        for idx, board in enumerate(boards + transposed_boards): 
            if idx >= len(boards): idx-=len(boards) # Ugly hack to make one index cover both boards
            if idx not in winning_board_indexes:
                for row in board:
                    if num in row: row.remove(num)
                    if not row:
                        winning_boards.append((board, num))
                        winning_board_indexes.append(idx)
    winner, winning_number = winning_boards[-1]
    return sum(map(sum, winner)) * winning_number

if __name__ == '__main__':
    with open('day4.input.txt', 'r') as input:
        print(f'Part 1: {part_one(input)} is the solution')

    with open('day4.input.txt', 'r') as input:
        print(f'Part 2: {part_two(input)} is the solution')
