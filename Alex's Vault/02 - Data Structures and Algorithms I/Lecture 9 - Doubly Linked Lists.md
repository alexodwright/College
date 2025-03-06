Linked lists are a general data structure - we would like to be able to use them for any sequential storage.

To make the operations easier, we will use dummy ‘head’ and ‘tail’ nodes.

```Python
class DLLNode:
    def __init__(self, item, prevnode, nextnode) -> None:
        self.element = item 
        self.next = nextnode
        self.prev = prevnode

class DLinkedList:

    def __init__(self) -> None:
    
    def add_after(self, item, other):

    def add_first(self, item)
    
    def add_last(self, item)

    def get_first(self):

    def get_last(self):

    def remove_node(self, node):

    def remove_first(self):
    
    def remove_last(self):
```

## Inserting Nodes into a Doubly Linked List

![[image 27.png|image 27.png]]

To swap two _adjacent_ nodes in a doubly linked list.

- Swap the contents of the node
- Swap the pointers of the node.

To swap two _arbitrary_ nodes in a doubly linked list.

==*** ***==