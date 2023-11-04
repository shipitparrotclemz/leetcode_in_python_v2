from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words: int = 0
        for sentence in sentences:
            # split is expensive, O(M), as it has to go through all characters in the sentence
            words_in_sentence: List[str] = sentence.split(" ")
            # len() gets the pre-computed length, stored under the hood. O(1)
            num_of_words: int = len(words_in_sentence)
            max_words = max(max_words, num_of_words)
        return max_words
