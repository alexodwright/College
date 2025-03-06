- Regular expressions are a powerful language for matching text patterns.
- We create a 'search pattern' which is made up of a sequence of characters - some of which can have special meanings.
- Regular expressions find use in text editors and word processors, search engines, web app frameworks, etc.

- We use the 're' library in Python to create and run regular expressions.
- To create and use a regular expression we follow these steps
	- Import 're'
	- Create a pattern to match against
	- Search for the pattern in some string.

- To create a pattern we use the compile function - for example:
```Python
import re
p = re.compile('ab*')
```
- We can then call the following methods against the compiled object:
	- match() - determine if the regex matches at the beginning of the string.
	- search() - scan through a string, looking for any location where the regex matches.
	- findall() - find all sub-strings where the regex matches and return these as a list.
## Regex Patterns

![[Pasted image 20241126122223.png]]

## Repetition and Options

- We can indicate that various characters or character ranges are detected in some pattern.
	- + - 1 or more occurrences of the pattern to its left, e.g. one or more 'i's

