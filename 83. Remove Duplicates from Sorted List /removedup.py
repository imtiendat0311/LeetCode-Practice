# faster than 80.88% other online python3 submisison
# use less mem than 30% other online python3 submission
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        a = []
        b = []
        i = 0
        while head is not None:
            if a.count(head.val)==0:
                a.append(head.val)
                b.append(ListNode(head.val))
                if i > 0:
                    b[i-1].next=b[i]
                i=i+1
            head = head.next
        return b[0]