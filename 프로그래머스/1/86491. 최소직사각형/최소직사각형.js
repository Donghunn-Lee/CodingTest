function solution(sizes) {
    let [width, height] = [0, 0];
    
    for (let size of sizes) {
        let [w, h] = size;
        
        if (width < w || height < h) {
            if (width < h || height < w) {
                let [w1, h1] = [Math.max(width, w),  Math.max(height, h)];
                let [w2, h2] = [Math.max(width, h),  Math.max(height, w)];
                
                let wh = w1 * h1;
                let hw = w2 * h2;
                
                if (wh < hw) {
                    [width, height] = [w1, h1];
                } else {
                    [width, height] = [w2, h2];
                }
            }
        }
    }
    
    return width * height;
}