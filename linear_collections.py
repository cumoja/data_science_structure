'''
Arrays

List
LinkedList
Doubly Linked List

----

Stacks

Queues

Deque
'''

class Node:
    def __init__(self, value:int) -> None:
        self.value = value
        self.next = None
        # self.previous = None #Only in doubly linked list

class List:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def isEmpty(self) -> bool:
        return self.head == None

    def length(self) -> int: #O(1)
        return self.length

    def removeFirst(self): #O(1)
        if self.head == None:
            return None
        else:
            temp = self.head
            self.head = temp.next
            self.length -= 1
            return temp
        
    def removeLastN(self): #O(n)
        if self.head == None:
            return None
        else:
            current = self.head
            temp = current.next 
            while temp != None and temp.next != None:
                current = temp
                temp = temp.next
            self.tail = current
            self.length -= 1
            return temp

    # def removeLast(self) -> Node: #O(1)
    #     last = self.tail
    #     self.tail = self.tail.previous
    #     return last
    def nlength(self) -> int: #O(N)
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.next
        return count


    def append(self, value:int)-> None:
        node = Node(value=value)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            #node.previous = self.tail
            self.tail = node
        self.length += 1

    def insertAtStart(self, value:int)-> None:
        node = Node(value=value)
        node.next = self.head
        self.head = node
        self.length += 1

    def insertAt(self, value:int, position:int):
        if position >= self.length and position < 0:
            print("Out of Bounds")
            return None
        else:
            count = 0
            current = self.head
            while count < position:
                current = current.next
                count += 1
            
            node = Node(value=value)
            node.next = current.next
            # node.previous = current
            # if current.next != None:
            #   current.next.previous = node
            current.next = node 

