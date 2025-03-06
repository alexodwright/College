## Database Management Systems

Database Management Systems (DBMS) are used to organize large quantities of information by providing systems for storing, managing and retrieval of the information.

DBMS seek to store data securely and safely. They are robust to errors by supporting data integrity and avoiding anomalous states.  
They also provide services such as security, and user authorization.  

## History of DBMS

![[image 20.png|image 20.png]]

## DBMS and the Software Industry

Data forms a key component of most applications.  
From telecoms to banking to manufacturing to social media, data bases form a key component of innumerable services, servers and applications.  

Typically, databases form the foundation of many software architectures.

![[image 1 17.png|image 1 17.png]]

## Databases

A database is a collection of data.

A database is hosted on a DBMS

The design of a database is called its schema and is made up of a set of inter-related relations.

## Relations and Keys

Each tuple within a relation must be uniquely identified - no two tuples should have the same ID.

A super key is one or more attributes that collectively identify a tuple.

There can be numerous candidate keys, but when we design the relation ,we choose one. This is known as the primary key.

## Queries

Queries are used to query information in one or more relations in a database.

Declarative languages describe the information we wish to retrieve.

When we write a simple SQL query, we focus on what we wish to retrieve rather than how it should be retrieved.