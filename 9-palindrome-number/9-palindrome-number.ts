function isPalindrome(x: number): boolean {
    const xStr = x.toString()
    
    if (xStr.length < 2) return true;
    
    const firstHalf = (xStr.substring(0, xStr.length/2))
    
    const revSecondHalf = xStr.substring(xStr.length/2).split('').reverse().join('')
    
    if (xStr.length % 2 == 0) {
        return Boolean(!firstHalf.localeCompare(revSecondHalf))
    } else {
        return Boolean(!firstHalf.localeCompare(revSecondHalf.substring(0,revSecondHalf.length-1)))
    }
};