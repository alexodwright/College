## Encapsulation

Encapsulation is grouping states and actions/behaviours in a class. Hiding the internal implementation details while providing a public interface for interacting with the class.

The attributes that describe the object and the actions that can be carried out on the object are encoded in the class.

Each object is an instance of the class.

Benefits of Encapsulation:
- The developer who develops the class will understand what is needed to change the state of the object and can encode this in the method.
- Other developers will not know the requirements of the object as well as they are developing their own code. The object class is an opaque box to them.

## Inheritance

Inheritance is a mechanism that allows a new class to inherit properties and methods from an existing class. It promotes reusability, modularity and the establishment of hierarchical relationships between classes.

If we wanted a new object that is similar to our previous implementation but requires some extra attributes and methods to model it.

We reuse the functionality of the original object, overriding any existing methods that need to be specialised, and add any new attributes and methods.

Benefits:
- Reducing the amount of code we need to write.
- We fix any bugs in the original class just once.

Inheritance captures an 'is-a' relationship between classes.

We analyse the requirements to see what is in common between two classes, and write a class to represent the base.

Next we write more specialised classes which only add the state and behaviour unique to this new specialised class.

In a case where a Manager and Engineer inherit from a Person class.
- Person is the parent of Engineer and Manager
- Engineer and Manager are children of Person
- Manager and Engineer are subclasses of Person
- Person is the superclass of Manager and Engineer.

```Python
from person import Person

class Manager(Person):

	def __init__(self, identity, name, job, salary, project):
		super().__init__(identity, name, job, salary)
		self._project = project.
```

- Extend: Add a new state and behaviour
- Specialise: Where functionality exists in the super class; adding a version of that functionality that is specific to the subclass.

Extending is the same as adding any method or attribute to a class.
## Composition

Composition is a design principle where complex objects are created by combining similar objects, establishing a 'has-a' relationship between them. It allows for the creation of more flexible and reusable code by assembling independent components to form a larger, cohesive structure.

This is useful in the same way inheritance was:
- Less code written
- Fewer bugs
- Any bugs fixed just once

## Object Oriented Programming

Advantages of OOP:
- Admits parallel code developments for groups of developers.
- Helps us write cleaner code that has fewer errors
	- And when errors occur, our code is easier to fix.
- Helps us reuse code
- Allows us to use related code organisation and design techniques.

Disadvantages:
- There is more code with OOP, and OOP design takes more effort
	- Not ideal for prototyping or developing a one off project.

We instantiate an object using a class

### The Class

A class is a set of related state and behaviours that describe some entity.
We capture state with variables and behaviours through methods (aka functions).

Classes act as a factory for instantiating one or more objects as they are the 'blueprint' of of the object.

An object exists in memory and has its own copy of variables to represent its state. These are known as instance variables.

When we call a method, it acts on a particular object.

They ultimately create a new datatype.
### \_\_init__

\_\_init__ is known as the constructor. It is called when we create a new instance of a class. It initialises the class, adding its instance variables, and gives some initial values.

### self

- Self is a reference to the object instance
	- When we call the constructor for the object, the self argument references the object instance.

### \_\_str__

\_\_str__ generates an nicely formatted string representation of an object. It must return a string 

### Methods

A method is a function that belongs to an class. It is like a regular function except that:
- It is contained in a class
- The first parameter is self
	- This causes it to act on the instance variables of a particular instance of the class.

## Properties

Getters and setters provide control of how users of our class can interact with instance variables.

`_` indicates that a variable is protected

The method acts as a gateway through which we can control how instance variables are used.

We use getters to get values - not as important as values aren't overwritten.

We use setters to set values. Much more important as values can be changed and we want to control how this happens.

Setters:
- We can ensure that third party code is not tightly bound to our instance variables. This gives us freedom to change our implementation without forcing changes to their code.

Properties allows access to our attributes through methods but using a syntax that is the same as when we directly access instance variables.
We get all of the simplicity of the attribute syntax but with all of the advantages of using the getter/setter methods.
- We can have error checking or other processing as part of the getter/setter.
- Third party code remains loosely bound to our code.

In the event that direct access was originally implemented, we can now modify our code to use getters/setters without requiring changes in third party code.

