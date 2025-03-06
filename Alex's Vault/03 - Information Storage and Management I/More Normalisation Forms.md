---
cssclasses:
  - center-table-contents
---
## Normalisation

Normalisation is a technique for producing a set of relations with desirable properties

Normalisation works by examining relationships (functional dependencies) between attributes in a relation and uses a series of tests (normal forms) to determine if the attributes are grouped optimally (form suitable relations).

The desirable properties are:
- A minimum number of attributes to support the data requirements of the enterprise.
- That relations contain attributes that are closely related (have functional dependencies)
- That there is minimum redundancy - each attribute is represented only once (with the exception of foreign keys).

These properties ensure maintainability, do not cause anomalies, require minimum number of operations to maintain, and take up minimum storage.

## Normalisation Forms

![[Pasted image 20241029131420.png]]

## 1NF (First Normal Form)

The normalisation process first seeks to transform an unnormalized schema into a 1NF schema (1st normal form)
An unnormalized table is one that contains repeating groups.
A 1NF table is a relation where the intersection of each row and column contains one and only one vale.
We achieve 1NF using one of two techniques.
1. We can place the repeating data with a copy of the original key attributes in a separate relation.
2. We 'flatten' the table by entering appropriate data in empty columns of rows containing repeating data.
We arrive at tables that contain atomic values at the intersection of the rows and columns in a relation.
It's the only normal form that MUST be achieved to represent data in a relation.
## 1NF (First Normal Form)

The following are unnormalized tables (containing the same data)

Department

| DNAME          | DNUMBER | DMGRSSN   | DLOCATION                      |
| -------------- | ------- | --------- | ------------------------------ |
| Research       | 5       | 333445555 | (Bellaire, Sugarland, Houston) |
| Administration | 4       | 987654321 | Stafford                       |
| Headquarters   | 1       | 888665555 | Houston                        |

| DNAME          | DNUMBER | DMGRSSN   | DLOCATION |
| -------------- | ------- | --------- | --------- |
| Research       | 5       | 333445555 | Bellaire  |
|                |         |           | Sugarland |
|                |         |           | Houston   |
| Administration | 4       | 987654321 | Stafford  |
| Headquarters   | 1       | 888665555 | Houston   |
## 2NF - An Introduction

2NF requires that every non-prime attribute A in relation R is fully functionally dependent on the primary key of R. *And is also in 1NF*

Remember - a fully functional dependency X $\rightarrow$ Y is a fully functionally dependent if removal of any attribute A from X means that the dependency doesn't hold anymore.

## Full Functional Dependency

Functional dependencies should have a minimum number of attributes.
A full functional dependency indicates that if A and B are attributes of some relation, B is fully functionally dependent on A if B is fully functionally dependent on A but not on any proper subset of A.
For example:

```
staffNo, sName -> branchNo
staffNo -> branchNo
```

The **former** is a partial functional dependency as there is an attribute that can be removed from the dependency.
The **latter** is fully functionally dependent - this is the type of dependency we are interested in.

## 2NF - Example

Employee_Project

![[Pasted image 20241029132556.png]]
![[Pasted image 20241029132606.png]]

## 2NF - A General Definition

A general definition of 2NF considers **all candidate keys**
A relation R is in second normal form (2NF) if in 1NF and every nonprime attribute A in R is not partially dependent on any key of R.

![[Pasted image 20241029132719.png]]

FD3 is partially dependent on the candidate key identified in FD2:
- We can safely remove Eircode and still identify Tax_Rate as this is functionally dependent on SmallAreaId.

![[Pasted image 20241029132811.png]]

Action: Normalize further by decomposing into tables that are fully functionally dependent.

## 3NF

A table is in 3NF if it is in 2NF and no non-prime attribute of R is transitively dependent on the primary key.
Remember a transitive dependency is when there is a set of attributes Z that is not a subset of any key of R and both X $\rightarrow$ Z and Z $\rightarrow$ Y hold.

## Transitive Functional Dependency

A condition where A, B and C are attributes in a relation and A $\rightarrow$ B and B $\rightarrow$ C, then C is transitively dependent on A.

![[Pasted image 20241029133034.png]]

## 3NF

Emp_dept

![[Pasted image 20241029133405.png]]

snn $\rightarrow$ dnumber
dnumber $\rightarrow$ dmgrssn

therefore: ssn $\rightarrow$ dmgrssn

(similarly for snn $\rightarrow$ dname)

![[Pasted image 20241029133452.png]]

## 3NF General Definition & BCNF

A table is in 3NF if it is in 2NF and no non-candidate-key attribute is transitively dependent on any candidate key.
A table is in BCNF (Boyce Codd Normal Form) if and only if every determinant is a candidate key.

## BCNF Example

- We are presented with the following scenario:
ClientInterview relation captures interviews of clients by staff. Members of staff interviewing clients are allocated specific rooms on the day of the interview. A room may be allocated to several staff members as required throughout the day. A client is interviewed only once in a given day but may be asked back on another day for a follow up.

- The following schema results:

| clientNo | interviewDate | interviewTime | staffNo | roomNo |
| -------- | ------------- | ------------- | ------- | ------ |
| X        | 2022-02-02    | 10:00         | 1       | A      |
| Y        | 2022-02-02    | 11:00         | 2       | A      |
| X        | 2022-03-15    | 16:00         | 3       | B      |
| Z        | 2022-04-01    | 14:00         | 1       | C      |

- We list the functional dependencies
	- fd1 clientNo, interviewDate $\rightarrow$ interviewTime, staffNo, roomNo
	- fd2 staffNo, interviewDate, interviewTime $\rightarrow$ clientNo
	- fd3 roomNo, interviewDate, interviewTime $\rightarrow$ staffNo, clientNo
	- fd4 staffNo, interviewDate $\rightarrow$ roomNo
## BCNF Example

- fd4 staffNo, interviewDate $\rightarrow$ roomNo is in breach of BCNF
	- The determinant is not a candidate key
	- The relation might suffer update anomalies as a result
- We resolve this by decomposing the table into two relations, interview and staffRoom as follows:
	- Interview(clientNo, interviewDate, interviewTime, staffNo)
	- StaffRoom(staff,No, interviewDate, roomNo)