function mySqrt(x: number): number {
    if (x < 2) return x
    
    let i = 0
    while (i * i <= x) i++
    
    return i-1
};