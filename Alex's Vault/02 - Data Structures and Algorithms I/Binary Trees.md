## Trees

A **tree** is a connected undirected simple graph with no cycles.

![[Pasted image 20241030140758.png]]

### Rooted Trees

Usually, when we think of trees, we assume there is a root.

A **rooted tree** is a tree in which one of the vertices is designated the **root**, and all edges are then directed away from that root.

![[Pasted image 20241030140856.png]]

### Describing Vertices in Rooted Trees

If there is a directed edge from x to y, then x is the **parent** of y, and y is a **child** of x.

If two vertices y and w have the same parent, they are **siblings** of each other.

A vertex with no children is a **leaf**. A vertex with children is an **internal** vertex.

The **ancestors** of a vertex v are all the vertices in the path from v to the root.

==*** ***==

## Binary Trees

A *Binary Tree* is a rooted tree in which:
- Every node has at most 2 children
- The children of a node are identified as left child and right child.

The depth of a tree is the length of the longest path from the root node to a leaf node.

![[Pasted image 20241030141110.png]]

Depth == 3
## Implementing Binary Trees

### Binary Tree Node

```Python
class Node:

	def __init__(self, item):
		self.left = None
		self.right = None
		self.element = item
```

![[Pasted image 20241030141724.png]]

When numbering a binary tree according to a Breadth-First approach you can get the left child's index with the formula $left = i\times2 + 1$ and to get the right you can use: $left = i\times2 + 2$ where $i$ is the current node's index.

You can use the same method in reverse to get the parent of any child node.

### Computing the height of a node.

The height of a node is the length of its longest (directed) path to a leaf.

**Recursive definition**:
- height(node) = 0 if node is a leaf
- height(node) = 1 + max(height(left), height(right))

```Python
def height(self):
	if (self.right is None) and (self.left is None):
		return 0
	elif self.left is None:
		return 1 + height(self.right)
	elif self.right is None:
		return 1 + height(self.left)
	return 1 + max(height(self.left), height(self.right))
```

## Preorder Traversal

To visit a node, read the element first, then visit the children in left-to-right order.

![[pre-order-traversal.gif]]

'Preorder' because we do the parent's element before the children

```Python
def preorder_print(node):
	if node:
		print(node.element)
		preorder_print(node.left)
		preorder_print(node.right)
```

Alternative version:

```Python
def preorder_str(node):
	if node:
		outstr = str(node.element)
		outstr += preorder_str(node.left)
		outstr += preorder_str(node.right)
		return outstr
	else
		return ''
```

## Inorder Traversal

To visit a node, visit the left child, then the parent's element, then the right child.

![[in-order-traversal.gif]]

```Python
def in_order_traversal(node):
	if node:
		in_order_traversal(node.left)
		print(node.element)
		in_order_traversal(node.right)
```

## Post-Order Traversal

![[post-order-traversal.gif]]

```Python
def postOrderTraversal(node):
  if node is not None:
	print(node.element)
    postOrderTraversal(node.left);
    postOrderTraversal(node.right);
```

## Evaluating Expression Trees

### An expression tree:

![[Pasted image 20241030145407.png]]

Evaluate node:
- If the node element is a number return it
- Else
	- Evaluate the left child
	- Evaluate the right child
	- Determine the operator in the node
	- Apply 'left (operator) right'