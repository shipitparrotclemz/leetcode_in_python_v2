import pytest
from typing import List
from questions.maximum_number_of_words_found_in_sentence.approach_1 import Solution


@pytest.fixture
def solution_object() -> Solution:
    return Solution()


class TestMaxNumberOfWordsFoundInSentenceApproachOne:
    @pytest.mark.parametrize(
        ("sentences", "expected"),
        (
            (["word"], 1),
            (["this is a sentence"], 4),
            (["this is a sentence", "this is a sentence"], 4),
            (["this is a sentence", "this is also another sentence"], 5),
        ),
    )
    def test_approach_one(
        self, solution_object: Solution, sentences: List[str], expected: int
    ):
        answer: int = solution_object.mostWordsFound(sentences)
        assert answer == expected
