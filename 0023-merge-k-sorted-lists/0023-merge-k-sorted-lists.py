import heapq

class Solution:
    def mergeKLists(self, lists):
        heap = []
        
        # push initial heads
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))  # i breaks ties

        dummy = ListNode(0)
        cur = dummy

        while heap:
            _, i, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        cur.next = None
        return dummy.next