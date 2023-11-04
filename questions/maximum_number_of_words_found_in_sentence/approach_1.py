from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words: int = 0
        for sentence in sentences:
            number_of_spaces_between_words: int = 0
            for character in sentence:
                if character == " ":
                    number_of_spaces_between_words += 1
            number_of_words: int = number_of_spaces_between_words + 1
            max_words = max(max_words, number_of_words)
        return max_words
