
# How to Connect to a DMBS

We can connect to a DBMS using several techniques

- Programmatically - using a programming language such as Python
- Through the command line interface (CLI) executed in a terminal or command line interface.
- Through a graphical user interface such as MySQL Workbench and other software.

Reserved words cannot be used as identifiers (column/table names)

Common Reserved words:

![[image 21.png|image 21.png]]

## SQL Data Types

![[image 1 18.png|image 1 18.png]]

- Data types of value - associated with attributes
- Provide guidelines for DBMS to store and manage data.
- Their naming and characteristics may vary - depend on DBMS.

## Common Data Types I

|             |                                                                                          |
| ----------- | ---------------------------------------------------------------------------------------- |
| Data Type   | Description                                                                              |
| CHAR(N)     | A string with a fixed length of N characters.                                            |
| VARCHAR(N)  | A string with a maximum length of N characters                                           |
| NCHAR(N)    | A Unicode string with a fixed length of N characters (typically width * for storage)     |
| NVARCHAR(N) | A Unicode string with a maximum length of N characters (typically width * 2 for storage) |
| TEXT        | A string with a maximum length of 64KB                                                   |
| LONGTEXT    | A string with a maximum length of 4GB                                                    |
| BOOL        | True (nonzero values) or False (zero)                                                    |

## Common Data Types II

|               |                                                                                                                        |
| ------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Data Type     | Description                                                                                                            |
| INT(N)        | An integer with a maximum display of width N                                                                           |
| BIGINT        | A large integer:  <br>- Signed: -9223372036854775808 to 9223372036854775807  <br>- Unsigned: 0 to 18446744073709551615 |
| DOUBLE(N, d)  | A floating-point number with N as the total number of digits and d as the number of digits after the decimal point.    |
| DECIMAL(N, d) | A fixed-point number with N as the total number of digits and d as the number of digits after the decimal point        |
| DATE          | A YYYY-MM-DD date                                                                                                      |
| DATETIME      | A YYYY-MM-DD hh:mm:ss date and time                                                                                    |
| TIMESTAMP     | A timestamp - The number of seconds from 1970-01-01 00:00:00 UTC                                                       |
