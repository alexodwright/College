unctional Dependencies & Normalisation Forms

## 1. Database Anomalies

Given the following table, provide examples of insertion, deletion, and update anomalies.

![[Pasted image 20241104121910.png]]
### Insertion Anomaly:

Suppose we need to insert the s_id, but the student has not opted for any subjects, we would have to insert NULL in the subject opted column, leading to insertion anomaly.

### Update Anomaly:

To update the address of a student who occurs twice or more in a table, we will have to update s_address in all the rows, otherwise the data will become inconsistent.

### Deletion Anomaly:

"Physics" is only appearing once (s_id of 404), when we delete that row, the subject would be deleted along with it.


## Functional Dependencies

The following table lists sample dentist/patient appointment data. A patient is given an appointment at a specific time and date with a dentist located in a particular surgery. On each day of patient appointments a dentist is allocated to a specific surgery for that day.

Table displaying dentist/patient appointment data.

![[Pasted image 20241104121650.png]]

### Functional Dependencies

**Note:** A functional dependency is a relationship between two sets of attributes in a database where one set (the determinant) determines the values of the other set (the dependent). For example, in a database of employees, the employee's ID number (determinant) would determine the employee's name, address, and other personal information (dependent). This means that, given an employee's ID number, we can determine the corresponding employee's name and other personal information, but not vice versa.

{staffNo} $\rightarrow$ {dentistName}
{patNo} $\rightarrow$ {patName}
{patNo} $\rightarrow$ {SurgeryNo}
{staffNo, Appointment} $\rightarrow$ {patNo}

## Normal Forms

### 3.a First Normal Form (1NF)

Indicate if the following table is in 1NF, if not convert the table into 1NF.

![[Pasted image 20241104122357.png]]

### Answer:

**First Normal Form (1NF)** is a property of a relation

| empID | s_name | language |
| ----- | ------ | -------- |
| 402   | Alex   | English  |
| 402   | Alex   | French   |
| ...   | ...    | ...      |
### 3.b Second Normal Form (2NF)

Indicate if the following table is in 2NF, if not convert the table into 2NF.

![[Pasted image 20241104124023.png]]

In this case Sid is the primary key and represents the student's ID. The student's name is represented by SName and their overall mark by Score. Dept information includes a department ID (DeptID) and a Department Name (DName). It also includes a department location (DLoc).

### Answer:

Primary Key: {Sid, DeptID}

2NF Conditions:
- 1NF
- No partial dependency on the primary key

{Sid, DeptID} $\rightarrow$ Sname (Partial Dependency, no need for DeptID)
{Sid, DeptID} $\rightarrow$ Dname

Sid, Sname, Score

Student Table

| Sid | Sname | Score |
| --- | ----- | ----- |
| 121 | John  | 85    |
| 122 | Mary  | 90    |
| 123 | Sally | 80    |
Department Table

| DeptId | Dname   | DLoc |
| ------ | ------- | ---- |
| 1      | CompSci | WGB  |
| 2      | Math    | Kane |
Link Table

| Sid | DeptID |
| --- | ------ |
| 121 | 1      |
| 122 | 2      |

### Third Normal Form (3NF)

Indication if the following table is in 3NF, if not convert the table into 3NF.

![[Pasted image 20241104124709.png]]

### Answer:

