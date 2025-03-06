## Object Orientated Programming Building Block - The Class

```Assembly
class Light(object):

	def __init__(self, isOnOff):
		self._isOnOff = isOnOff
		
kitchenLight = Light(True)
hallLight = Light(False)
```

In order to initialise all instances of this object in a consistent manner, we define a constructor.

In Python this constructor method is named __ init __ which is a method, though we only ever use the method name for constructors.

A method is a function that is part of a class. Its header begins with the def keyword and it’s first parameter is always self. The __ init __ method never returns a value.