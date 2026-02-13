function solution(play_time, adv_time, logs) {
    const toSec = (time) => {
        const [h, m, s] = time.split(':').map(Number);
        return h * 3600 + m * 60 + s;
    }
    
    const toTime = (sec) => {
        const h = String(Math.floor(sec/3600)).padStart(2, '0');
        const m = String(Math.floor((sec % 3600) / 60)).padStart(2, '0');
        const s = String(sec % 60).padStart(2, '0');
        return `${h}:${m}:${s}`;
    }
    
    const playSec = toSec(play_time);
    const advSec = toSec(adv_time);
    
    const timeline = Array(playSec + 1).fill(0);
    
    for (let log of logs) {
        const [start, end] = log.split('-').map(toSec);
        timeline[start] += 1;
        timeline[end] -= 1;
    }
    
    for (let i = 1; i <= playSec; i++) {
        timeline[i] += timeline[i - 1];
    }
    
    for (let i = 1; i <= playSec; i++) {
        timeline[i] += timeline[i - 1]
    }
    
    let maxView = timeline[advSec];
    let maxStart = 0;
    
    for (let start = 1; start + advSec <= playSec; start++) {
        const end = start + advSec - 1;
        const viewTime = timeline[end] - timeline[start - 1];
        
        if (viewTime > maxView) {
            maxView = viewTime;
            maxStart = start;
        }
        
        
    }
    return toTime(maxStart);
}