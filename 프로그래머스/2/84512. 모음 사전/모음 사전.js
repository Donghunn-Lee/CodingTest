function solution(word) {
    const dictionary = [];

    function dfs(currentWord) {
        if (currentWord.length > 5) return;
        
        if (currentWord.length > 0) dictionary.push(currentWord);

        const vowels = ['A', 'E', 'I', 'O', 'U'];
        for (const vowel of vowels) {
            dfs(currentWord + vowel);
        }
    }

    dfs("");
    
    return dictionary.indexOf(word) + 1;
}