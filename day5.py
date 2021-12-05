def part_one(input):
    def parse_line(input_line):
        str_tuple_to_int_tuple = lambda s : tuple(map(int, s))
        point_str_to_tuple = lambda p : str_tuple_to_int_tuple(p.strip().split(','))
        start_point, finish_point = map(point_str_to_tuple, input_line.split('->'))
        return start_point, finish_point
    def get_line_values(start_point, finish_point):
        x_range = list(range(start_point[0], finish_point[0]+1) or range(finish_point[0], start_point[0]+1))
        y_range = list(range(start_point[1], finish_point[1]+1) or range(finish_point[1], start_point[1]+1))
        if len(x_range) == 1:
            x_point = start_point[0]
            for y in y_range: yield (x_point, y)
        elif len(y_range) == 1:
            y_point = start_point[1]
            for x in x_range: yield (x, y_point)

    points = set()
    overlaps = set()  
    for line in input:
        for point in get_line_values(*parse_line(line)):
            if point in points:
                overlaps.add(point)
            points.add(point)
    return len(overlaps)

def part_two(input):
    def parse_line(input_line):
        str_tuple_to_int_tuple = lambda s : tuple(map(int, s))
        point_str_to_tuple = lambda p : str_tuple_to_int_tuple(p.strip().split(','))
        start_point, finish_point = map(point_str_to_tuple, input_line.split('->'))
        return start_point, finish_point
    def get_line_values(start_point, finish_point):
        x_range = list(range(start_point[0], finish_point[0]+1) or range(finish_point[0], start_point[0]+1))
        y_range = list(range(start_point[1], finish_point[1]+1) or range(finish_point[1], start_point[1]+1))
        if len(x_range) == 1:
            x_point = start_point[0]
            for y in y_range: yield (x_point, y)
        elif len(y_range) == 1:
            y_point = start_point[1]
            for x in x_range: yield (x, y_point)
        else:
            if start_point[0] > finish_point[0] : y_range.reverse()
            if start_point[1] > finish_point[1] : y_range.reverse()
            for point in zip(x_range, y_range): yield point

    points = set()
    overlaps = set()  
    for line in input:
        for point in get_line_values(*parse_line(line)):
            if point in points:
                overlaps.add(point)
            points.add(point)
    return len(overlaps)

if __name__ == '__main__':
    with open('day5.input.txt', 'r') as input:
        print(f'Part 1: {part_one(input)} is the solution')
    with open('day5.input.txt', 'r') as input:
        print(f'Part 1: {part_two(input)} is the solution')
