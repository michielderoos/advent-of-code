def part_one(input):
    graph = {}
    for line in input: 
        start, end = line.rstrip().split('-')
        if start in graph: graph[start].append(end)
        else: graph[start] = [end]
        if end in graph: graph[end].append(start)
        else: graph[end] = [start]

    def get_paths(graph):
        start_to_end = []

        def traverse(start_point, visited_caves = []):
            visited_caves = visited_caves.copy()
            visited_caves.append(start_point)
            for point in graph[start_point]:
                if point.islower() and point in visited_caves: continue
                if point == 'end': start_to_end.append(visited_caves + ['end'])
                else: traverse(point, visited_caves)

        traverse('start')
        return start_to_end

    return len(get_paths(graph))

def part_two(input):
    graph = {}
    for line in input: 
        start, end = line.rstrip().split('-')
        if start in graph: graph[start].append(end)
        else: graph[start] = [end]
        if end in graph: graph[end].append(start)
        else: graph[end] = [start]

    def get_paths(graph):
        start_to_end = []

        def traverse(start_point, visited_caves = [], can_revisit_small_cave = True):
            visited_caves = visited_caves.copy()
            visited_caves.append(start_point)
            for point in graph[start_point]:
                if point.islower() and not can_revisit_small_cave and point in visited_caves: continue
                if point.islower() and point in visited_caves: 
                    if point != 'start': traverse(point, visited_caves, False)
                elif point == 'end': start_to_end.append(visited_caves + ['end'])
                else: traverse(point, visited_caves, can_revisit_small_cave)
                
        traverse('start')
        return start_to_end

    return len(get_paths(graph))
    
if __name__ == '__main__':
    with open('day12.input.txt', 'r') as input:
        print(f'Part 1: {part_one(input)} is the solution')

    with open('day12.input.txt', 'r') as input:
        print(f'Part 2: {part_two(input)} is the solution')
