class Solution:
    def generateParenthesis(self, n: int):
        result = []

        def backtrack(current, open_count, close_count):
            # when length becomes 2*n
            if len(current) == 2 * n:
                result.append(current)
                return

            # add '('
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)

            # add ')'
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return result