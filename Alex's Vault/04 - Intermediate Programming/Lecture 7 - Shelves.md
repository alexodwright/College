## Sample Exam

### Question 1:

In object oriented programming, ‘setters methods’ are used to set the value of attributes in objects. What is an advantage of using setter methods?

**Part B:**

In the Python programming language, we can declare properties. What are properties and what are their advantages?

**Part C:**

In object oriented programming, inheritance enables new objects to take the properties and behaviours of existing objects. The subclass can extend or specialist its superclass. Explain what is meant by specialisation and extension in this context.

### Question 2:

Implement a Python class called Ebook. The Ebook inherits from the Book class.

The Book class is described by title of book and author of book. Provide an implementation for the Book class including a constructor, getters/setters, **str** method and properties.

The Ebook class extends the Book class by adding a format property that describes the format of the e-book. Provide an implementation for this class including a constructor, getters/setters, __str_ method and properties.

There is no need to add error checking or a test block to your solution.

## Test Topics

Importance of Object Oriented Programming (OOP) particularly in the software engineering context.

- Structure/Packaging, Robust Code, Reusable Code

Concepts in OOP

- Encapsulation - what it is, why is it useful?
- Inheritance - what it is, why is it useful?
- Composition - what it is, why is it useful?

Class and Object:

- What are classes? What are objects? How are they different?

Structure of a class:

- Defining classes, adding inheritance
    - How do we document classes?
- Role of the constructor:
    - What is it? Why is it used?
    - Error checking
    - Initializing inherited classes
    - Adding and initializing instance variables.

Exceptions (raise, try/except)

- What are exceptions? Why are they used?
- Best practices around exceptions
- Cursory knowledge about common exceptions (TypeError, ValueError, etc)

Self and what it represents in the context of a method

- Scope of instance variables
- Use of underscore and its importance

Methods (how are they different to functions)

- How to document these

Properties (both types, related getters and setters)

- How to use
- How they relate to encapsulation and why this is important.

Magic/Dunder variables and methods

- Example of **str**

## NOT ON CLASS TEST

- Role of environments/Anaconda or their use, other development tools (e.g. Docker etc)
- Magic methods such as __eq__, __ne__, etc
- Finally/else in exception checking.

## Object Persistence

There are many ways to persist data from your program

- You can write to file
- You can store data in database
- You can serialise your objects and write them to disk - This final option is called **shelving**