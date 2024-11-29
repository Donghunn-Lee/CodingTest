function toLowercaseAlphabets(input) {
    return input.replace(/[A-Z]/g, (match) => match.toLowerCase());
}

function solution(new_id) {
    let processed = new_id.toLowerCase();
    processed = processed.replace(/[^a-z0-9-_.]/g, '');
    
    processed = processed.replace(/\.{2,}/g, '.');
    processed = processed.replace(/^\.|\.$/g, '');
    
    if (processed === '') {
        processed = 'a';
    }
    
    if (processed.length >= 16) {
        processed = processed.slice(0, 15).replace(/\.$/, '');
    }
    
    while (processed.length < 3) {
        processed += processed[processed.length - 1];
    }
    
    return processed;
}