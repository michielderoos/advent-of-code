BRACKETS = { '{' : '}', '[' : ']', '(' : ')', '<' : '>', }
def part_one(input):
    SCORES = { ')': 3, ']': 57, '}':1197, '>': 25137 }
    open_brackets = []
    score = 0
    for l in input:
        line = [char for char in l.strip()]
        for b in line:
            if b in BRACKETS:
                open_brackets.append(b)
            else:
                if BRACKETS[open_brackets[-1]] != b:
                    score += SCORES[b]
                open_brackets.pop()
    return score

def part_two(input):
    SCORES = { ')': 1, ']': 2, '}':3, '>': 4 }
    final_scores = []
    for l in input:
        line = [char for char in l.strip()]
        open_brackets = []
        valid_line = True
        for b in line:
            if valid_line:
                if b in BRACKETS: open_brackets.append(b)
                else:
                    if BRACKETS[open_brackets[-1]] != b:
                        valid_line = False
                        continue
                    open_brackets.pop()
        if valid_line:
            rest_of_line = []
            while open_brackets: rest_of_line.append(BRACKETS[open_brackets.pop()])
            score = 0
            for c in rest_of_line:
                score *= 5
                score += SCORES[c]
            final_scores.append(score)
    final_scores.sort()
    return final_scores[int(len(final_scores)/2)]

if __name__ == '__main__':
    with open('day10.input.txt', 'r') as input:
        print(f'Part 1: {part_one(input)} is the solution')

    with open('day10.input.txt', 'r') as input:
        print(f'Part 2: {part_two(input)} is the solution')
