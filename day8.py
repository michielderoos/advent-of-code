from itertools import permutations, product

"""
 ┌───┬───────────────┬───┐
 │num│   positions   │len│
 │ 0 │ a,b,c,e,f,g   │ 6 │
 │ 1*│ c,f           │ 2 │
 │ 2 │ a,c,d,e,g     │ 5 │
 │ 3 │ a,c,d,f,g     │ 5 │
 │ 4*│ b,c,d,f       │ 4 │
 │ 5 │ a,b,d,f,g     │ 5 │
 │ 6 │ a,b,d,e,f,g   │ 6 │
 │ 7*│ a,c,f         │ 3 │
 │ 8*│ a,b,c,d,e,f,g │ 7 │
 │ 9 │ a,b,c,d,f,g   │ 6 │
 └───┴───────────────┴───┘
 * == unique position length
"""

sort_and_stringify_set = lambda s :  ''.join(sorted(list(s)))

NUM_POSITIONS = {
    '0': set(['a', 'b', 'c', 'e', 'f', 'g']),
    '1': set(['c', 'f']),
    '2': set(['a', 'c', 'd', 'e', 'g']),
    '3': set(['a', 'c', 'd', 'f', 'g']),
    '4': set(['b', 'c', 'd', 'f']),
    '5': set(['a', 'b', 'd', 'f', 'g']),
    '6': set(['a', 'b', 'd', 'e', 'f', 'g']),
    '7': set(['a', 'c', 'f']),
    '8': set(['a', 'b', 'c', 'd', 'e', 'f', 'g']),
    '9': set(['a', 'b', 'c', 'd', 'f', 'g']),
}
STR_POSITIONS_TO_NUMS = { ''.join(sorted(list(NUM_POSITIONS[num]))) : num for num in NUM_POSITIONS }
POSITION_LENGTHS = { pos: len(NUM_POSITIONS[pos]) for pos in NUM_POSITIONS }
LENGTH_TO_NUMS = {} # {6: {0, 9, 6}, 2: {1}, etc....}
for pos in POSITION_LENGTHS:
    if POSITION_LENGTHS[pos] in LENGTH_TO_NUMS: LENGTH_TO_NUMS[POSITION_LENGTHS[pos]].add(pos)
    else: LENGTH_TO_NUMS[POSITION_LENGTHS[pos]] = set([pos])
POSSIBLE_DISPLAYS = [n for n in NUM_POSITIONS.values()]
SEGMENTS = set(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
NUMBERS = list(NUM_POSITIONS.keys())

def part_one(input):
    count = 0
    for line in input:
        _, output = line.split('|')
        output = [char.rstrip() for char in output.strip().split(' ')]
        for char in output:
            if len(char) in [2, 4, 3, 7]:
                count += 1
    return count

def part_two(input):
    def check_display(display, mapping):
        decoded_chars = set()
        for char in display:
            decoded_chars.add(mapping[char])
        if decoded_chars not in POSSIBLE_DISPLAYS: return False
        return STR_POSITIONS_TO_NUMS[sort_and_stringify_set(decoded_chars)]

    final_num = 0
    for line in input:
        possible_mappings = {char:SEGMENTS for char in SEGMENTS}
        solved_displays = {}
        signal, output = line.split('|')
        signal = [char.rstrip() for char in signal.strip().split(' ')]
        output = [char.rstrip() for char in output.strip().split(' ')]
        all_displays = signal + output
        # Shrink possible_mappings using length first
        for display in all_displays:
            if len(LENGTH_TO_NUMS[len(display)]) == 1: solved_displays[list(LENGTH_TO_NUMS[len(display)])[0]] = set(display)
            possible_mappings_for_display = set()
            for num in LENGTH_TO_NUMS[len(display)]:
                possible_mappings_for_display = set.union(NUM_POSITIONS[num], possible_mappings_for_display)
            for segment in display:
                possible_mappings[segment] = possible_mappings[segment].intersection(possible_mappings_for_display)
        # Now remove impossible mappings based on the already solved displays
        # I.e. What does 7 and 1 NOT have in common? a! Narrow down possibilities based on that
        for disp_num_one, disp_num_two in permutations(solved_displays, 2):
            disp_one = NUM_POSITIONS[disp_num_one]
            disp_two = NUM_POSITIONS[disp_num_two]
            diff = disp_two - disp_one
            scrambled_disp_one = solved_displays[disp_num_one]
            scrambled_disp_two = solved_displays[disp_num_two]
            scrambled_diff = scrambled_disp_two - scrambled_disp_one
            for segment in scrambled_diff:
                possible_mappings[segment] = possible_mappings[segment] & diff
        # At this point, segments should only have one or two possible mappings each.
        # We can now make a set of presumptive mappings and see which one is right
        # This probably isn't the most efficient way to do this
        keys, values = zip(*possible_mappings.items())
        presumptive_mappables = [dict(zip(keys, v)) for v in product(*values)]
        final_mapping = None
        for mapping in presumptive_mappables:
            good_candidate = True
            for display in all_displays:
                display_status = check_display(display, mapping)
                if not display_status : good_candidate = False
                continue
            if good_candidate:
                final_mapping = mapping
        output_num = ''
        for line in output:
            output_num += check_display(line, final_mapping)
        final_num += int(output_num)
    return final_num

if __name__ == '__main__':
    with open('day8.input.txt', 'r') as input:
       print(f'Part 1: {part_one(input)} is the solution')

    with open('day8.input.txt', 'r') as input:
        print(f'Part 2: {part_two(input)} is the solution')
