class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class linked_list:
    def __init__(self):
        self.head = node()
    
    def append(self, data):
        new_node = node(data)
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node
    
    def length(self):
        curr = self.head
        total = 0
        while curr.next != None:
            total += 1
            curr = curr.next
        return total
    
    def display(self):
        elems = []
        curr_node = self.head
        while curr_node.next != None:
            curr_node = curr_node.next
            elems.append(curr_node.data)
        print(elems)
    
    def get(self, index):
        if index > self.length():
            print("ERROR: 'Get' Index out of range")
            return
        curr_node = self.head
        count = 0
        while True:
            curr_node = curr_node.next
            if count == index:
                return curr_node.data
            count += 1
    
    def remove(self, index):
        if index >= self.length():
            print("ERROR: 'Remove' Index is out of range")
            return
        curr_indx = 0
        curr_node = self.head
        while True:
            last_node = curr_node
            curr_node = curr_node.next
            if index == curr_indxindx:
                last_node.next = curr_node.next
                return
            index += 1


my_list = linked_list()
my_list.display()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
my_list.display()
my_list.remove(3)
my_list.display()