A queue is a collection of objects, where:

- If we want to take an item, we take it from the front
- If we want to add an item , we add it onto the back

A queue is first-in, first-out (FIFO)

![[image 25.png|image 25.png]]

## Queues in Computer Science

Queues are essential data structures in computing:

- Packets being transmitted across the internet are queued for retransmission at each router
- Input and output buffers are queues - what you type first appears on the screen first
- Path planning algorithms maintain a queue of edges or locations to explore next
- Cloud computing maintains queues of work, queries, updates and access requests

## The Queue ADT

enqueue: add an item to the queue

dequeue: remove and return the item that has been in the queue for the longest time

front: report the item that has been in the queue for the longest time

length: report how many items are in the queue.

## Avoiding Copying Elements

Let’s avoid using list.pop(0)

Instead, maintain our own internal reference to the first element in the list, which we will call the head.

To dequeue, record the element which is referred to by head, reassign None to that cell, update our head pointer to the next index, and return the recorded element.

We need to fix our length method since we can’t just return the length of the list- instead we first subtract head

These operations take constant time, so dequeue is O(1) and we haven’t changed enqueue.

## Exploding the Space

If we do many enqueue and dequeue operations on our queue, we may end up with a very short queue, but with Python maintaining space for a very large list.

(and Python may have created space at the end as part of the dynamic list growth)

### How do we avoid exploding the space?

When we reach the end of the list, instead of letting Python extend it, we will wrap around, and start placing new items at the front.

We only expand the list space when we have filled all cells in our current list.

We must maintain an head and a tail index, and update them carefully when we enqueue and dequeue.

## Complexity of Operations

enqueue and deque are now O(1) ==**on average**==

front and length are always O(1)

Our space requirement is determined by the biggest number of elements ever stored in our queue at any one time (and not by the number of enqueue methods called)