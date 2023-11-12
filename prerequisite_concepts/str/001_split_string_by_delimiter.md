## python's standard `str`'s `split` method, to split a sentence into a `List[str]` by space as a delimiter `" "`

### Recommended Questions for Practice:

1. [Maximum Number of Words Found in Sentence](../../questions/maximum_number_of_words_found_in_sentence/README.md)

### Example 1: Splitting a sentence `str` into a `List[str]` of words
 
```python3
from typing import List
my_string: str = "my sentence"
my_split_string: List[str] = my_string.split(" ")   # ["my", "sentence"]
```