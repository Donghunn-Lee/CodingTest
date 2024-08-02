function solution(players, callings) {
    let players_dict = {};
    players.forEach((e, idx) => players_dict[e] = idx);
    
    for (const name of callings) {
        let idx = players_dict[name]
        let tmp = players[idx - 1];

        players[idx - 1] = name;
        players[idx] = tmp;
        players_dict[name] -= 1;
        players_dict[tmp] += 1;
        
    }
    
    return players;
}

console.log(solution(	["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))