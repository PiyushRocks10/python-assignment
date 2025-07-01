  #Lambda functions

students = [("ABC", 25), ("LMN", 20), ("PQR", 23), ("XYZ", 22)]

sorted_students = sorted(students, key=lambda x: x[1])

print("Students sorted by age:")
for student in sorted_students:
    print(student)

    #even numbers in lambda function
     
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Even numbers :", even_numbers)

#map of square

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x ** 2, numbers))

print("Squares of the list:", squares)

