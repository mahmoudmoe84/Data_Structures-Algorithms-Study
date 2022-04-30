# The language of the flowers has a long history and has often been a topic resigned to the domain of dusty books in a thrift bookseller or a library. 
# With Blossom, we want to give people lightning fast access to all of the possible meanings of their favorite flowers.

# In this project, we are going to implement a hash map to relate the names of flowers to their meanings. 
# In order to avoid collisions when our hashing function collides the names of two flowers, we are going to use separate chaining. 
# We will implement the Linked List data structure for each of these separate chains.

from linked_list import Node, LinkedList
from blossom_lib import flower_definitions
class HashMap:
  def __init__(self,size):
    self.array_size = size
    self.array = [LinkedList() for i in range(size)]

  def hash(self,key):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code
  
  def compress(self,hash_code):
    return hash_code % self.array_size
  
  def assgin(self,key,value):
    hash_code = self.hash(key)
    array_index = self.compress(hash_code)
    payload = Node([key,value])
    list_at_array =self.array[array_index] 
    for item in list_at_array:
      if key == item[0]:
        item[1] = value
        return
    list_at_array.insert(payload)
      
  def retrieve(self,key):
    hash_code  = self.hash(key)
    array_index = self.compress(hash_code)
    list_at_index = self.array[array_index]
    for item in list_at_index:
      if key == item[0]:
        return item[1]
      else:
        None
blossom = HashMap(len(flower_definitions))
for element in flower_definitions:
  blossom.assgin(element[0],element[1])

print(blossom.retrieve('daisy'))