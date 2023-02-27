#linked list is a data structure consisting of a collection of nodes which together represent a sequence.
#Elements order in linked list is not given by their physical placement in memory. 
#Instead, each element points to the next.


# A simple demonstartion of how elements work in linked list.


class Node:
    """Class for linked list elements"""

    def __init__(self, value):
        """Each node in linked list contains a value and a pointer to the next value.
        If the list contains only one node, its pointer is equal to None"""
        self.value = value
        self.next = None
    
    def __str__(self):
        """__str__ method creates human-readable string representation of the class object"""
        return str(self.value)

    def append_to_tail(self, value):
        """append_to_tail method creates new Node object in the end of the linked list
        and puts a pointer in the previous object"""
        last_element = Node(value)
        # by default pointer is being created in the first node of the list
        # but if the first node already has a pointer, 
        # method searches the very last element of the list which has no pointer, 
        # assigns pointer and saves new element right after it
        pointer = self
        while (pointer.next):
            pointer = pointer.next
        pointer.next = last_element


# list_a is the first object of Node class
list_a = Node(10)
# other nodes are being created by the append_to_tail method
list_a.append_to_tail(20)
list_a.append_to_tail(30)
list_a.append_to_tail(40)

# a piece of code which shows all the elements in linked list
linked_list_value = list_a
print(linked_list_value)
while linked_list_value.next:
    linked_list_value = linked_list_value.next
    print(linked_list_value)
