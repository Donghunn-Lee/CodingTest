const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = [line];
}).on('close',function(){
    str = input[0];
    ans = '';
    
    for (s of str){
        if (s === s.toUpperCase()){
            ans += s.toLowerCase();
        } else {
            ans += s.toUpperCase();
        }
    }
    
    console.log(ans);
    
});