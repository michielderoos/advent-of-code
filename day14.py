def part_one(input):
    STEPS = 10
    template = input.readline().rstrip()
    rules = {}
    letters = set()
    for line in input:
        if line.rstrip(): 
            input, output = line.split(' -> ')
            rules[input] = output.rstrip()
            for letter in input+output.rstrip():
                if letter: letters.add(letter)

    for _ in range(STEPS):
        output = []
        for first, second in zip(template, template[1:]):
            if not output: output.append(first)
            output.append(rules[first+second]) 
            output.append(second)
        template = output

    letter_counts = []
    for letter in letters:
        letter_counts.append(template.count(letter))
    letter_counts.sort()
    return letter_counts[-1] - letter_counts[0]

def part_two(input):
    STEPS = 40
    template = input.readline().rstrip()
    rules = {}
    pair_counts = {}
    letters = {}
    for line in input:
        if line.rstrip(): 
            input, output = line.split(' -> ')
            rules[input] = output.rstrip()
            pair_counts[input] = 0
            for letter in input+output.rstrip():
                if letter: letters[letter] = 0

    for first, second in zip(template, template[1:]):
        pair_counts[first+second] += 1

    for _ in range(STEPS):
        new_pair_counts = pair_counts.copy()
        new_pair_counts = dict.fromkeys(new_pair_counts, 0)
        for pair in pair_counts:
            new_pair_counts[pair[0] + rules[pair]] += pair_counts[pair]
            new_pair_counts[rules[pair] + pair[1]] += pair_counts[pair]
        pair_counts = new_pair_counts

    for p in pair_counts:
        letters[p[1]] += pair_counts[p]
    scores = list(letters.values())
    scores.sort()
    return scores[-1] - scores[0]

if __name__ == '__main__':
    with open('day14.input.txt', 'r') as input:
        print(f'Part 1: {part_one(input)} is the solution')

    with open('day14.input.txt', 'r') as input:
        print(f'Part 2: {part_two(input)} is the solution')
