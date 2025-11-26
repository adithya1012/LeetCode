# Given a positive integer x, return any list of values whose squared and summed together produce x
# I used a greedy approach, starting from the closest integer lower or equal to sqrt of x, them added all numbers below it repeating when possible, until reaching x.

def find_squares_recursive(x):
    """
    Wrapper function for recursive solution.
    """
    memo = {}

    def helper(n):
        # Base case
        if n == 0:
            return []

        # Check memo
        if n in memo:
            return memo[n]

        # Try all possible squares and find minimum
        best_result = None
        min_length = float('inf')

        j = 1
        while j * j <= n:
            # Recursively solve for remaining
            remaining_result = helper(n - j * j)
            current_result = [j] + remaining_result

            if len(current_result) < min_length:
                min_length = len(current_result)
                best_result = current_result

            j += 1

        memo[n] = best_result
        return best_result

    return helper(x)


# Test cases
test_cases = [12, 6, 13, 7, 25, 100]
for x in test_cases:
    result = find_squares_recursive(x)
    squares_sum = sum(n * n for n in result)
    print(f"x = {x}: {result} → {' + '.join(str(n * n) for n in result)} = {squares_sum}")