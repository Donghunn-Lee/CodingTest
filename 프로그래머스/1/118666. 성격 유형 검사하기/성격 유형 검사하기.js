function solution(survey, choices) {
    var answer = '';
    let indicator = {
        'R' : 0,
        'T' : 0,
        'C' : 0,
        'F' : 0,
        'J' : 0,
        'M' : 0,
        'A' : 0,
        'N' : 0,
    }
    let points = [
        [3, 0],
        [2, 0],
        [1, 0],
        [0, 0],
        [0, 1],
        [0, 2],
        [0, 3],
    ]

    for (let i = 0; i < survey.length; i++) {
        indicator[survey[i][0]] += points[choices[i] - 1][0];
        indicator[survey[i][1]] += points[choices[i] - 1][1];
    }
    
    if (indicator['R'] < indicator['T']) answer += 'T';
    else if (indicator['R'] > indicator['T']) answer += 'R';
    else answer += 'R'
    
    if (indicator['C'] < indicator['F']) answer += 'F';
    else if (indicator['C'] > indicator['F']) answer += 'C';
    else answer += 'C'

    if (indicator['J'] < indicator['M']) answer += 'M';
    else if (indicator['J'] > indicator['M']) answer += 'J';
    else answer += 'J'

    if (indicator['A'] < indicator['N']) answer += 'N';
    else if (indicator['A'] > indicator['N']) answer += 'A';
    else answer += 'A'
    
    
    return answer;
}