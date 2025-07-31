from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(idx, comb, total):
            if total == target:
                result.append(list(comb))

            if total > target or idx >= len(candidates):
                return

            if comb in result:
                return
            comb.append(candidates[idx])
            backtrack(idx, comb, total + candidates[idx])
            comb.pop()
            backtrack(idx + 1, comb, total)

        backtrack(0, [], 0)
        return result

if __name__ == '__main__':
    test = Solution()
    x = test.combinationSum([2, 3, 6, 7], 7)
    print(*x)