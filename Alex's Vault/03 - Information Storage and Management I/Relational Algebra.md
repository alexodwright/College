## Precedence Graphs

Given two or more transactions, we create a node for each transaction and a directed edge to denote that one of the following holds.

- Ti executes write (Q) before Tj executes read (Q)
- Ti executes read (Q) before Tj executes write (Q)
- Ti executes write (Q) before Tj executes write (Q)

## Concurrency

We know that serializable schedules of multiple concurrent transactions are guaranteed consistent.
We also know that it is impractical to retrospectively test a schedule of transactions to see if it was serializable.
The solution lies in finding a protocol that transactions should follow that will guarantee that they only participate in serializable schedules.
Two general-purpose solutions have been proposed, of which one is in common use:
	- Locking (the common approach)
	- Timestamping
We consider locking - in its two-phase locking (2PL) form.

## Concurrency - Locking

- Under this scheme, a transaction should acquire a lock on data object before accessing it, and release that lock afterward.
- Acquiring a lock might be explicitly done, via a user-issued command; alternatively the DBMS could implicitly do it (as usual, the trade will be between flexibility (user) and simplicity (system)).
- Two types of lock are required
	- A shared lock, that may be held by multiple transactions but is useful for readers only.
	- An exclusive lock, that may be held by only one transaction at a time and is useful primarily for writers (though a reader could also hold one).

The DBMS should support an interface for acquiring and releasing locks; it must also support a data structure for recording which extent transactions hold which locks: a lock table; other data structures are also required, such as transaction queues (transactions waiting to acquire locks).

The implementation of the contains implementations for three operations.
- Acquiring a shared lock / an exclusive lock
- Releasing a lock that is held.

Recall that a transaction could have a series of database requests:

```SQL
SELECT: A shared lock would suffice.

UPDATE: An exclusive lock would be required.

Lock updating and downgrading (no commercial DBMS supports this)
```


A transaction T is well-behaved if it adheres to the following conventions, which are easily checked by a syntactic analysis of the transaction's operations:
- A transaction T must issue the operation read_lock(X) or write_lock(X) before any read_item(X) operation is performed in T.
- A transaction T must issue the operation write_lock(X) before any write_item(X) operation is performed in T.
- A transaction T must issue the operation unlock(X) after all read_item(X) and write_item(X) operations are complete in T.
- A transaction T will not issue a read_lock(X) operation if it already holds a read(shared) lock or a write (exclusive) lock on item X.
- A transaction T will not issue a write_lock(X) operation if it already holds a read(shared) or write(exclusive) lock on item X.

