def factorial(n):
    if n==0 or n==1:
        return 1
    elif n<0:
        print("Enter valid input")
    else:
        return n*factorial(n-1)

num =int(input("Enter a no.: "))
print(f"The factorial of {num} is: {factorial(num)}")