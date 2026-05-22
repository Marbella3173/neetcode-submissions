class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.head.next

        for _ in range(index):
            curr = curr.next
        
        return curr.val

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)

        prevNode = self.head
        nextNode = self.head.next

        newNode.prev = prevNode
        newNode.next = nextNode

        prevNode.next = newNode
        nextNode.prev = newNode
        
        self.size += 1

    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)

        prevNode = self.tail.prev
        nextNode = self.tail

        newNode.prev = prevNode
        newNode.next = nextNode

        prevNode.next = newNode
        nextNode.prev = newNode
        
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return

        if index <= 0:
            self.addAtHead(val)
            return
        
        if index == self.size:
            self.addAtTail(val)
            return
        
        newNode = ListNode(val)

        curr = self.head.next

        for _ in range(index):
            curr = curr.next

        prevNode = curr.prev
        nextNode = curr

        newNode.prev = prevNode
        newNode.next = nextNode

        prevNode.next = newNode
        nextNode.prev = newNode
        
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        curr = self.head.next

        for _ in range(index):
            curr = curr.next

        prevNode = curr.prev
        nextNode = curr.next

        prevNode.next = nextNode
        nextNode.prev = prevNode
        
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)