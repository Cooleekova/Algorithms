#linked list is a data structure consisting of a collection of nodes which together represent a sequence.
#Elements order in linked list is not given by their physical placement in memory. 
#Instead, each element points to the next.


# 1. A simple demonstartion of how elements work in linked list.


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
print("list_a: ")
print(linked_list_value)
while linked_list_value.next:
    linked_list_value = linked_list_value.next
    print(linked_list_value)


# 2. A more complex demonstration of linked list idea.
# inspired by: https://builtin.com/data-science/python-linked-list
# how to add list indexes: 
# https://stackoverflow.com/questions/22284578/linked-list-in-python-append-index-insert-and-pop-functions-not-sure-with-c


class Knot:
    """Class for linked list data elements"""

    def __init__(self, value):
        """Each node in linked list contains a value and pointers to the next and previous values.
        If the list contains only one node, its pointers are equal to None"""
        self.value = value
        self.next = None
        self.previous = None

    def __str__(self):
        return str(self.value)
    
    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


class LinkedList:
    """Linked list which contains data elements"""

    def __init__(self, head=None, end=None):
        """A list has its first and last elements, 
        other elements are in between them"""
        self.head = head
        self.end = end
        self.count = 0


    def insert_to_head(self, value):
        """
        Create a new element at the Head of the Linked List
        """ 

        #create a new element to hold the data
        new_element = Knot(value)
        
        #set the next of the new element to the current head
        new_element.next = self.head

        #set the head of the Linked List to the new element
        self.head = new_element

        # if there is only one element in the list,
        # it also will be the last element
        if self.end is None:
            self.end = new_element

        #add 1 to the count
        self.count += 1


    def insert_to_end(self, value):
        """
        Create a new element at the End of the Linked List
        """ 

        #create a new element to hold the data
        new_element = Knot(value)
        
        #set the next pointer of the previous element to the new element
        self.end.next = new_element
        
        #set the previous pointer of the new element to the current end
        new_element.previous = self.end
       
        #set the end of the Linked List to the new element
        self.end = new_element
        
        #add 1 to the count
        self.count += 1


    def remove(self, item):
        """
        Remove Node with value equal to item

        Time complexity is O(n) as in the worst case we have to 
        iterate over the whole linked list
        """

        #set the current node starting with the head
        current = self.head
        #create a previous node to hold the one before
        #the node we want to remove
        previous = None

        #while current is note None then we can search for it
        while current is not None:

            #if current equals to item then we can break
            if current.value == item:
                break

            #otherwise we set previous to current and 
            #current to the next item in list
            previous = current
            current = current.get_next()

        #if the current is None then item, not in the list
        if current is None:
            raise ValueError(f"{item} is not in the list")
        #if previous None then the item is at the head
        if previous is None:
            self.head = current.next
            self.count -= 1

        #if the element has no next pointer, then the item is at the end
        elif current.next is None:
            previous.set_next(current.next)
            self.end = current.previous
            self.count -= 1


        #otherwise then we remove that node from the list
        else:
             previous.set_next(current.get_next())
             self.count -= 1



        
    def find_value(self, value):
        """
        Search for item in Linked List with data = val
        
        Time complexity is O(n) as in worst case scenario
        have to iterate over whole Linked List
        """

        #start with the first item in the Linked List
        item = self.head

        #then iterate over the next nodes
        #but if item = None then end search
        while item != None:
           #if the data in item matched val
           #then return item
           if item.value == value:
               return f"Yes, {item} is in the list!"
           
           #otherwise we get the next item in the list
           else:
                item = item.next
        #if while loop breaks with None then nothing found
        #so we return None
        return f"{value} is not in the list"


# create a list object
ll = LinkedList()
# insert some values into the list
ll.insert_to_head(1)
ll.insert_to_head(0)
ll.insert_to_end(3)
ll.insert_to_end(5)
ll.insert_to_end(9)
# check how many values are in the list
print("list_ll: ")
print("Total of elements :", ll.count)
# try to remove value
ll.remove(9)
# check the list length once again
#print("After deleting: ", ll.count)
# find first and last elements - complexity O(1)
print("Head ", ll.head,",", "End ", ll.end)
# try to find value in the list - complexity O(n)
print(ll.find_value(3))
# try to find value that is not in the list
print(ll.find_value(1000))
