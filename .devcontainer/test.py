import 


head = [3,2,0,-4]
pos = 1

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return false
            slow = slow.next
            fast = fast.next.next
            return True