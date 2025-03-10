# An implementation of the Fibonacci algorithm using a for loop.
print("\nAn implementation of the Fibonacci algorithm using a for loop.\n")

prev2 = 0
prev1 = 1

print(prev2)
print(prev1)
for fibo in range(18):
    newFibo = prev1 + prev2
    print(newFibo)
    prev2 = prev1
    prev1 = newFibo


# An implementation of the Fibonacci algorithm using recursion
print("\nAn implementation of the Fibonacci algorithm using recursion.\n")

print(0)
print(1)
count = 2

def fibonacci(prev1, prev2):
    global count
    if count <= 19:
        newFibo = prev1 + prev2
        print(newFibo)
        prev2 = prev1
        prev1 = newFibo
        count += 1
        fibonacci(prev1, prev2)
    else:
        return

fibonacci(1,0)

# Finding the nth Fibonacci number using recursion.
print("\nFinding the nth Fibonacci number using recursion.")
def F(n):
    if n <= 1:
        return n
    else:
        return F(n - 1) + F(n - 2)

print(F(19))