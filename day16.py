from functools import reduce

hex_to_bin = lambda input : bin(int(input,16))[2:]
bin_to_int = lambda input : int(''.join(input), 2)
read_version = lambda bits : bin_to_int(bits[:3])
read_type = lambda bits : bin_to_int(bits[:6][3:])

version_tally = 0

# Takes literal value from first chunk of input, then returns the rest of the input
# I.e. D2FE28DDDD -> 0xD2FE28 becomes 2021, return DDDD to process later
def read_literal_value(input):
    input = input[6:] # Strip header
    chunk_size = 5
    value = []
    for i in range(0, len(input), chunk_size):
        chunk = input[i:i+chunk_size]
        sign = chunk[0]
        data = chunk[1:]
        value.append(data)
        if sign == '0':
            return bin_to_int(value), input[i+chunk_size:]

# Takes operator, processes it, and returns the rest of the input
def read_operator(input):
    input_type = read_type(input)
    input = input[6:] # Strip header
    length_type_id = input[0]
    if length_type_id == '0':
        subpacket_length = bin_to_int(input[1:16])
        subpackets = input[16:subpacket_length+16]
        output = []
        while subpackets:
            out, subpackets = read_packet(subpackets)
            output.append(out)
        return parse_operator_output(output, input_type), input[subpacket_length+16:]
    if length_type_id == '1':
        subpacket_count = bin_to_int(input[1:12])
        subpackets = input[12:]
        output = []
        for _ in range(subpacket_count):
            out, subpackets = read_packet(subpackets)
            output.append(out)
        return parse_operator_output(output, input_type), subpackets

# Process operator input
# E.g. takes values [1, 2, 3], 0 (where type 0 is sum), return 6
def parse_operator_output(values, type):
    # Processing functions
    product = lambda values : reduce(lambda x, y: x*y, values)
    gt = lambda values : 1 if values[0] > values [1] else 0
    lt = lambda values : 1 if values[0] < values [1] else 0
    et = lambda values : 1 if values[0] == values [1] else 0

    processing_functions = {
        0 : sum,
        1 : product,
        2 : min,
        3 : max,
        5 : gt,
        6 : lt,
        7 : et,
    }
    return processing_functions[type](values)

def read_packet(input):
    global version_tally # Shame on me
    version = read_version(input)
    input_type = read_type(input)
    version_tally += version
    if input_type == 4:
        return read_literal_value(input)
    else: 
        return read_operator(input)

def part_one(input):
    binary_input = hex_to_bin(input.readline())
    binary_input = '0' * (len(binary_input) % 4) + binary_input
    read_packet(binary_input)
    return version_tally
    
def part_two(input):
    binary_input = hex_to_bin(input.readline())
    binary_input = '0' * (len(binary_input) % 4) + binary_input
    return read_packet(binary_input)[0]

if __name__ == '__main__':
    with open('day16.input.txt', 'r') as input:
        print(f'Part 1: {part_one(input)} is the solution')

    with open('day16.input.txt', 'r') as input:
        print(f'Part 2: {part_two(input)} is the solution')
