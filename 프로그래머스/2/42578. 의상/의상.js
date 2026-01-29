function solution(clothes) {
    let answer = 1;
    
    const clothesMap = new Map();
    
    clothes.forEach((e, idx) => {
        const [name, type] = e;
        
        if (!clothesMap.has(type)) clothesMap.set(type, []);
            
        clothesMap.get(type).push(name);    
    })
    
    for (const [type, name] of clothesMap) {
        answer *= name.length + 1;
    }
    
    return answer - 1;
}
