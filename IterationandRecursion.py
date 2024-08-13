#Jacklyn Meiers, CIS261, Iteration and Recursion

#Part ! Iterative Function

def factorial_iterative(n):
    result = 1
    for i in range(2, n +1):
        result *= i
    return result

#Part 2 Recursive Function
def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

test_numbers = [0, 5, 10, 25, 50, 100]
print("Iterative Factorial Result:")
for number in test_numbers:
    print(f"{number}! = {factorial_iterative(number)} ")


    
print("Recursive Factorial Results: ")
for number in test_numbers:
    print(f"{number}! = {factorial_recursive(number)} ")

    