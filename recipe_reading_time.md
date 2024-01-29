
# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
def estimate_reading_time(text):
    
    pass
calculates reading time from the length of the text 

parameters: 
    text: a string with words

returns:
    estimated_time: string including int representing the time (in minutes)
                OR BONUS: a string showing the time expected (in hours and minutes)
side effects:
    hopefully none?

```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

#if the string is less than 200 words, return 'less than a minute' for the estimated time

estimate_reading_time('I am a tiny little sentence') => 'Estimated reading time: less than a minute.'

# if the string is empty, return 'please provide a text'

estimate_reading_time('') => 'Please provide a text.'

# if the string is 200+ words, return estimated reading time

estimate_reading_time(long_sample_text) => 'Estimated reading time: {insert reading time here}'

# if the string is so long that it takes more than 59 minutes to read, return estimated time in hours and minutes

estimate_reading_time(really_long_sample_text) => 'Estimated reading time: {insert reading time in hours and minutes}
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
