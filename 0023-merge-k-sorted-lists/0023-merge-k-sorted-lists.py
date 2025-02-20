# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        hq = []
        
        for i in range(len(lists)):
            if not lists[i]:
                continue
            else:
                temp = lists[i]
                while True:
                    heapq.heappush(hq, temp.val)
                    if temp.next:
                        temp = temp.next
                    else:
                        break

        if not hq:
            return None
        answer = ListNode()
        pointer = answer
        length = len(hq)
        for h in range(length):
            pointer.val = heapq.heappop(hq)
            if h != length - 1:
                pointer.next = ListNode()
                pointer = pointer.next

        return answer