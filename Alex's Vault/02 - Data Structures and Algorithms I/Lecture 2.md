## Problem

### Checking for Anagrams

Give two strings, or lists of elements, determine whether or not they are anagrams - that is, exactly the same bag of elements.

To simplify the problem, consider lists where the elements are selected from integers between 0 and 9999.

### Replace Method

```Python
for each x in input1:
	if x is not in input1:
		return false
	else:
		input2.replace(x, "", 1)
return true
```

### Sort Method

```Python
input1.sort()
input2.sort()
for i in range(len(input1)):
	if input1[i] != input2[i]:
	return false
return true
```

### Dictionary Method

```Python
dict1 = {for k, input1.count(k) for k in input1}
dict2 = {for k, input2.count(k) for k in input2}
return dict1 == dict2
```

### Count Method

Create a list with 9999 0’s.

Treat the indexes as the ASCII code of each character of the inputs.

Add 1 to the index for each occurrence of a letter in input1.

Subtract 1 to the index for each occurrence of a letter in input2.