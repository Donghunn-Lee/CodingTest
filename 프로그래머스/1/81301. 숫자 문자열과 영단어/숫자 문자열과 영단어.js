const numbers = {
    "zero":'0',
    "one":'1',
    "two":'2',
    "three":'3',
    "four":'4',
    "five":'5',
    "six":'6',
    "seven":'7',
    "eight":'8',
    "nine":'9',
}    
    

function solution(s) {
    let replacedString = s;
    
    for (const number in numbers) {
        const regex = new RegExp(number, "g");
        replacedString = replacedString.replace(regex, numbers[number]);
    }
    
    return +replacedString;
}