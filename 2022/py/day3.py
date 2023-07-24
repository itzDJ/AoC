def part1():
    with open('../day3.txt') as f:
        lines = f.readlines()
        total = 0
        for line in lines:
            # iterate through first half
            for c in line[:len(line)//2]:
                # check if the corresponding character is in the second half
                if c in line[len(line)//2:]:
                    # add the value of the character to the total and
                    # break the inner loop which will move to the next character
                    # preventing it from being added again if it repeats in the second half
                    if c.isupper():
                        total += ord(c) - 38
                    else:
                        total += ord(c) - 96
                    break
    return total

print(part1())

def part2():
    with open('../day3.txt') as f:
        lines = f.readlines()
        total = 0
        for i in range(0, len(lines), 3):
            for c in lines[i]:
                if c in lines[i+1] and c in lines[i+2]:
                    if c.isupper():
                        total += ord(c) - 38
                    else:
                        total += ord(c) - 96
                    break
    return total

print(part2())

