class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        arr = [0] * (2 * n - 1)
        used = set()

        def backtrack(index):
            if index == len(arr):
                return True

            for val in reversed(range(1, n + 1)):
                if val in used:
                    continue
                if val > 1 and (index + val >= len(arr) or arr[index + val]):
                    continue

                used.add(val)
                arr[index] = val
                if val > 1:
                    arr[index + val] = val

                j = index + 1
                while j < len(arr) and arr[j]:
                    j += 1

                if backtrack(j):
                    return True

                used.remove(val)
                arr[index] = 0
                if val > 1:
                    arr[index + val] = 0
            return False

        backtrack(0)
        return arr
