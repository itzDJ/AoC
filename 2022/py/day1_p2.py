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
print(groups[0] + groups[1] + groups[2])
