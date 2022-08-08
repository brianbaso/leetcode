function romanToInt(s: string): number {
    const key = new Map([
        ['I', 1], ['V', 5], ['X', 10],
        ['L', 50], ['C', 100], ['D', 500],
        ['M', 1000], ['IV', 4], ['IX', 9],
        ['XL', 40], ['XC', 90], ['CD', 400],
        ['CM', 900],  
    ])
    
    let total: number = 0;
    
    for (let i = 0; i < s.length; i++) {
        const sub = s.substring(i, i+2)
        
        if (key.has(sub)) {
            total += key.get(sub)
            i++;
        } 
        
        else if (key.has(sub[0])) {
            total += key.get(sub[0])
        }
    }
    
    return total
};