from typing import Optional
## 95.23% faster than python3 submission
## 43.23% less mem than python3 submission

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = ""
        b = ""
        d = []
        temp = l1 
        temp2 = l2
        while l1!=None or l2!=None:
            if(l1!=None):
                a = str(l1.val)+a
                l1=l1.next
            if(l2!=None):
                b =str(l2.val)+b
                l2=l2.next
        c = str(int(a)+int(b))
        for i in range(0,len(c)):
            d.append(ListNode(int(c[i])))
            if i>0:
                d[i].next = d[i-1]
        return d[-1]