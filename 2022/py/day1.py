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
print(largest)

