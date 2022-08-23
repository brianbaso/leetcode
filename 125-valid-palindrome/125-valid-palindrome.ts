function isPalindrome(s: string): boolean {
    const str = s.replace(/[^0-9a-z]/gi, '').toLowerCase()
    const isEven = str.length % 2 === 0
    const s1 = str.substring(0, str.length/2)
    const s2 = str.substring(isEven ? str.length/2 : str.length/2+1, str.length)
    const rev = s2.split("").reverse().join("")
        
    return !s1.localeCompare(rev)
};