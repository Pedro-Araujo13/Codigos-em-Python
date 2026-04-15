#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def mergeTwoLists(self, list1:ListNode, list2:ListNode):
        dummy = ListNode(0)
        atual = dummy
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                atual.next = list1
                list1 = list1.next
                atual = atual.next
            else:
                atual.next = list2
                list2 = list2.next
                atual = atual.next
        if list1 is None:
            atual.next = list2
        
        elif list2 is None:
            atual.next = list1
        return dummy.next