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
console.log(groups[0] + groups[1] + groups[2]);
