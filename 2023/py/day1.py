def part1():
    with open("../day1.txt") as f:
        lines = f.readlines()

        sum = 0
        v1, v2 = 0, 0

        for line in lines:
            for c in line:
                if c.isdigit():
                    v1 = c
                    break

            for c in line[::-1]:
                if c.isdigit():
                    v2 = c
                    break

            sum += int(v1 + v2)

    return sum


print(f"Part 1: {part1()}")
