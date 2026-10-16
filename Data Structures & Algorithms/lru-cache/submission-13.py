class DoubleLinkedList:
    def __init__(self,val=0,prev=None,next=None,key=-1):
        self.val = val
        self.prev = prev
        self.next = next
        self.key = key

class LRUCache:
    def __init__(self, capacity: int):
        self.dummystart = DoubleLinkedList()
        self.dummyend = DoubleLinkedList()
        self.dummystart.next, self.dummyend.prev = self.dummyend, self.dummystart
        self.absent = DoubleLinkedList(-1)
        self.table = dict()
        self.count = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        adrr = self.table.get(key,self.absent)
        if not adrr == self.absent:
            self.remove(adrr)
            self.add(adrr.key,adrr.val)
        return adrr.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.table:
            self.remove(self.table[key])
            self.count -= 1
        if self.count//self.capacity < 1:
            self.add(key,value)
            self.count += 1
        else :
            self.remove(self.dummystart.next)
            self.add(key,value)
    
    def remove(self,node):
        node_prev,node_next = node.prev,node.next
        if node_next :
            node_prev.next,node_next.prev = node_next,node_prev
        else :
            node_prev.next = None
        self.table.pop(node.key)
    
    def add(self,key,value):
        new = DoubleLinkedList(value,key=key)
        prev,nxt = self.dummyend.prev,self.dummyend
        prev.next = nxt.prev = new
        new.next, new.prev = nxt, prev
        self.table[key] = new

