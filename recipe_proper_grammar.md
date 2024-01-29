# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
def check_grammar(text):
    
    pass
checks that a text starts with a capital letter and ends with punctuation (of any appropriate kind)

parameters: 
    text: a string with words

returns:
    True if the text is grammatically correct or False if it is not
side effects:
    hopefully none?

```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

#check for capitalization at the beginning of the text

check_grammar('I am a sentence.') => True

# check for punctuation at the end

check_grammar('I am still a sentence') => True

# check for other alternative punctuation that isn't just a period

check_grammar('I am a yelling sentence!') => True


```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]

```

Ensure all test function names are unique, otherwise pytest will ignore them!
