function solution(players, callings) {
    let players_dict = {};
    players.forEach((e, idx) => players_dict[e] = idx);
    
    for (const name of callings) {
        let tmp = players[players_dict[name] - 1];

        players[players_dict[name] - 1] = name;
        players[players_dict[name]] = tmp;
        players_dict[name] -= 1;
        players_dict[tmp] += 1;
        
    }
    
    return players;
}

console.log(solution(	["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))