# Fibonacci numbers module
# Recursion practice.

def fib(n):
	a, b = 0, 1
	while b < n:
		print(b)
                # Pythonic way to reassign a and b to their new values
		a, b = b, a+b

