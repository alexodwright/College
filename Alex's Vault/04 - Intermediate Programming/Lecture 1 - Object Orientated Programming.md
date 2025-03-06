Object Orientated Programming is a programming style characterised by Encapsulation, Inheritance and Composition.

### Encapsulation

We group state and actions/behaviours in a class. This is called encapsulation. The attributes that describe objects and the actions that can be carried out on the object are encoded in the class.

One class can describe each object. Each object is an instance of a class.

Ideally, we change the object’s state with a method.

The developer who develops the class will understand what is needed to change the state of the object and can encode this in the method.

Other developers will not know the requirements of the object as well as they are developing their own code. The object class is an opaque box to them.

### Inheritance

A regular object has already been implemented.

But now we have a new type of object that requires some extra attributes and methods to model it.

We could start from scratch, or we could reuse the functionality of the original object - using what we can as is, overriding any existing methods that need to be specialised, and add any new attributes and methods.

This is called inheritance.

This reduces the amount of code that we need to write and we can fix any bugs in the original class just once.

### Composition

We can use model complex objects.

Say we have a room with a light and a light switch

Rather than write a single class, we write a class, Room, that is composed of the methods and actions required for a room, but reuses the classes we have already written. This is useful in the same way inheritance was - less code written, fewer bugs, and any bugs fixed just once.

## Python vs Pure Object Oriented Languages

Languages such as Java are pure Object Orientated languages. They enforce the principles of Object Orientation strictly.

Python doesn’t require OO to be used.

Python also emphasises freedom to use the language in any way. Developers implement encapsulation based on trust.  
Python is more OO in some ways than Java, allowing the use of multiple inheritance and other features.