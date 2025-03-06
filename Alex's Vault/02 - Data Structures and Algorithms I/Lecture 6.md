## The Stack

A stack is last-in, first-out (LIFO)

![[image 24.png|image 24.png]]

## Stacks in Computer Science

The stack idea is surprisingly useful in computer science.

- The UNDO option in a text editor or IDE relies on a stack of actions.
- The ‘back’ button in a web browser returns to the page at the top of a stack of previous pages.
- Many languages (including Python) are implemented using a stack of active function calls
- Evaluating arithmetic expressions without the need for brackets (via postfix notation)
- A quick method for reversing a sequence of input characters.

## Postfix

The standard infix notation for arithmetic requires brackets to allow operators to be applied against the precedence order

- e.g. $3+5*2 = 13$﻿, but $(3+5)*2 = 16$﻿

It is called ‘infix’ because the operators are located in between the values or expressions they operate on.

In postfix, the operator comes after the values.

- $3\space5 +$﻿ is interpreted as $(3+5)$﻿, and so = 8
- 3 5 - is interpreted as (3-5), and so = -2
- 5 2 * is interpreted as (5*2), and so = 10

Precedence is entirely based on the sequence of the operators. To apply a standard operator, every operator to the left of it must have been applied already, and then we can apply it to the values immediately to its left.

==*** ***==

## Evaluating Postfix with a Stack

- If you read a number, push it onto the top of the stack
- If you read an operator, pop the top off the stack as the 2nd term, pop the next top off the stack as the 1st term, compute the result, and push it onto the top.

![[image 1 21.png|image 1 21.png]]

## Abstract Data Type

We will want to use stacks in programming, and we want to know that they will behave like a stack.

We need a way to specify to other programmers (and to ourselves) that we are offering a stack.

Other people don’t need to know how it is implemented underneath.

We need a _specification_ of a stack, that everyone agrees on, and then we will guarantee that our object behaves according to the specification.

The specification is an ==Abstract Data Type== (ADT).

## The Stack ADT

- push: add an item to the stack
- pop: remove the item that was added to the stack most recently.
- top: report the item that was added to the stack most recently.
- length: report how many elements are in the stack.

Note: sometimes an “is_empty” method is also specified, but is implemented by ‘length( == 0)’

## Implementing the Stack

We will define a class, offering those methods.

### Complexity of Operations

- List.append() is O(1)
- List.pop() is O(1) (always pop last item)
- List index lookup is O(1)
- List length is O(1)
- List creation is O(1)