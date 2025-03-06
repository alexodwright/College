## Object Oriented Programming Building Block - The Class

### Magic Methods

Python provides a number of methods and variables for every object. We can view these by running

```Python
print(dir(Light))
# or any classname
```

or

```Python
print(dir(kitchenLight))
# or any instance of a class
```

They are marked as having reserved meaning in Python with trailing and leading double underscore e.g. __ init __, __ str __.

These are known as dunder or magic methods.

We can provide our own version (or override) these magic methods to add our own class specific behaviour.

Getters and Setters provide control of how users of our class can interact with instance variables.  
We want to control how users will set our instance variables.  
This is especially true of variables with a leading ‘_’ character. It makes no difference to the Python interpreter but is read by other developers as indicating a variable is protected (i.e. shouldn’t be changed directly).  

We do this by providing a method to set the variables. We could add checks (e.g. types, values etc) or determine when a variable is set etc. The method acts as a gateway through which we can control how instance variables are used.

We use getters to get values - not as important as values aren’t overwritten.

We use setters to set values. Much more important as values can be changed and we want to control how this happens.

## Supporting Encapsulation

Already we mark variables as protected with an ‘_’ - we indicate that users of our class should proceed with caution when using variables named like this.

We should encourage developers to use methods we provide to change instance variable values. This is advantageous.

- We can ensure values are changed in a controlled way.
- We can ensure that third party code is not tightly bound to our instance variables. This gives us freedom to change our implementation without forcing changes to their code.