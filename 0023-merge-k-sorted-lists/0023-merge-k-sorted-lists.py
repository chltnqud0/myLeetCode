# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        answer = ListNode()
        temp = answer
        flag = True
        if len(lists) == 0:
            return None
        while lists:
            comp = 10001
            index = 10001
            lst = []
            for i in range(len(lists)):
                if not lists[i]:
                    lst.append(i)
                elif lists[i].val < comp:
                    comp = lists[i].val
                    index = i
            if index == 10001:
                break
            temp.val = comp
            flag = False
            if lists[index].next:
                lists[index] = lists[index].next
            else:
                lst.append(index)
            lst.sort(reverse=True)
            for t in lst:
                del lists[t]

            if lists:
                temp.next = ListNode()
                temp = temp.next
        if flag:
            return None
        return answer
