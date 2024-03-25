/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    const MAX = 2147483647;
    const MIN = -2147483648;

    let negative = false;
    let absoluteNum = Math.abs(x);

    if (x < 0) {
        negative = true;
    }

    let str = String(absoluteNum);
    
    const strRev = str.split("").reverse().join("");

    const rev = strRev.toString();

    if (rev > MAX) {
        return 0;
    }

    if (negative) {

        negRev = rev * -1;

        if (negRev < MIN) {
            return 0;
        }

        return negRev;
    }

    return rev;

};