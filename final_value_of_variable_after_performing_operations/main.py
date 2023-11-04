from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        """
        High Level Approach
        - Define a final value `X` (`int`)
        - Iterate every value (str) in operations
            - Check if value is an increment or decrement operation `==`
            - Increment X or Decrement X
        - return `X`

        Clusters of Test Cases
        1. Purely contains only increment operations
        - ["++X"], Expected = 1
        2. Purely contains only decrement operations
        - ["--X"], Expected = -1
        3. Contain both increment and decrement operations
        - ["--X", "++X"], Expected = 0
        4. No operations, Expected = 0
        - []

        N is the size or length of your list:
        - operations

        Worst Case Time Complexity:
        - In the worse case scenario, how does your algorithm's time taken to run
        - Scale with the input size N
        - Removing co-efficients, and only caring about the scale (polynomial)
        - O(N)

        Worst Space Complexity:
        - in the worst case scneario, how does your algorithm's RAM (random access memory)
        scale with input size N
        - O(1)
        """
        X: int = 0

        for operation in operations:
            if operation == "++X" or operation == "X++":
                X += 1
            else:
                X -= 1
        return X
