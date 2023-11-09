class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class singly_linked_list:
    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0
    def append_item(self,data):
        node=Node(data)
        if self.head:
            self.head.next=node
            self.head=node
        else:
            self.head=node
            self.tail=node
        self.count +=1
    def iterate_item(self):
        current_item=self.tail
        while current_item:
            val=current_item.data
            current_item=current_item.next
            yield val 
items=singly_linked_list()
items.append_item("PHP") 
items.append_item("Python")                  
items.append_item("Java")                  
items.append_item("C#")                  
items.append_item("C++")                  
items.append_item("C")
for val in items.iterate_item():
    print(val)

print("oringinal List:")
print("\nSize of the List:",items.count)