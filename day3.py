# Sloppy implementation, redone slightly nicer in part 2
def part_one(input):
    tally = []
    rows = 0
    for value in input:
        rows += 1
        value = value.rstrip()
        if(len(tally)) != len(value): tally = [0] * len(value)
        for position, char in enumerate(value):
            tally[position] += int(char)
    gamma = []
    for val in tally:
        if val >= rows/2: gamma.append(1)
        else: gamma.append(0)
    alpha = [abs(n - 1) for n in gamma]
    gamma = int(''.join(map(str, gamma)), 2)
    alpha = int(''.join(map(str, alpha)), 2)
    return alpha * gamma

def part_two(input):
    string_to_binary_list = lambda a : [int(a) for a in a.rstrip()] if type(a) == str else a
    binary_list_to_int = lambda a : int(''.join(map(str, a)), 2)
    calculate_list_modes = lambda row, length : [1 if n >= length/2 else 0 for n in row]
    # This is often inefficient since we usually only need to count once specific row
    def tally_and_count_matrix(matrix):
        tally = []
        row_count = 0
        for row in matrix:
            row_count += 1
            row = string_to_binary_list(row)
            if(len(tally)) != len(row): tally = [0] * len(row)
            for position, num in enumerate(row):
                tally[position] += num
        return tally, row_count

    def eliminate_rows(matrix, check_most_frequent=True):
        row, count = tally_and_count_matrix(matrix)
        for n in range(len(row)):
            modes = calculate_list_modes(row, count)
            if check_most_frequent:
                matrix = [r for r in matrix if string_to_binary_list(r[n]) == modes[n]]
            else:
                matrix = [r for r in matrix if string_to_binary_list(r[n]) != modes[n]]
            row, count = tally_and_count_matrix(matrix)
            if count == 1: 
                return row
    # I shouldn't store the whole list in memory like this
    input = [string_to_binary_list(l) for l in input]
    return binary_list_to_int(eliminate_rows(input, True)) * binary_list_to_int(eliminate_rows(input, False))

if __name__ == '__main__':
    input = open('day3.input.txt', 'r')
    print(f'Part 1: {part_one(input)} is the solution')
    input = open('day3.input.txt', 'r')
    print(f'Part 2: {part_two(input)} is the solution')
