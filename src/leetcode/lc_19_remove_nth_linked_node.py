from typing import List, Optional


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

    def to_list(self):
        l = []
        while self:
            l.append(self.val)
            self = self.next
        return l

    def __repr__(self):
        return f"{self.val}->{self.next.val if self.next else None}"


# TODO: refine
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nth_node = last_node = head
        while n > 0:
            last_node = last_node.next
            n -= 1
        while last_node and last_node.next:
            nth_node = nth_node.next
            last_node = last_node.next
        if nth_node == head and not last_node:
            head = nth_node.next
        else:
            nth_node.next = nth_node.next.next

        return head


def test1():
    input_list = [1, 2, 3, 4, 5]
    n = 2

    head = ListNode(input_list[0])
    for val in input_list[1:]:
        head.append(val)
    res_head = Solution().removeNthFromEnd(head, n)

    assert [1, 2, 3, 5] == res_head.to_list()


def test2():
    input_list = [1]
    n = 1

    head = ListNode(input_list[0])
    for val in input_list[1:]:
        head.append(val)
    res_head = Solution().removeNthFromEnd(head, n)

    assert res_head is None


def test3():
    input_list = [1, 2]
    n = 2

    head = ListNode(input_list[0])
    for val in input_list[1:]:
        head.append(val)
    res_head = Solution().removeNthFromEnd(head, n)

    assert [2] == res_head.to_list()


def test4():
    input_list = [1, 2]
    n = 1

    head = ListNode(input_list[0])
    for val in input_list[1:]:
        head.append(val)
    res_head = Solution().removeNthFromEnd(head, n)

    assert [1] == res_head.to_list()


if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
