function isAnagram(s: string, t: string): boolean {
    if (s.length !== t.length) return false
    
    let map = new Map();
    
    const sChar = s.split("")
    
    for (let i = 0; i < sChar.length; i++) {
        map.set(sChar[i], map.get(sChar[i]) ? map.get(sChar[i]) + 1 : 1)
    }
    
    const tChar = t.split("")
    
    for (let i = 0; i < tChar.length; i++) {
        map.set(tChar[i], map.get(tChar[i]) - 1)
    }
    
    // Check if map is not empty
    for (let i = 0; i < sChar.length; i++) {
        if (map.get(sChar[i]) !== 0) return false
    }
    
    return true
};