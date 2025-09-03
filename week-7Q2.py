def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n_terms = 10
print(f"Fibonacci series up to {n_terms} terms:")
for i in range(n_terms):
    print(fibonacci(i), end=" ")
print()
