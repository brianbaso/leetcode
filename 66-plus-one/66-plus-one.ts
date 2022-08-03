function plusRecurse(digits: number[], n: number, carry: number): number[] {
    if (n < 0 && !carry) return digits
    
    if (n < 0 && carry) {
        digits.unshift(1)
        return digits
    }
    
    if (digits[n] < 9) {
        digits[n]++
        return digits
    }
    
    if (digits[n] === 9) {
        digits[n] = 0
        return plusRecurse(digits, n-1, 1)
    }
}

function plusOne(digits: number[]): number[] {
    return plusRecurse(digits, digits.length-1, 0)
};