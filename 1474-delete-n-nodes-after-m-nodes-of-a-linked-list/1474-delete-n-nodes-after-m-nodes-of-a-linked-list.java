/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteNodes(ListNode head, int m, int n) {
        ListNode prev_head = new ListNode(-1);
        prev_head.next = head;
        ListNode current = prev_head;
        ListNode prev = prev_head;
        
        while (current.next != null) {
            for (int i = 0; i < m; i++) {
                if (current.next != null) {
                    current = current.next;
                    prev = prev.next;
                }
            }

            for (int i = 0; i < n; i++) {
                if (current.next != null) {
                    current = current.next;
                }
            }
        
        prev.next = current.next;
        prev = current;
        
        }
        
        return head;
        
    }
}