def count_numbers_with_digit_sum(X, Y):
    digits = list(map(int, str(X)))  # Extract digits of X
    memo = {}  # Dictionary for memoization

    def dp(pos, curr_sum, tight):
        # Base Case: If we've processed all digits
        if pos == len(digits):
            return 1 if curr_sum == Y else 0

        # Memoization check
        if (pos, curr_sum, tight) in memo:
            return memo[(pos, curr_sum, tight)]

        limit = digits[pos] if tight else 9  # If tight, bound by the digit in X, otherwise 9
        total_count = 0

        for d in range(0, limit + 1):
            total_count += dp(pos + 1, curr_sum + d, tight and (d == limit))

        # Store result in memoization dictionary
        memo[(pos, curr_sum, tight)] = total_count
        return total_count

    result = dp(0, 0, True)
    return result if result > 0 else -1


# Input
X = int(input())
Y = int(input())

# Output
print(count_numbers_with_digit_sum(X, Y))
