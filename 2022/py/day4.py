def part1():
    with open('../day4.txt') as f:
        lines = f.readlines()
        contained = 0
        for line in lines:
            pairs = line.split(',')
            pair1 = pairs[0].split('-')
            pair2 = pairs[1].split('-')

            # if left contains right
            if int(pair1[0]) <= int(pair2[0]) and int(pair1[1]) >= int(pair2[1]):
                contained += 1
            # if right contains left
            elif int(pair1[0]) >= int(pair2[0]) and int(pair1[1]) <= int(pair2[1]):
                contained += 1
    return contained
            
print(f'Part 1: {part1()}')

def part2():
    with open('../day4.txt') as f:
        lines = f.readlines()
        overlap = 0
        for line in lines:
            pairs = line.split(',')
            pair1 = pairs[0].split('-')
            pair2 = pairs[1].split('-')

            # check for overlap
            if int(pair1[0]) <= int(pair2[0]) <= int(pair1[1]):
                overlap += 1
            elif int(pair2[0]) <= int(pair1[0]) <= int(pair2[1]):
                overlap += 1
    return overlap

print(f'Part 2: {part2()}')

