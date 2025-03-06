
Indexing is a technique to optimise operational time of database queries using data structures

It leads to faster query results.

![[Pasted image 20250116100634.png]]

# How do Indexes Work

Database is loaded into memory by reading files
Files are written to disk across blocks.
Rather than read individual records, we load the block and locate the data we require from there.

Data has to be read from memory or even worse, disk.
This adds latency to the query (loads it). We then have to search the blocks for the values we want.
The more searching we do, the slower the query.

Index help us locate the block where the data is located
Less reading as we only read the blocks where the data is located.
Less searching as we have smaller collection of data to search.

## Index Definition as SQL

We can create an index on an attribute of a relation
- This creates a data structure (e.g. B+ tree) that allow the system to efficiently search for tuples with a particular value for the attribute.
We can create an index using a syntax such as:
```SQL
CREATE INDEX <index_name> ON <relation>(<attributelist>)
```
where the attributes list is the list of attributes that form the search key for the index.

## Creating an Index

We can create an index as follows:
```SQL
CREATE INDEX <index_name> ON <relation>(<attributelist>)
```
For example:
```SQL
CREATE INDEX example ON exampledata('time')
```

This can significantly improve the performance of a query. Taking the same query before we now have:
![[Pasted image 20250116102011.png]]

Now, because the query is searched, only one row need be accessed.

## Indexes

Indexes are arranged as an indexing field (corresponding to a field in the file/table being indexed) and a list of pointers to disk blocks containing records with that field value.

The values are ordered and the file is much smaller than the target file and so is much faster to search.##

The index exists as a file/table entity in the database.

Different kinds of indexes exist:
- A primary index is an index specified on the ordering key field of the table.
- A secondary index which allows us to index on any non-ordering fields of a file where values are either unique or have duplicates.

## File Blocks

A file is organized as a set of records that are mapped onto blocks.

Several records will occupy a block.
In a simple model, we can say that blocks contain only whole records.
This avoids multiple writes for a single record if it is spanning a block.
When a record is deleted, it is marked as deleted and are subsequently overwritten by new records as desired.

## Non-dense Primary Index
![[Pasted image 20250116102350.png]]

