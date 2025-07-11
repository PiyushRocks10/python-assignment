#positive negative or zero
num = float(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

#If-Else
# Simple Login System using if-else

correct_username = "admin"
correct_password = "12345"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("Login successful! Welcome,", username)
else:
    print("Login failed! Invalid username or password.")


#even numbers 1-20
# Program to print even numbers from 1 to 20

print("Even numbers from 1 to 20:")
for num in range(1, 21):
    if num % 2 == 0:
        print(num)
        
        
        
        #Factorial numbers
# Program to find the factorial of a number

num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0 or num == 1:
    print("The factorial of", num, "is 1.")
else:
    factorial = 1
    for i in range(2, num + 1):
        factorial *= i
    print("The factorial of", num, "is", factorial)


# Program to sum all numbers in a list using a while loop

numbers = [5, 10, 15, 20, 25]

i = 0
total = 0

while i < len(numbers):
    total += numbers[i]
    i += 1
print("The sum of all numbers in the list is:", total)
