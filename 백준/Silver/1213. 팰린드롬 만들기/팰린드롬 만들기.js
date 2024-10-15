const filePath = process.platform == 'linux' ? '/dev/stdin' : './input.txt';
const input = require('fs').readFileSync(filePath).toString().trim().split('').sort();

const [head, body] = [[], []];
while (input.length) {
  const first = input.shift();
  const idx = input.indexOf(first);
  if (idx === -1) body.push(first);
  else {
    head.push(first);
    input.splice(idx, 1);
  }
}
const tail = [...head].reverse().join('');
if (body.length > 1) console.log("I'm Sorry Hansoo");
else console.log(head.join('') + body.join('') + tail);