## Iterating items in a `List` with `for`

### Recommended Questions for Practice:

1. [Maximum Number of Words Found in Sentence](../../questions/maximum_number_of_words_found_in_sentence/README.md)

### Example 1: Iterating words in a `List[str]`

```python3
from typing import List
my_list: List[str] = ["this", "is", "a", "word"]

for word in my_list:
    print(word)
```

This will iterate 4 times (once for each word in the list), and print each in the list

```txt
this
is
a
word
```