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
console.log(largest);
