/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
    let stack1 = [], stack2 = []
    
    while (l1 !== null) {
        stack1.push(l1.val)
        l1 = l1.next
    }
    
    while (l2 !== null) {
        stack2.push(l2.val)
        l2 = l2.next
    }
    
    let reverse1 = [], reverse2 = []
    
    while (stack1.length !== 0) {
        let num = stack1.pop()
        reverse1.push(num)
    }
    
    while (stack2.length !== 0) {
        let num = stack2.pop()
        reverse2.push(num)
    }
    
    const num1 = BigInt(reverse1.join(''))
    const num2 = BigInt(reverse2.join(''))
    const sum = num1 + num2

    
    const sumArray = sum.toString().split('').map(Number)
    
    let prev = new ListNode(sumArray[0]);
    let len = sumArray.length
    
    for (let i = 1; i < len; i++) {
        const current = new ListNode(sumArray[i], prev);
        prev = current
    }
    
    return prev
    
};