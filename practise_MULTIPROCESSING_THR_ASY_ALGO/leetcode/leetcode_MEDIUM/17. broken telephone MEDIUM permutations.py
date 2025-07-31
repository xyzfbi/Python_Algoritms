from itertools import product
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        comb = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        letters = [comb[d] for d in digits]
        comb = product(*letters)
        return [''.join(c) for c in comb]

solution = Solution()
print(solution.letterCombinations('23'))


