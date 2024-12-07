def function_with_uncommon_error_solution(n):
    fib_numbers = [0, 1]
    if n <= 1:
        return fib_numbers[n]
    else:
        for i in range(2, n + 1):
            next_fib = fib_numbers[i - 1] + fib_numbers[i - 2]
            fib_numbers.append(next_fib)
        return fib_numbers[n]

# Example usage of the solution
result = function_with_uncommon_error_solution(35) #This will now run without stack overflow