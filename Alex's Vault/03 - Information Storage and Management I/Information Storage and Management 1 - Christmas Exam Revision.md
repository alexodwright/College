Key features provided by databases:
- Data storage, retrieval and update
- Provide a user-accessible catalog - this allows users of the DB to examine descriptions of the DB's structure and organisation.
- Transaction support - ensure that all modifications of data are applied or none at all.
- Concurrency support - ensure that multiple users can interact with the data and that the state of the data remains consistent.
- Recovery services - a DBMS should be able to recover to at least a recent version if it is corrupted.
- Authorization control.
- Support for data communications - external applications should be able to interact with data.

Database Management Systems (DBMS) are used to organize large quantities of information by providing systems for storing, managing and retrieval of the information.
They seek to store data securely and safely. They are robust to errors by supporting data integrity and avoiding anomalous states.
They also provide services such as security, and user authorization.

A database is a collection of data and is hosted on a DBMS. It's design is called its schema and is made up of a set of inter-related relations.

A superkey is one or more attributes that collectively identify a tuple.
The primary key is the candidate key we choose when we design the relation.

We can connect to a DBMS using several techniques.
- Programmatically - using a programming language such as Python
- Through the command line interface (CLI) executed in a terminal or command line interface.
- Through a graphical user interface such as MySQL Workbench and other software.

## Create Table

```SQLite
CREATE TABLE `employee` (  
`id` int(4),  
`name` varchar(200),  
`dept` varchar(50),  
`salary` double,  
PRIMARY KEY (`id`)  
);
```

## Insert into Table

```SQLite
INSERT INTO `employee` (`id`, `name`, `dept`, `salary`)  
VALUES  
('1002','Laura','HR','40000'),  
('1003','Cathal','IT','55000'),  
('1004','Ann','HR','50000'),  
('1005','Mary','IT','45000'),  
('1006','Phil','Sales','50000'),  
('1007','Peter','Sales','60000');
```

## Update Table

```SQLite
UPDATE employee  
SET salary = salary * 1.05  
WHERE salary < 50000
```

# DMBS with Python

## Connection

```Python
import pymysql.cursors

connection = pymysql.connect(host='cs1.ucc.ie’,  
				user='your_user’,  
				password='your_password’,  
				database='your_database’,  
				cursorclass=pymysql.cursors.DictCursor)
```

## Executing Queries

```Python
with connection:  
	with connection.cursor() as cursor:  
	# Create a new record  
		sql = "INSERT INTO `employee` (`id`, `name`, `dept`, `salary`) VALUES (%s, %s, %s, %s)”  
		cursor.execute(sql, (1008, 'Bill', 'IT', 60000)  
	# connection is not autocommit by default  
	connection.commit()


# or if executing a select query:
		sql = "SELECT `id`, `name`, `dept`, `salary` FROM `employee` WHERE `name`=%s”  
		cursor.execute(sql, ('Bill’,))  
		result = cursor.fetchone()  
		print(result)
```

# Steps in Implementing a DBMS

Database Planning: Overarching view of data management and governance within an organization, the 'mission statement' for data storage.

System Definition: Description of the scope and boundaries of what information will be stored on the DB, and a high level description of the uses of this information.

