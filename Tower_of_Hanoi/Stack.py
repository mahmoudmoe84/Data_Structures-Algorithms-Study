from Node import Node

class Stack:
    def __init__(self, limit = 1000):
        self.top_item = None
        self.size = 0
        self.limit = limit
    
    def is_empty(self):
        return self.size == 0
    
    def has_space(self):
        return self.limit>self.size
    
    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value()
        else:
            print("Nothing to look at stack is empty")
    
    def push(self,value):
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)
            top_item = item
            self.size +=1
        else:
            print("Stack is full")
    
    def pop(self):
        if not self.is_empty():
            item = self.top_item
            self.top_item = item.get_next_node()
            self.size -=1
        else:
            print("stack is empty")
        