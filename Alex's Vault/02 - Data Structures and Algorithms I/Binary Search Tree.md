
## Ordered Map ADT

```Python

getitem(key) # return key's stored value, or None if key is not there

setitem(key, value) # assign value to element with key

```

==*** ***==

## Could just use a sorted list for the map.

The items sorted in ascending order of the key

getitem(k): binary search to find key k; return Element

setitem(k, v): binary search to find key k; change the value, or insert Element(k, v) in the right place if k is not found.

delitem(k): binary search to find key k; pop the Element from that cell.

first(): return Element in cell 0
last(): return Element in last cell
sortedkeys(): return a copy of the list


|             | geitem(k) | setitem(k, v) | delitem(k) | first() | last() | sortedlist() | build map |
| ----------- | --------- | ------------- | ---------- | ------- | ------ | ------------ | --------- |
| sorted list | O(log n)  | O(n)          | O(n)       | O(1)    | O(1)   | O(n)         | O($n^2$)  |

## Let's look at linked vs array-based lists again...

==*** Insert table here ***==

## Sequence of cell lookups in binary search

A sorted list:

==*** Insert Image Here ***==

## Binary Search Tree

![[Pasted image 20241106142249.png]]

A binary search tree is a binary tree representing an ordered sequence of elements, where:

- All left descendants of a node have values less than the node's value
- All right descendants of a node have values greater than the node's value.
- 
Note: The arrows represent the tree structure, not the order of the elements in the sequence.

### How to perform a traversal

Inorder traversal, first do the left child then the node, then the right child.

### Searching a Binary Tree

Input: A reference to the root node of the tree; a target to search for

Goal: If the target we are searching for is in the tree, return the node that has it as its element; else return None;

- All left descendants of a node have values less than the node's value
- All right descendants of a node have values greater than the node's value

```Python
def search(node, item):
	if node == None
		return None
	if node.element > item:
		return search(node.left, item)
	elif node.element < item:
		return search(node.right, item)
	else:
		return node
```

If h is the height of the root, then this is O(h).

## Adding a node to a BST

Requirement: maintain the order property.
Aim: minimize the work.

When asked to add, if we allow only one copy of each element, then:
1. First we need to check that the element is not already there
2. Then we need to add it.

We know the value we want to add: x
We know the location of the root node

If a node is not in the tree, then the search ends when we reach a null value.

Solution: add the element there, and don't change anything else in the tree.

```Python
def add(node, x):
	if x < node.element
		if node.left is None:
			node.left = Node(x, None, None)
		else:
			add(node.left, x)
	elif x > node.element:
			if node.right is None:
			node.right = Node(x, None, None)
		else:
			add(node.right, x)
```

For a given BST, for each possible addition, if we are restricted to simply adding the new element in an empty place, then there is only one possible location in the tree.

It is O(h) to add an item, since we add the item after the search.

## Removing a node from a BST

We know the value we want to remove: x
We know the location of the root node.

Requirement: maintain the BST property
Aim: minimize the work

Start by finding the node in the tree (and if it is not there, stop)

Handle the removal by breaking it down into different cases.

For this, we will need the links back from a node to its parent.

Cases:
- If it is a leaf node
- If the node has 1 child
- If the node has 2 children

==*** ***==

## Removing an internal node from a BST

We are going to have to do some work - deleting, or moving one child up, might cut off one or more existing children, or break the order.

We will have to pick one of then items below our node, and then rearrange the sub-tree to maintain the order.

Which choice requires the least work?
Can we avoid making the tree deeper?

1. We will always pick the biggest element less than our current node
2. We will move that element straight into our current node.
3. Then remove the node we took the element from
4. Return the original element.

## Removing a node from a BST: complexity

To find the node is O(height of tree)
- Worst case when it is a leaf on the longest branch.

To remove a node is O(height of tree)

== *** *** ==

Note:
Implementing node removal in a BST is tricky.
Maintaining the parent references makes it easier to keep track of where you are in the tree, and of which nodes need to be updated.
But there are now more references to update, and more special cases to handle.

## Is minimising the work the right thing to do?

Our method for adding and removing nodes in BST focused on doing as little work as possible (while maintaining the BST properties)

But if this increases the height of the tree, this might be storing up trouble, and creating more work to do when searching the tree (and so also for adding and removing).

A binary tree of depth d can hold up to $2^0 + 2^1 + 2^2 + 2^3 + 2^d = 2^{d+1}-1$ or n items can be stored in a binary tree of depth = log(n)

### The promise of BST

If h is the height of the root:
- searching, adding and removing is O(h)

Height of the root is 'depth' of the tree. N items can be stored in a binary tree of depth log(n).

Binary search trees support search and updates with complexity O(log(n)).