Requirements Gathering: The process of collecting and analysing information (fact-finding) and integrating these views (facts from user's perspective) to form a description of requirements.

Database Design - Conceptual: High level design that is independent of all implementation details. Determine database type, identify entities that must be represented, general relationships between these attributes and their domains, keys, etc.

Database Design - Logical: Design with reference to the relational model. For example, normalize the schema, validate user transactions against schema, addition of integrity constraints, etc.

Database Design - Physical: Design with reference to the chosen DBMS by translating logical schema into one compatible with the features available.

Database Prototyping: Sometimes useful activity in which the schema is coarsely implemented to give insights into the overall plan. Can also be used to garner more feedback from the users.

DBMS Selection: Selection of a DBMS that is suitable for managing the proposed database.

Application Design: An aside. Consultation with others in charge of the software architecture about how best to integrate with the database 
system.

Implementation: Installation of DBMS, creation of schema and associated features.

Data Conversion/Loading: Transfer any existing information into the database. This may be a manual process if paper records exist of may involve transforming existing database's data.

Testing: The process of using the database with existing processes and systems. This may result in iteration over implementation.

Operation Maintenance: Monitoring the operational database to allow optimisation. May yield new requirements.

## Fact Finding

Fact finding is a process using a range of techniques to collect facts about systems, requirements and preferences.

It occurs primarily at the start of a project, through it is also used during prototyping and iteration during the operational phase.

It can include:
- Examining Documentation
- Interviews
- Questionnaires
- Observation of operations and processes
- Research

Interview Advantages/Disadvantages:

Advantages:
- Free flow of information from employees (even through body language etc)
- Buy in through involvement
- Ability to follow up
- Allows refinement of interview questions
- Discovery of new information sources.

Disadvantages:
- Expensive: time consuming and effort intensive.
- Interviews are an acquired skill. Often more is garnered from later interviews when compared with earlier ones.
- Requires buy in of participants: be aware, new technologies can meet resistance if it is felt they can threaten employee roles.

Observation Advantages/Disadvantages:

Advantages:
- Used to verify and refine data collected through other techniques.
- Can observe actual methodologies used - this can reveal nuance not disclosed during other techniques.
- Can observe friction points in the process.
- Can observe the physical setting of tasks and external stresses not detected from other techniques.
- Relatively inexpensive.

Disadvantages:
- Observation can affect how users behave.
- Will capture typical tasks but unusual circumstances may not arise.
- Need to observe several uses - observing one might not capture typical usage.
- Considerations such as presence of customers may make conduct of observation difficult.

Research Advantages/Disadvantages:

Advantages:
- Saves time and effort if a similar solution exists.
- Even if solution isn't suitable, learning of skills, technologies, etc will save effort.
- Transferrable knowledge learned for one project may save effort in other projects.

Disadvantages:
- Must have access to information sources and be capable of using research outputs.
- Will work in general terms. Will still need to understand how to use outputs for specific tasks.

Questionnaire Advantages/Disadvantages

Advantages:
- Can be completed at user's convenience
- Inexpensive and scalable
- Likely to elicit honest answers as questionnaire can be conducted confidentially.
- Analysis can be quick and repeated to answer subsequent observations.

Disadvantages:
- User motivation and participation can be low.
- Incomplete answers.
- Requires careful design to avoid misinterpretation. Worth prototyping where possible.
- Care needed to balance questions types - closed can be limiting as remove flexibility when answering, while open can lead to difficult analysis.

# DBMS Architecture

The top most layer consists of typical server features such as authentication, connection handling, threading and security.
These facilitate network client/server tools such as Workbench.
Each user sessions creates a new thread through which their queries are executed.

The next layer consists of modules that parse queries, optimise their execution. This layer also manages query catching. The output of the process is a series of calls to particular storage engines.
Essentially functionality that is common to all storage engines is represented here whereas storage engines focus on managing data of particular formats or in particular ways.

The third and final layer contains the storage engines. These are responsible for storing and retrieving data 'in the database'.
Different engines are optimised for different purposes and data formats.
The core MySQL service works with storage engines via a storage API.
This common interface means that storage engines can be plugged into the DBMS architecture.
Therefore, interactions with storage engines are via API calls - they never directly execute SQL.
The output of the optimiser is a series of API calls to the storage engine.

## Query Parsing

The query parser creates a parse tree to identify parts of the query.
Ultimately, this is expressed as a series of API calls to various storage engines.
Returned data is marshalled into a result relation.

## Query Optimisation

Before a query is executed, it is optimised.
This can include rewriting the query parse tree to optimise table read order, or determining which where clauses to apply first.
The optimiser also queries storage engines to determine their capabilities. For instance, some engines will support indexing and the availability of such features will determine how optimisation is done.

## Query Caching

Before parsing or optimisation takes place, the cache is examined to determine if a select statement (only select statements are cached) and its result set has already been executed.
If the query was already executed, and if the table remains unchanged, then the result set is returned with no further action (parsing or optimising) taking place.

## Storage Engines

Storage engines are dedicated software modules that implement a standard API to allow core MySQL to interact with the engine.
Each engine is optimised for particular data types and formats.
Ultimately all data in a database is stored in files on the filesystem.
Different file extensions are used to denote different types of data.
Both core MySQL and storage engines follow this pattern.

We can inspect information about a table in a number of ways.
- 'Describe course' will describe the attributes and their domains.
- 'Show table status' will reveal information useful for optimisation. For example, the engine that is used to store the table.

### Optimization through engine selection

When designing a highly optimised database, we should include storage engine selection as part of our design.
Each table can be assigned a storage engine.

We have to consider the table's data, rate of growth, need to support transactions, need or concurrency etc, when carrying out our physical design phase.

# ER (Entity Relationship) Models

ER Diagrams take a top down approach to identify entities and their relationships. Further details such as entity attributes and constraints can be added.

## Entity Type and Occurrence

An entity type is a group of objects in the real world that have the same properties. Entities can be physical or conceptual. Entities are identified by a name and a list of properties.

An entity occurrence is an identifiable instance of an entity.

## Relationship Type and Occurrence

A relationship type is a set of associations between entities.

A relationship occurrence is a uniquely identifiable association that includes one occurrence from each entity type in the relationship.

## Attributes

Entities have properties, which are known as attributes.

Relationships can also have attributes.

Attributes can have a domain though we usually don't add these until physical design.
- Attribute domain is the set if allowable values for an attribute
- Not quite a type - we can also limit to certain ranges of values.

## Primary Keys

Attributes for any one entity should include a key attribute
- Primary Key - the attribute that is used to uniquely identify an entity instance.
- We mark a primary key by adding (pk) after the attribute name.

## UML (Unified Modelling Language)

UML is a standard set of notations, shapes and symbols for modelling software solutions, application architectures, system behaviours and more.

## Multiplicity

Multiplicity is the number of occurrences of an entity type that may relate to an associated entity type.

![[Pasted image 20241206172400.png]]

This can be described from either end of the relationship
- 'A staff member is associated with a branch' - one staff member to one branch - 1..1
- 'A branch has one to several staff members' - one branch can have as few as one and up to many staff - 1..*

## Strong and Weak Entities

- A weak entity is an entity whose existence is dependent on some other entity type.
- A strong entity is an entity whose existence doesn't depend on some other entity type.

e.g. If we have a database representing a Bank, then Bank Branches can be considered to be weak as they cannot exist without a Bank existing.

## Multiplicity in Detail

Multiplicity is made up of two parts, cardinality and participation.

![[Pasted image 20241206172722.png]]

Cardinality describes the maximum number of possible occurrences of participating in a relationship.
Participation determines whether all or only some entity occurrences participate in a relationship.
- If the value is non-zero then participation is mandatory, if it can be zero, participation is optional.

![[Pasted image 20241206172823.png]]

## ER Diagram Symbols

### Chen's Notation

![[Pasted image 20241206172839.png]]

### Barker's

![[Pasted image 20241206173350.png]]

### Crow's Foot

![[Pasted image 20241206173409.png]]

### IDEF1X

![[Pasted image 20241206173424.png]]

### UML

![[Pasted image 20241206173437.png]]

### UML Database Design

![[Pasted image 20241206173455.png]]

# ER to Schema

## Steps to Convert - Entities

- Every entity set becomes a table (relation)
- The columns of the table are the atomic attributes of the entity set
- The key column(s) of the table are the key attribute(s) of the entity set
- If the entity set is weak
	- The resulting table must import the key attribute of the owner entity set.
	- The key to this table is the composition of the partial key (of the weak set) and imported key (of the owner set).

## Steps to Convert - Relationships

- Ignore identifying relationship types.
- Every relationship type becomes a table (relation)
- The columns of the table are the key attributes of the entity sets involved, along with any attributes of the relationship type itself.
- The key to this table is chosen from among the key attributes imported from the entity sets, and depends on the cardinality ratio
	- 1:1 Attributes act as independent keys
	- 1:N Attribute on N (many) side chosen as key
	- N:M Attributes combined to form composite key.

## Steps to Convert - Table Reduction

- Tables deriving from N:M (many to many) relationship types must be retained as is.
- A table deriving from a 1:N (one to many) relationship can be merged into the table representing the entity set on the N (many) side of the relationship.
- A table deriving from a 1:1 (one to one) relationship can optionally be merged into the table representing the entity set on either side of the relationship (the choice of merge option may be intuitive, or may involve minimisation of null values, for example).

# Normalisation

Normalisation is a technique for producing a set of relations with desirable properties.

It works by examining relationships (functional dependences) between attributes in a relation and uses a series of test (normal forms) to determine if the attributes are grouped optimally (form suitable relations).

The desirable properties are:
- A minimum number of attributes to support the data requirements of the enterprise.
- That relations contain attributes that are closely related (have functional dependencies).
- That there is a minimum redundancy - each attribute is represented only once (with the exception of foreign keys).

These properties ensure maintainability, do not cause anomalies, require minimum number of operations to maintain, and take up minimum storage.

## Anomalies

### Insertion Anomalies

If we enter in new tuples, there is latitude for data to become inconsistent; multiple representations of the same data could contain conflicting information.

If we want to represent data and do not yet know other data, we would have to provide null values. This would fail if this null value linked to a primary key.

### Deletion Anomalies

Deletion anomalies occur when inconsistencies arise in our database after a delete operation.

### Update Anomalies

Update anomalies occur when inconsistencies arise in our database after an update operation.

## Decomposing Large Relations

When we decompose a large relation we seek to ensure that two properties are maintained:
- Lossless-join - ensure all instances in the original relation can be recreated from the corresponding data in the smaller relations.
- Dependency Preservation - ensure that the constraints on the original relation are maintained by enforcing constraints on the smaller relations.
Normalisation helps us to decompose tables safely so that these properties are observed.

Normalisation is a technique for analysing relations based on their primary key and functional dependencies.

## Functional Dependency

- A functional dependency is the relationship between attributes in a relation. e.g. if A and B are attributes in a relation R, B is functionally dependent on A if every value of A is associated with exactly one value of B.
- A determinant refers to the attribute or group of attributes on the left hand size of the arrow in a functional dependency.

We consider not just the existing data, but understand the nature of the attributes so that we can say that no potential attributes would change the correctness of our functional dependency.

### Identifying Functional Dependencies

- Identifying all functional dependencies requires understanding what attributes represent and how they relate to one another.
- We consider each attribute in relation to the others based on our definitions.

## Identifying Primary Keys with Functional Dependencies

Taking each determinant we look for the determinant for which all attributes (excluding those that make up the candidate key) are functionally dependent on.

### Full Functional Dependency

- Functional dependencies should have a minimum number of attributes.
- A full functional dependency indicates that if A and B are attributes of some relation, B is fully functionally dependent on A if B is functionally dependent on A but not on any proper subset of A.

### Transitive Functional Dependency

- A condition where A, B and C are attributes in a relation and A -> B and B -> C, then C is transitively dependent on A.

## 1NF (First Normal Form)

- The normalisation process first seeks to transform an unnormalized schema into a 1NF schema (1st Normal Form).
- An unnormalized table is one that contains repeating groups.
- A 1NF table is a relation where the intersection of each row and column contains one and only one value.
- We achieve 1NF using one of two techniques:
1. We can place the repeating data with a copy of the original key attributes in a separate relation.
2. We 'flatten' the table by entering appropriate data in empty columns of rows containing repeating data.
3. We arrive at tables that contain atomic values at the intersection of the rows and columns in a relation.
4. It's the only normal form that MUST be achieved to represent data in a relation.

![[Pasted image 20241206185023.png]]

## 2NF (Second Normal Form)

2NF requires that every non-prime attribute A in relation R is fully functionally dependent on the primary key of R (and is also in 1NF).

A general definition of 2NF considers all candidate keys.

A relation R is in second normal form if it is in first normal form and every nonprime attribute A in R is not partially dependent on any key of R.

![[Pasted image 20241206185036.png]]
## 3NF (Third Normal Form)

A table is in 3NF it is in 2NF and no non-prime attribute of R is transitively dependent on the primary key.

![[Pasted image 20241206185043.png]]
## BCNF (Boyce Codd Normal Form)
A table is in BCNF (Boyce Codd Normal Form) if and only if every determinant is a candidate key.

![[Pasted image 20241206185103.png]]

# SQL Data Definition Language (DDL)

In the context of SQL, data definition or data description language (DDL) is a syntax for creating and modifying database objects such as tables, indices, etc.

### Altering a table

A relation can be modified, though modifications should be made with care

```SQLite
ALTER TABLE r ADD A D;
ALTER TABLE r MODIFY COLUMN A D;
ALTER TABLE r DROP COLUMN A;
```

where r is the name of the table and we are adding attribute A with domain (type) D.

- We must be careful that we do alters carefully and consider the implications for introducing anomalies.
	- The new table should be normalised and consideration given to its new structure
	- The new table structure may also require an update of its data - if rows already exist then the new column may have many null values.

## Indexing in DBMS

Indexing is a technique to optimise operational time of database queries using data structures.
It leads to faster query results, better database performance and lesser storage sizes.

We can create an index on an attribute of a relation.
- This creates a data structure (e.g. B+ tree) that allow the system to efficiently search for tuples with a particular value for the attribute.
We can create an index using a syntax such as:
```SQLite
CREATE INDEX <index_name> ON <relation>(<attributelist>);
```

where attributes list is the list of attributes that form the search key for the index.

e.g.
```SQLite
CREATE INDEX dept_index ON instructor (dept_name);
```

## Views

- Views are a mechanism that allow us to treat a query result as a relation
- They are useful for creating customised views of data related to some process
- They can also be used to restrict the views of full relations for some users.
- E.g.: We might create a view for an office clerk that hides personal information about instructors (e.g. salary)

We can create a view as follows:
```SQLite
CREATE VIEW faculty AS
SELECT id, name, dept_name
FROM instructor
```

We can then run queries against the view as we would against any relation.

## Integrity Constraints

Integrity constraints ensure that changes made to databases do not cause any inconsistencies.

These constraints are defined when a table is created.

We can either write SQL to capture these constraints or we can use graphical interfaces in Workbench.
We can also add constraints using an alter statement but we should be careful if the table is populated with existing data.

#### NOT NULL

Any attribute in a relation can have a null value - null is a member of all domains.
In some cases, null is an inappropriate value.
Primary keys must be not null.

#### UNIQUE

- Unique means that for some attribute, no two attribute values in the list of all attribute values can be the same
	- That is they must be unique
- Unique variables can be null however.

#### CHECK

- Check allows us to ensure that attribute values satisfy specific conditions.
- For example, that a salary should be greater than zero

```SQLite
CREATE TABLE instructor  
(  
id int,  
name varchar(20) NOT NULL,  
dept varchar(20),  
salary numeric(8,2) CHECK (salary > 0),  
PRIMARY KEY (id)  
);
```

#### Referential Constraints

- We often wish to ensure that a value that appears in one relation also appears in some other relation.
	- E.g. Department id for instructor
	- By adding a foreign key constraint we ensure that the referenced department must already exist.
	- The referenced attribute must a primary key or a unique value and must be compatible with the attribute described in the referencing table.

```SQLite
CREATE TABLE instructor  
(  
id int,  
name varchar(20) NOT NULL,  
dept varchar(20),  
salary numeric(8,2) CHECK (salary > 0),  
PRIMARY KEY (id),  
FOREIGN KEY (dept_name) REFERENCES department  
)
```

#### Cascades

- If a referential integrity constraint is violated, the attempted operation is rejected.
	- e.g. if we try to delete a row in a table that is also referred to by a foreign key - for e.g., a department referenced by an instructor record - then the operation would be rejected.
- We can override this and allow a delete of a department to also delete any referring instructors
```SQLite
FOREIGN KEY (deptid) references department on delete cascade
```

- We can keep the instructors and replace the department id with null as follows:

```SQLite
FOREIGN KEY (deptid) references department on set null cascade
```

- We can declare these cascades for delete or update operations

## Stored Procedures and Functions

- Most DBMS allow us to define both stored procedures and functions
- Each DBMS has its own syntax for doing this
- We can embed common actions in our database into SQL using functions
	- We've already used functions, such as SUM(), AVG(), etc.
- Stored Procedures capture processes that we might wish to implement
	- We can call these from our SQL or we can invoke them through a library call from a procedural language.

```SQLite
CREATE PROCEDURE `book_room`(  
IN roomid int,  
IN booker varchar(45),  
IN roomname varchar(45),  
IN guestnumber int,  
IN eventdate varchar(45),  
OUT result int)  
BEGIN  
DECLARE roomlimit int;  
SELECT roombookinglimit.limit into roomlimit FROM roombookinglimit WHERE roombookinglimit.roomname  
= roomname;  
IF roomlimit >= guestnumber THEN  
INSERT INTO roombooking values (roomid, booker, roomname, guestnumber, eventdate);  
SET result = 0;  
ELSE  
SET result = 1;  
END IF;  
END
```

### Stored Procedure - Setup & Run

```SQLite
CREATE TABLE `roombookinglimit` (  
`roomname` VARCHAR(45) NOT NULL,  
`limit` INT NULL,  
PRIMARY KEY (`roomname`));  
CREATE TABLE `roombooking` (  
`roomid` INT NULL,  
`booker` VARCHAR(45) NULL,  
`roomname` VARCHAR(45) NULL,  
`guestnumber` INT NULL,  
`event_date` VARCHAR(45) NULL);  
INSERT INTO `roombookinglimit`(`roomname`, `limit`)  
VALUES ('Double', 2),('Triple', 3);  
CALL book_room(101, 'HN', 'Double', 3, '2022-11-08', @R1);  
SELECT @R1; -- Result: 1  
CALL book_room(101, 'HN', 'Triple', 3, '2022-11-08', @R2);  
SELECT @R2; -- Result: 0  
SELECT * FROM roombooking;
```

## Triggers

A trigger extends the idea of a stored procedure and uses many of the same features. It automatically invokes (triggers) in response to some database event such as an insert, update or delete in an associated table.

They have many functions:
- Checking integrity of dta
- Updating other tables based on changes to one table
- Supporting automation of parts of transactions

A trigger can be created as follows:
```SQLite
CREATE TRIGGER trigger_name  
{BEFORE | AFTER} { INSERT | UPDATE | DELETE}  
ON table_name FOR EACH ROW  
trigger_body;
```

### Adding and Showing Triggers

- We can use the same approach to see existing triggers that we might want to edit. We can also create triggers through raw SQL. We can view existing triggers using 'SHOW Triggers'.

## Data Storage

- Main memory- this is where data that we operate on is stored. While it can be expensive, it won't be big enough to maintain a large database. It is also volatile - a power cut or other failure would cause data loss without use of persistent data storage.
- Flash memory - is not volatile. It is cheaper than main memory and less performant. It is faster than magnetic disk and more expensive. Data is organised as blocks. It is very robust.
- Magnetic disks - are not volatile and cheap. They can be prone to failures. They are less performant than flash memory.
- Tape storage is used primarily for backup. Tape is cheap. It is slow to access and read. It is very reliable and durable. It has a very large capacity.

### RAID

- Redundant Arrays of Independence (Inexpensive) Disks (RAID) are devices with a large number of disks.
- Various organisations are used to promote performance and/or reliability.

- Performance is achieved by duplicating data on one or more disks allowing parallel operation (backed by complex management schemes to admit data consistency)
- Reliability is achieved as multiple copies of data are maintained and loss of one disk won't cause a loss of data.

#### How it works

- Data can be mirrored one one or more disks in the same array.
- Some levels allow us to restore the data in case of a failure (Data loss prevention)
- Data is distributed across the drives in one of several ways (RAID levels).
- Standard RAID levels
	- Level 0, 1, 2, 3, 4, 5, 6, 10

#### RAID 0 - Stripping

- Not fault tolerant
- Data is striped across multiple disks

![[Pasted image 20241206192712.png]]

#### RAID 1 - Mirroring and Duplexing

- Is fault tolerant
- Data is copied on more than 1 disk

![[Pasted image 20241206192757.png]]

#### RAID 10 (1+0)

- Combines RAID 1 with RAID 0
- Minimum of 4 disks

![[Pasted image 20241206192823.png]]

#### RAID 5 - Stripping with Parity

- Requires 3 or more disks
- Data is 'striped' across multiple disks along with parity

![[Pasted image 20241206192849.png]]

- Data isn't duplicated
- Parity is used to rebuilt data in case of a disk failure.

### File Blocks

A file is organised as a set of records that are mapped onto blocks.
Several records will occupy a block.

- In a simple model, we can say that blocks contain only whole records.
- This avoids multiple writes for a single record if it is spanning a block
- When a record is deleted, it is marked as deleted and are subsequently overwritten by new records as required.

## Indices

Ordered indices: search keys are stored in sorted order.

Hash indices: search keys are distributed uniformly across 'buckets' using a 'hash function'.

## Data Buffers

Persisted data is stored in 'non volatile' storage (hard drives or SSD's). This is organised into blocks.
Most DBMS have a memory based data buffer to improve performance.
The data buffer is part of memory that is available for the storage of  copies of disk blocks
- These blocks are always duplicated on disk.
- The buffer is managed by the buffer manager.
- We use the buffer as memory access which is much faster than disk access.

### Data Buffer Manager

The buffer manager manages buffer requests
- If a block is needed from disk, the buffer manager checks if it is in memory
- if it is, the BM passes the block address to the requester.
- If it is not in memory, if necessary, space is made by removing some other block and reading the new block.
- The old block is written out before being replaced (if it has been modified)
- The new block is read and its address is passed to the requester.

This is done using a 'least recently used' (LRU) scheme.

### Pinning Blocks

- Buffers employ pins to ensure consistency
- For instance, imagine a block has been read into memory and is being accessed. If that block were evicted and replaced, the read operation would be corrupted.
- To prevent this, a block is pinned before a process interacts with it. Pinned objects are never evicted. When finished, the accessor removes the pin to allow the buffer to consider it eligible for eviction.
- The buffer uses various approaches to ensure that not too many blocks are pinned.

## Block Locks

- Blocks are locked to ensure consistency - that is, certain actions are permitted for one or a subset of users if they hold a lock while other clients must wait to carry out their actions until they too hold a lock.
- These can be shared or exclusive depending on the type of action to be carried out.
	- Shared locks are held by processes that want to read the block.
	- Exclusive locks are held by those that want to update the block.

- Only one process can hold an exclusive lock.
- Requests for locks are queued - they are granted when earlier locks are released.
- Shared locks can be granted where no exclusive lock is held..
- To interact with a block, it must first be pinned. The process then obtains an appropriate lock. All lock must be released before a block is unpinned.

## Transactions

- A transaction is a unit of execution that updates one or more data records.
- However, the collection of steps appears to the user as a single indivisible unit that executes in its entirety or not at all.

### ACID

Transactions are said to have ACID properties.
- Atomicity - either all operations are reflected properly or none at all.
- Consistency - Any change maintains data integrity or the transaction is cancelled in its entirety.
- Isolation - Any read or write of a transaction will not be impacted by the read or write of another transaction. Given two transactions Ti and Tj - then Ti appears to have fully executed before Tj (or vice versa).
- Durability - after a transaction has completed the changes made persist.

#### Atomicity

If the system fails at some intermediary step it would leave the database in an inconsistent state. All steps of the transaction must be completed or none at all. All steps carried out are recorded. This log provides sufficient data to roll back a transaction and return to the initial state.
This is known as 'recovery'.

#### Consistency

It is the responsibility of the client to ensure that the steps of the transaction are executed correctly (in the correct order, with the correct values, etc).

#### Isolation

- Even though atomicity ensures that the database is in a consistent state at the beginning or end of a transaction, there exists a period during the transaction where the database is not consistent.
- If another transaction were to act on the values during this period, their result would be incorrect.
- The concurrency control system ensures that the results of transactions always appear as completed and never in an intermediate state.

#### Durability

The actions are persisted or if a failure occurs just at write time, that sufficient information about the transaction has been written to reconstruct updates or rollback from them.

## Transaction States

![[Pasted image 20241207164253.png]]

- Active - transaction as it executes
- Partially Committed - after the final statement has executed
- Failed - after normal execution cannot continue
- Committed - successfully completed

- We say that a transaction that didn't complete successfully has aborted.
- If a transaction isn't committed, then it can be rolled back - undoing actions that were part of the transaction.
- Once committed, we cannot rollback and would need to apply a compensating transaction.

### System log

Operations that form a transaction are not written to the database until the commit instruction is issued.
Instead, the operations are stored in a log file - a serial file that is maintained by the DBMS.
When a commit is issued, the write operations are retrieved in sequence and applied to the database. In the case of a rollback, the operations that make up that transaction are disregarded.

### Serial vs Concurrent Execution

- Serial execution of transactions implies that transactions execute one after another.
- In reality, concurrent execution is more desirable as transactions can run in parallel

- Concurrent execution is more complicated and requires careful management - concurrent execution can violate the isolation property.
- Concurrency control scheme generate schedules to ensure isolation is maintained and allows transactions to execute concurrently.

### Two Transactions

![[Pasted image 20241207165050.png]]

#### Serial Transactions

We develop a schedule that describes an execution sequence. A transaction would execute to completion or rollback before the other started.

![[Pasted image 20241207165130.png]]

#### A concurrent example

![[Pasted image 20241207165142.png]]

#### An inconsistent concurrent example

![[Pasted image 20241207165157.png]]

### Transaction conflict and schedule equivalence

Two transactions are said to conflict if there are operations by both transactions that are on the same data and at least one operation is a write.

Schedule equivalence can be achieved by applying rules to a concurrent schedule to produce a serial schedule.
- If this can be achieved the transactions are said to be conflict equivalent.
- A schedule of several concurrent transactions is considered serializable if it is equivalent to a serial schedule.

## Precedence Graphs

Given two or more transactions, we create a node for each transaction and a directed edge to denote that one of the following holds:

- Ti executes write(Q) before Tj executes read(Q).
- Ti executes read(Q) before Tj executes write(Q)
- Ti executes write(Q) before Tj executes write(Q).

![[Pasted image 20241207165453.png]]
![[Pasted image 20241207165502.png]]
![[Pasted image 20241207165512.png]]
![[Pasted image 20241207165526.png]]

### Concurrency

We know that serializable schedules of multiple concurrent transactions are guaranteed consistent.
We also know that is is impractical to retrospectively test a schedule of transactions to see if it was serializable.
The solution lies in finding a protocol that transactions should follow that will guarantee that they only participate in serializable schedules.
Two general-purpose solutions have been proposed, of which one is in common use.
- Locking (the common approach)
- Timestamping
We consider locking - in its two-phase locking (2PL) form.

### Concurrency - Locking

- Under this scheme, a transaction should acquire a lock on a data object before accessing it, and release that lock afterward.
- Acquiring a lock might be explicitly done, via a user-issued command; alternatively, the DBMS could implicitly do it (as usual the trade will be between flexibility (user) and simplicity (system)).
- Two types of lock are required:
	- A shared lock, that may be held by multiple transactions but is useful for readers only.
	- An exclusive lock, that may be held by only one transaction at a time and is useful primarily for writers (though a reader could also hold one).

- The DBMS should support an interface for acquiring and releasing locks; it must also support a data structure for recording which extent transactions hold which locks: a lock table; other data structures are also required, such as transaction queues (transactions waiting to acquire locks).
- The implementation contains implementations for three operations:
	- Acquiring a shared lock
	- Acquiring an exclusive lock
	- Releasing a lock that is held
- Recall that a transaction could have a series of database requests.
	- SELECT: A shared lock would suffice
	- UPDATE: An exclusive lock would be required.
	- Lock upgrading and downgrading (no commercial DBMS supports this).

A transaction T is well-behaved if it adheres to the following conventions, which are easily checked by a syntactic analysis of the transaction's operations.
- A transaction T must issue the operation read_lock(X) or write_lock(X) before any read_item(X) operation is performed in T.
- A transaction T must issue the operation write_lock(X) before any write_item(X) operation is performed in T.
- A transaction T must issue the operation unlock(X) after all read_item(X) and write_item(X) operations are complete in T.
- A transaction T will not issue a read_lock(X) operation if it already holds a read (shared) lock or a write (exclusive) lock on item X.
- A transaction will not issue a write_lock(X) operation if it already holds a read(shared) or write (exclusive) lock on item X.