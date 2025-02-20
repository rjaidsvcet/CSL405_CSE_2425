class Node:
    def __init__(self, value) -> None:
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insertionToFront (self, data):
        newNode = Node (data)
        newNode.next = self.head
        self.head = newNode

    def insertion (self, data):
        newNode = Node (data)
        if not self.head:
            self.head = newNode
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode

    def traversal (self):
        current = self.head
        while current:
            print (current.data, end = ' -> ')
            current = current.next
        print ('None')
    
    def recursiveTraversal (self, current):
        print (current.data, end = ' -> ')
        if current.next == None:
            print ('None')
            return
        self.recursiveTraversal (current.next)

    def search (self, target) -> bool:
        current = self.head
        while current:
            if current.data == target:
                return True
            current = current.next
        return False
    
    def deletion (self, element):
        if not self.head:
            return
        
        if self.head == element:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next:
            if current.next.data == element:
                current.next = current.next.next
                return
            current = current.next

if __name__ == '__main__':
    ll = LinkedList ()
    ll.insertion (1)
    ll.insertion (2)
    ll.insertion (3)
    # ll.traversal ()
    ll.recursiveTraversal (ll.head)
    output = ll.search (4)
    print (f'The element to be searched : {output}')
    ll.deletion (2)
    ll.recursiveTraversal (ll.head)
