def ArrToLinkedList(arr):
    head = ListNode()
    curr = head

    for v in arr:
        curr.next = ListNode(v)
        curr = curr.next
        print(curr.val)
    return head.next


class Solution(object):

    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        arr = []
        for lst in lists:
            curr = lst
            while curr:
                arr.append(curr.val)
                curr = curr.next

        arr.sort()
        yooo = ArrToLinkedList(arr)
        return yooo
