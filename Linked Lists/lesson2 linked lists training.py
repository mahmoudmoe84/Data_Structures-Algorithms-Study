class Node:
    def __init__(self, value , next_node = None):
        self.value = value
        self.next_node = next_node
    
    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.next_node
    
    def set_next_node(self,next_node):
        self.next_node = next_node
    
class LinkedLists:
    def __init__ (self,value=None):
        self.head_node = Node(value)
        
    def get_head_node(self):
        return self.head_node

    
    def insert_begining(self,new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node
        
    def stringfy_list(self):
        string_list=""
        current_node_value = self.get_head_node()
        while current_node_value:
            if current_node_value.get_value() !=None:
                string_list = string_list + str(current_node_value.get_value()) + "\t"
            current_node_value = current_node_value.get_next_node()
        return string_list
        
l1 = LinkedLists(5)
l1.insert_begining(50)
l1.insert_begining(60)
l1.insert_begining(80)


print(l1.stringfy_list())