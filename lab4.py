'''
MyLinkedList class keeps track of three things:

int size
MyLinkedListNode first
MyLinkedListNode last

MyLinkedListNode has:

String val,
MyLinkedListNode next,
MyLinkedListNode prev.
'''

class MyLinkedList():
    class MyLinkedListNode():
        def __init__(self,val:str) -> None:
            self.val = val
            self.next = None
            self.prev = None
    def __init__(self) -> None:
        self.size = 0
        self.first = None
        self.last = None