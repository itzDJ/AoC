def part1():
    with open('../day1.txt') as f:
        # get every line of the file in a list
        content = f.readlines()

        # start at beginning of list and add nums to var until '\n'
        nums = 0
        largest = 0
        for num in content:
            if num != '\n':
                nums += int(num)
            else:
                # if the current group is larger than the largest, set largest to current
                if nums > largest:
                    largest = nums
                # reset the group count
                nums = 0
    return largest

print(part1())

def part2():
    with open('../day1.txt') as f:
        # get every line of the file in a list
        content = f.readlines()

        # start at beginning of list and add nums to var until '\n'
        nums = 0
        groups = []
        for num in content:
            if num != '\n':
                nums += int(num)
            else:
                # reset the group count
                groups.append(nums)
                nums = 0

    groups.sort(reverse=True)
    return groups[0] + groups[1] + groups[2]

print(part2())

