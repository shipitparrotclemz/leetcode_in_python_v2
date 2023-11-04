from typing import List

import pytest
from questions.final_value_of_variable_after_performing_operations.main import Solution


@pytest.fixture
def solution_object() -> Solution:
    return Solution()


class TestFinalValueOfVariableAfterPerformingOperations:
    @pytest.mark.parametrize(
        ("input", "expected_answer"),
        (
            (["--X", "X++", "X++"], 1),
            (["++X", "++X", "X++"], 3),
            (["X++", "++X", "--X", "X--"], 0),
        ),
    )
    def test_solution(
        self, solution_object: Solution, input: List[str], expected_answer: int
    ) -> None:
        output: int = solution_object.finalValueAfterOperations(input)
        assert output == expected_answer
