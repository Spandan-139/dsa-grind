class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current1 = head
        current2 = head
        while current1 and current1.next:
            current1 = current1.next.next
            current2 = current2.next
            if current1 == current2:
                return True
        return False