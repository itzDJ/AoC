function part1() {
    // Read the file and convert to an array
    const fs = require('fs');
    const content = fs.readFileSync('../day1.txt', 'utf8').split('\n');

    let nums = 0;
    let largest = 0;

    for (let i = 0; i < content.length; ++i) {
        if (content[i] !== '') {
            nums += Number(content[i]);
        } else {
            if (nums > largest) {
                largest = nums;
            }
            nums = 0;
        }
    }
    return largest;
}

console.log(part1());

function part2() {
    // Read the file and convert to an array
    const fs = require('fs');
    const content = fs.readFileSync('../day1.txt', 'utf8').split('\n');

    let nums = 0;
    let groups = [];

    for (let i = 0; i < content.length; ++i) {
        if (content[i] !== '') {
            nums += Number(content[i]);
        } else {
            groups.push(nums);
            nums = 0;
        }
    }
    // sort the array in reverse order
    groups.sort();
    groups.reverse();
    return groups[0] + groups[1] + groups[2];
}

console.log(part2());
