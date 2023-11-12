## Checking the length of a list, with `len()`

### Recommended Questions for Practice:

1. [Maximum Number of Words Found in Sentence](../../questions/maximum_number_of_words_found_in_sentence/README.md)

### Example 1: Checking the length of a `List[str]` with `len()`

```python3
from typing import List
my_list: List[str] = ["this", "is", "a", "sentence"]
my_list_length: int = len(my_list)
print(my_list_length)
```

This will print 4

```txt
4
```

### Details on `len()`:

The length of a list is stored as an attribute when the list is instantiated.

Hence, calling `len()` is O(1) Worst Case Time Complexity