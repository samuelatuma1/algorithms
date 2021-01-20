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

#Bubble sort
list1 = [3, 7, 5, 1, 8, 2, 1, 23, 9, 17, 2]

def bubble_sort(array):
    for i in range(len(array)-1, 0, -1):
        for j in range(i):
            if array[j] > array[j+1]:
                temp = array[j] 
                array[j] = array[j+1]
                array[j+1] = temp
        
        print('current state of array: ', array)

#bubble_sort(list1)


def mergesort(dataset):
    if len(dataset) > 1:
        mid = len(dataset) // 2
        leftarr = dataset[:mid]
        rightarr = dataset[mid:]

        #recursively break down the array
        mergesort(leftarr)
        mergesort(rightarr)

        #perform the indexing
        i=0 #index into the left array
        j=0 #index into the right array
        k=0 #index into the array we are remerging

        #while both contents have content
        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] < rightarr[j]:
                dataset[k] = leftarr[i]
                i += 1
            else:
                dataset[k] =rightarr[j]
                j += 1
            k += 1

        #IF LEFT ARR still has residual elements
        while i < len(leftarr):
            dataset[k] = leftarr[i]
            i += 1
            k += 1
        
        #IF LEFT ARR still has residual elements
        while j < len(rightarr):
            dataset[k] = rightarr[j]
            j += 1
            k += 1
    
    return dataset

        
#print(mergesort([11, 3, 17, 1, 8, 2, 19, 7, 6, 5]))

#QUICKSORT CODE EXAMPLE
def quick_sort(sequence):
    length = len(sequence)
    #The break point
    if length <= 1:
        return sequence
    
    else:
        #pop out the last item on the list. This will serve as the pivot
        pivot = sequence.pop()
    
    #Create lists partitioning to hold the lower and higher values
    items_lower = []
    items_greater = []

    #Now for every item left in the popped sequence
    for item in sequence:
        #If item is less than the pivot 
        if item < pivot:
            items_lower.append(item)
        
        else:
            items_greater.append(item)

    #Recurse 
    #concatente, keeping the pivot between the lower and greater
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


#print(quick_sort([1,4, 2, 8, 1, 13, 2, 7]))


#Module 5
#SEARCHING DATA

def search_unordered(item, itemslist):
    for i in range(0, len(itemslist)):
        if itemslist[i] == item:
            return f'Search at position {i} '

    
    return None

itemslist = [1,3,2, 5, 8, 11, 4, 17, 8, 8, 21, 2, 23]
item = 8
#print(search_unordered(item, itemslist))



#Search ordered
def binarysearch(item, array):
    #listsize = 

    lowerIdx = 0
    upperIdx = len(array) - 1

    #While there is still at least one value in the list
    while lowerIdx <= upperIdx:
        #find midpoint
        midpoint = (lowerIdx + upperIdx) // 2

        #If item is the middle, return the idx
        if item == array[midpoint]:
            return f'Item at index {midpoint}'

        else:
            #if item in lower part
            if item < array[midpoint]:
                upperIdx = midpoint - 1
            
            # else if item in upper half
            elif item > array[midpoint]:
                lowerIdx = midpoint + 1

    return None
        


array = [1, 2, 3, 4, 6, 8, 9, 11, 20,  26]
item = 11
#print(binarysearch(item, array))


#Determine if a list is osrted

#Using the brute force method
def is_sorted(array):
    for index in range(0, len(array) - 1):
        #Once the first unsorted value is reached, return false
        if array[index] > array[index+1]:
            return False
        else: 
            pass
    
    #At the end of the list, if no False has been reached, return True
    return True


#A pythonic apporach to solving is_sorted
def is_sorted_pythonic(array):
    return all(array[index] <= array[index+1] for index in range(0, len(array) - 1))

#print(is_sorted(array))
#print(is_sorted_pythonic(array))


#Unique identifier
def unique_identifier(array):
    filter = {}
    set_values = set()
    for item in array:
        if item in filter:
            filter[item] += 1
        else: 
            filter[item] = 1

        set_values.add(item)
    
    

    return f'{set_values}, {filter}'

#print(unique_identifier([1, 1, 2, 3, 5, 5, 5, 5, 7]))

def find_max(array):
    if len(array) == 1:
        return array[0]
    else:
        op1 = array[0]
        op2 = find_max(array[1:])
        if op1 > op2:
            return op1
        else:
            return op2
    
print(find_max([1, 1, 2, 3, 5, 5, 5, 5, 7]))