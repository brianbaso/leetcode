function climbStairs(n: number): number {
    if (n < 4) return n
    
    let fib = [1,1]
    
    for (let i = 2; i <= n; i++) {
        fib[i] = fib[i-2] + fib[i-1]
    }
    
    return fib[n]
};