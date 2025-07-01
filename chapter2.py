# Program to create a list of 5 favorite movies

favorite_movies = ["Pokemon", "Doraemon", "Tom&jerry", "Avengers: Endgame", "Power rangers"]

print("My 5 favorite movies are:")
for movie in favorite_movies:
    print("-", movie)



# Program to create a dictionary with keys: name, age, course

student = {
    "name": "Piyush",
    "age": 21,
    "course": "Full stack Python"
}

print("Student Profile:")
print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])



# Program to add and remove items from a set

fruits = {"apple", "banana", "cherry"}

fruits.add("orange")
print("After adding 'orange':", fruits)

fruits.remove("banana")
print("After removing 'banana':", fruits)

fruits.discard("grape")
print("After discarding 'grape':", fruits)



# Program to sort a list of numbers

numbers = [5, 2, 9, 1, 7, 3]
numbers.sort()

print("Sorted list in ascending order:", numbers)

numbers.sort(reverse=True)
print("Sorted list in descending order:", numbers)



# Program to loop through a dictionary and print key-value pairs

student = {
    "name": "Deepak",
    "age": 21,
    "course": "Full stack Java"
}

print("Student Details:")
for key, value in student.items():
    print(f"{key}: {value}")



