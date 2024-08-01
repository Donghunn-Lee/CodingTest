function solution(bandage, health, attacks) {
    const max_hp = health
    const end_time = attacks.at(-1)[0];
    const recovery_time = bandage[0], recovery = bandage[1], bonus = bandage[2];
    let cur_hp = health;
    let attack_num = 0;
    let cur_time = 1;
    let streak = 1;
    
    while (cur_time <= end_time) {        
        if (attacks[attack_num][0] === cur_time) {
            cur_hp -= attacks[attack_num][1];

            if (cur_hp <= 0) {
                return -1;
            }

            attack_num++;
            cur_time++;
            streak = 0;

            continue;
        }
        
        let nxt_hp = 0;
        streak++;

        if (streak === recovery_time) {    
            nxt_hp = cur_hp + recovery + bonus;
            streak = 0;
        } else {
            nxt_hp = cur_hp + recovery;
        }
        
        cur_hp = nxt_hp >= max_hp ? max_hp : nxt_hp;
        cur_time++;
        
    }
    
    return cur_hp;
}