### Property Decorators

```Python
@property
def pay(self): # use name of attribute but without '_'
	return self._pay

@pay.setter
def pay(self, pay): # use name of attribute but without '_'
	if pay < 0 or pay > 100000:
		print(f"{pay} is an invalid pay value - no value set")
	else:
		self._pay = pay

print(person.pay)
```

### Properties

```Python
def getPay(self):
	return self._pay

def setPay(self, pay):
	if pay < 0 or pay > 100000:
		print(f"{pay} is an invalid pay value - no value set")
	else:
		self._pay = pay

pay = property(getPay, setPay) # getter first then setter second
```

## Try - Except

```Python
try:
	val = int(input("Enter in a positive number: "))
except ValueError:
	print("An invalid value was entered - enter numbers")
except Exception:
	print("Some unanticipated event occurred")

# we can also add actions that are always executed whether or not
# there is an exception

finally:
	# do something
```

- We can raise an exception in our code when we want to communicate that something unusual has occurred - `raise ValueError`
- We can also customise the message we pass back which can be useful between instances of the same exception - `raise ValueError("An incorrect number was entered")`

We can make our own exception:
```Python
class MyException(Exception):
```

Prime area to handle exceptions are at construction and when values are taken into the class. We should check that they are in a valid range of values, and of the expected type.

## Object Persistence

- There are many ways to persist data from a program:
	- Write to file
	- Store in DB
	- Serialise objects and write to disk - called shelving.
- Pickles allow us to serialise (convert to a string of bytes and write to a file) any object or collection of objects.
- Shelves allow us to store pickled objects as key/value pairs:
	- In effect a persist-able dictionary
	- It provides the usual dictionary functions such as `len()` etc.
	- We must open and close them
	- Pickling is done under the hood when we shelve an object; we don't have to explicitly do this action.

```Python
import shelve

db = shelve.open("exampledb")
db[data.attribute] = var
db.close()
```

## TKinter

- TKinter is a lightweight framework for developing user interfaces in Python.
- The basic components in the library are:
	- Basic Frame
	- Widgets
	- Layouts
	- Event handlers and event loop

### Event Driven Program

- Event-driven programming is a programming paradigm in which the flow of the program is determined by events such as user actions (mouse clicks, key presses).
- Events are generated by the OS and passed to the running application where they are translated into object instances (Event).
	- Here they are used to trigger event handlers where the event can be passed and values about the event accessed.

### Design Patterns

Design patterns are established approaches for organising code for typical operations that we might have to implement.

One pattern is called the Model View Controller:
- It seeks to achieve a 'separation of concerns' - essentially decoupling the data representation from the interface.
- This makes it easy to present different views of the data to different apps.

- The model is responsible for managing data in the application. It is manipulated by the controller and provides information to the view.
- The controller receives inputs from the user, validates those and makes changes to the mode.
- The view presents information to the user - several views of the same data can be presented.

![[Pasted image 20241214150707.png]]

## Unit Testing

- A software development process in which the smallest testable parts of an application, called units, are individually scrutinized for proper operation.
- Unit tests can be automated tests or manual tests, written and run by software developers to ensure that a section of an application (known as the 'unit') meets its design and behaves as intended.
- They are often performed by the developer who originally wrote the code, as a first line of defence before conducting further testing.

Benefits:
- Early detection of problems in the development cycle
- Reduced cost
- Detects changes which may break a design.
- Test-driven development: The same unit tests are run against that function frequently as the larger code base is developed either as the code is changed or via an automated process with the build. If the unit tests fail, it is considered to be a bug either in the changed code or the tests themselves.

## Regular Expressions

- Regular expressions are a powerful language for matching text patterns
- We create a 'search pattern' which is made of a sequence of characters.
- They are used in text editors and word processors, search engines, web app frameworks, etc.

We use the 're' library in Python.

To create a pattern use compile function:
```Python
import re
p = re.compile('ab*')
```

We can then call the following methods against the compiled object:
- `match()` - determine if the regex matches at the beginning of the string.
- `search()` - scan through a string, looking for any location where the regex matches.
- `findall()` - find all substrings where the regex matches and return these as a list.

![[Pasted image 20241214153405.png]]