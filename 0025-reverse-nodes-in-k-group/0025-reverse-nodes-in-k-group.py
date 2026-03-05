class Solution:
    def reverseKGroup(self, head, k: int):
        if k <= 1 or not head:
            return head

        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            # 1) find kth node from group_prev
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next  # not enough nodes

            group_next = kth.next  # node after the group

            # 2) reverse the group
            prev = group_next
            cur = group_prev.next
            while cur != group_next:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt

            # 3) reconnect
            old_group_start = group_prev.next  # becomes tail after reverse
            group_prev.next = kth              # kth is new head of this group
            group_prev = old_group_start       # move to tail for next iteration