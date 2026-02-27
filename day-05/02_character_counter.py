"""
## **EXERCISE: Character Counter**

**OBJECTIVE:** Given a string (e.g. `"hello world"`), we want to design a function/script that can count the frequency of unique characters in that string.

**INPUT:** `"data"`, `"DATA"`, `"Data"`

**OUTPUT:**
  { "d": 1, "a": 2, "t": 1 }
---
"""

# dictionary = { "name": "Chett" }
# dictionary.get("age") # this will not error out

def character_counter(string):
    char_counter = {}
    for char in string:
        char_counter[char] = char_counter.get(char, 0) + 1
    return char_counter