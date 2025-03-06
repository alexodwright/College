## Free Storage of List Elements

Remember that a list is a sequence of references to items, and each item is stored individually by Python

We will store each reference individually - don’t require them to be stored in consecutive memory

Let Python decide where to put them.

But with each reference, also store a reference to the next one in the list, so that we can find it.

![[image 26.png|image 26.png]]

Here there is no space management issues - as long as there is any memory left for Python to use anywhere, we can create a new element object, and a new ‘list node’ object.

But we have to do the work to read the element - we can’t now rely on the efficient list lookup.

```Python
class SLLNode:
    def __init__(self, item, next_node) -> None:
        self.element = item
        self.next = next_node

class SLinkedList:
    def __init__(self) -> None:
        self.first = None
        self.size = 0

def add_first(self, element):
    node = SLLNode(element, self.first)
    self.first = node
    self.size += 1

def get_first(self):
    if self.size == 0:
        return None
    return self.first.element

def remove_first(self):
    if self.size == 0:
        return None
    item = self.first.element
    self.first = self.first.next
    self.size -= 1
    return item

def length(self):
    return self.size
```

Each of the methods have a time complexity of O(1).

## Implementing the Stack ADT

Since the singly-linked list behaves like a Stack, it is easy to implement the Stack ADT using a SLinkedList

Stack methods:

- push()
- pop()
- length()
- top()

SLinkedList methods:

- add_first()
- remove_first()
- length()
- get_first()

An alternative is to implement linked list behaviour directly into a Stack class.

## Testing the LinkedList Implementation

Use all the test methods and other functions we wrote to test or use the previous Stack Implementation.

If we have implemented these test methods properly, then we do not make any reference to the internals of the Stack class, and so all previous methods should still work.

## Implementing the Queue ADT

Queue methods:

- enqueue(item)
- dequeue()
- front()

LinkedList methods:

- ?
- ?
- ?

The Queue requires operations at both ends of the sequence, but the LinkedList only gives us access to the front...

Can we modify the LinkedList implementation?


![[Pasted image 20241028235907.png]]

## Implementing the Queue ADT (2)

Queue methods:
- enqueue(item)
- dequeue()
- front()
LinkedList methods:
- add_last(item)
- remove_first()
- get_first()

Enqueue (i.e. add) at the end of the linked list
Dequeue (i.e. remove) at the front of the linked list.

### Implementing a Queue with a Singly Linked List

```Python
class QueueSLL:
	def __init__(self):  
		self.body = SLinkedList() 
		 
	def enqueue(self, element):  
		self.body.add_last(element)  
		
	def dequeue(self):  
		return self.body.remove_first()  
		
	def first(self):  
		return self.body.get_first()  
		
	def length(self):  
		return self.body.length()
```

All the above operations are O(1)