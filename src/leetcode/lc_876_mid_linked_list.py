from calendar import c
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def append(self, val):
        while self.next:
            self = self.next
        self.next = ListNode(val)

    def print(self):
        while self.next:
            print(self.val, end=", ")
            self = self.next
        print(self.val)


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        middle = head
        current = head
        while current and current.next:
            middle = middle.next
            current = current.next.next
        return middle


if __name__ == "__main__":
    input_list = [1, 2]

    head = ListNode(0)
    for val in input_list:
        head.append(val)
    head.print()
    assert 1 == Solution().middleNode(head).val

    head.append(7)
    head.print()
    assert 2 == Solution().middleNode(head).val

    head.append(8)
    head.print()
    assert 2 == Solution().middleNode(head).val
