## Getting max of multiple numbers

### Recommended Questions for Practice:

1. [Maximum Number of Words Found in Sentence](../../questions/maximum_number_of_words_found_in_sentence/README.md)

### Approach 1: Getting the max of numbers in a List by overriding the max number, only if a number is greater than it. 

```python3
from typing import List
current_max: int = 0
my_numbers: List[int] = [10, 20]

for number in my_numbers:
    if number > current_max:
        current_max = number

print(current_max)
```

This will print

```txt
20
```

### Approach 2: Pass the list directly into `max()`

This is way faster compared to Approach 1, as `max()` is a standard python function implemented in C.

This means, the C compiler is able to apply optimizations to make it faster than a standard python implemented approach like Approach 1

```
from typing import List

my_list: List[int] = [1,2,3,4,5,6,7,8,9]
my_max: int = max(my_list)
print(my_max)
```

This will print

```txt
9
```