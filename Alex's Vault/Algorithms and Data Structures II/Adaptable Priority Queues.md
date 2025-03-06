In practice, the priority of patients will change, as their illnesses improve or deteriorate. Some patients may leave the waiting list.

We need to enable:
- Reading the current key of an item
- Updating the key of an item.
- Removing an item
For all items at an arbitrary position in the PQ.
With a reasonable time-complexity.

The Priority Queue ADT doesn't give us the flexibility we need:
- Only gives access to the item with the minimum key.
- No way to change the key of an item.
- If we could change the key, or remove an item, some of our implementations of the PQ would then be inconsistent.
	- E.g. the heap property might be violated.

We need a new Adaptable Priority Queue ADT.

## Adaptable Priority Queue ADT




