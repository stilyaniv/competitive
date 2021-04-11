class Node:    
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class MyCircularQueue:

    def __init__(self, k: int):
        self._size = k
        self._length = 0
        self._front = None
        self._rear = None
        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        node = Node(value)
        if self._rear:   
            self._rear.next = node
        else:
            self._front = node
            
        self._rear = node
            
        self._length += 1       
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        if self._front.next:
            self._front = self._front.next
        else:
            self._front = None
            self._rear = None
        
        self._length -= 1
        return True
        
    def Front(self) -> int:
        if not self._front:
            return -1
        return self._front.value

    def Rear(self) -> int:
        if not self._rear:
            return -1
        return self._rear.value
        
    def isEmpty(self) -> bool:
        return self._length == 0
        
    def isFull(self) -> bool:
        return self._size == self._length
        

#TODO refactor into tests
# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()