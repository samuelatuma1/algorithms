# Euclid's algorithm
def Euclid_HCF(num1, num2):
    while num2 != 0:
        temporary_num1_holder = num1
        num1 = num2
        num2 = temporary_num1_holder % num2
    return num1

#print(Euclid_HCF(20, 4))
#print(Euclid_HCF(80, 32))


#Big O notation concept

data = [1, 2, 3]
alphabet = ['A', 'B', 'C']

def constant_time_Big_O(data):
    last_data = data[len(data) - 1]
    return f' This is a constant time because output, {last_data} \n takes the same amount of time to execute irrespective of the input'

#print(constant_time_Big_O(data))

def linear_Big_O(data):
    big_o = 0
    for datum in data:
        big_o += 1
        print(datum)
    return f' Big o is linear here because {data} is executed \n {big_o} times which is equal to the number of inputs'

#print(linear_Big_O(data))   

def quadratic_Big_O(data, alphabet):
    bigo=len(data)
    total = 0
    for datum in data:
        for alpha in alphabet:

            total += 1
            print(datum, alpha)
    
    bigo2 = (total / bigo)
    return f"Big_O is {bigo * bigo2} which is ({bigo} * {bigo2}) i.e it is quadratic"
            

#print(quadratic_Big_O(data, alphabet))


#Linked List walk through

#The particular node class i.e the particular item
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


    def get_data(self):
        return self.val

    def set_data(self, val):
        self.val = val
    
    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

# The List class as a whole (The linkedlist class)
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.count = 0

    def get_count(self):
        return self.count
    
    #Add a node to the list
    def insert(self, data):
        #insert a new node at the head
        new_node = Node(data)
        
        #set the current head to be the next value after the new node
        new_node.set_next(self.head)
        #set node as the new head of the linked list
        self.head = new_node
        #Increase list count by 1
        self.count += 1
        

    def find(self, val):
        #find the first item with a given value
        item = self.head
        while item is not None:
            if item.get_data() == val:
                return item
            else:
                item = item.get_next()
            
        return None

    def deleteAt(self, idx):
        #delete an item given the index
        if idx > self.count - 1:
            return
        #If head, just set the next head as the new head
        if idx == 0:
            self.head = self.head.get_next()
        else:
            tempidx = 0
            node = self.head

            #Go to the linkednode just before the one we want to delete
            #Done by looping through the linked list in this funny fashion
            while tempidx < idx - 1:
                node = node.get_next()
                tempidx += 1
            
            #Now, point the previous node to the node after the node we want to delete
            node.set_next(node.get_next().get_next())
            self.count -= 1
            


    def dump_list(self):
        #start at the head and print each value following
        temporary_node = self.head

        while temporary_node is not None:
            print(f'Node value: {temporary_node.get_data()}')
            temporary_node = temporary_node .get_next()


#Create a linked list and insert some items
itemList = LinkedList()
itemList.insert(24)
itemList.insert(31)
itemList.insert(50)
itemList.insert(18)
#itemList.dump_list()
#Print out the list
#itemList.deleteAt(3)
#print("Item count: ", itemList.get_count())
#print('finding item: ', itemList.find(24))
#print('finding item: ', itemList.find(60))


# Stacks and queues example
#Stacks are best described by the acronym LIFO (Last in First out)
#That is, the last item to e added is the first to be popped out
stack = []
#stack items to a stack list
stack.append(5)
stack.append(4)
stack.append(7)
stack.append(8)

# remove the last added item from the list
#print('popped', stack.pop())
#print('new_stack', stack)


#Queues follow the name queues. First added is first popped
#Using list to represent queues will result in a linear time
#A more efficient way (constant time) will be to use deque similar to a list
from collections import deque

queue = deque()
queue.append(1)
queue.append(7)
queue.append(6)
queue.append(8)

#print(queue)

#pop the first item out
#print('popped', queue.popleft())
#print('new_queue', queue)


#Hash tables
#Hash tables are dictionaries
item1 = dict({'key1': 1, 'key2': 2, 'key3': 3})

#for item, val in item1.items():
#   print('item', item, 'val,', val)


#Recursion example
import time
import math
def recursion(number):
    #The breaking point
    
    if number <= 0:
        time.sleep((math.pi)/14)

        print('Done!')
        return 

    #The recursive point
    else:
        time.sleep(0.33)

        print(number)
        recursion(number - 1)
    print(f'Rewinding {number}')

#recursion(10)

#Reverse string example using recursion
def names(your_name, reverse_name=''):
    
    if len(your_name) == 0:
        return
    
    else:
        reverse_name += your_name[-1]
        your_name = your_name[:-1]
        print(reverse_name)
        names(your_name, reverse_name)

#names('Chidiebere Clington Okpara Saake Atuma Chidiebere Clington Okpara Saake Atuma Chidiebere Clington')

def reverse_string(string, count=0):
    if len(string) == count:
        return 

    else:
        print(string[-1 - count])
        reverse_string(string, count + 1)

#reverse_string('Atuma Chidiebere Clington Okpara Saake Atuma Chidiebere Clington Okpara Saake Atuma Chidiebere Clington')

def power(num, pwr):
    if pwr == 0:
        return 1
    
    else: 
        return num * power(num, pwr-1)

#print(power(2, 4))

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

#print(factorial(4))

#SOrting algorithms



