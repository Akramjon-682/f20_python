import string
import os
import random
# # Exception Handling and File I/O Practice

# # 1. Handle ZeroDivisionError when dividing by zero
# try:
#     x = 10 / 0
# except ZeroDivisionError:
#     print("Cannot divide by zero!")

# # 2. Prompt for integer input and raise ValueError if input is invalid
# try:
#     num = int(input("Enter an integer: "))
# except ValueError:
#     print("Invalid input! Not an integer.")

# # 3. Open a file and handle FileNotFoundError
# try:
#     with open("nonexistent.txt") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("File not found.")

# # 4. Input two numbers and raise TypeError if inputs are not numerical
# try:
#     a = float(input("Enter first number: "))
#     b = float(input("Enter second number: "))
#     print(a + b)
# except ValueError:
#     print("Inputs must be numbers.")

# # 5. Open a file and handle PermissionError
# try:
#     with open("/root/secret.txt") as file:
#         print(file.read())
# except PermissionError:
#     print("Permission denied.")

# # 6. Handle IndexError when accessing list out of range
# try:
#     lst = [1, 2, 3]
#     print(lst[5])
# except IndexError:
#     print("Index out of range.")

# # 7. Handle KeyboardInterrupt during user input
# try:
#     user_input = input("Enter something: ")
# except KeyboardInterrupt:
#     print("\nInput cancelled by user.")

# # 8. Handle ArithmeticError during division
# try:
#     result = 10 / 0
# except ArithmeticError as e:
#     print("Arithmetic error:", e)

# # 9. Handle UnicodeDecodeError when reading file with encoding issues
# try:
#     with open("text.txt", encoding="ascii") as f:
#         print(f.read())
# except UnicodeDecodeError:
#     print("Encoding issue while reading file.")

# # 10. Handle AttributeError in list operation
# try:
#     my_list = [1, 2, 3]
#     my_list.upper()
# except AttributeError:
#     print("List has no attribute 'upper'.")

# # 11. Read an entire text file
# with open("sample.txt", "r") as f:
#     print(f.read())

# # 12. Read the first n lines of a file
# n = 3
# with open("sample.txt", "r") as f:
#     for _ in range(n):
#         print(f.readline().strip())

# # 13. Append text to a file and display it
# with open("sample.txt", "a") as f:
#     f.write("\nNew line appended.")
# with open("sample.txt", "r") as f:
#     print(f.read())

# # 14. Read the last n lines of a file
# n = 2
# with open("sample.txt", "r") as f:
#     lines = f.readlines()
#     print("".join(lines[-n:]))

# # 15. Read a file line by line and store in a list
# with open("sample.txt", "r") as f:
#     line_list = f.readlines()
# print(line_list)

# # 16. Read a file line by line and store in a variable
# with open("sample.txt", "r") as f:
#     content = f.read()
# print(content)

# # 17. Read a file line by line and store in an array
# with open("sample.txt", "r") as f:
#     arr = [line.strip() for line in f]
# print(arr)

# # 18. Find the longest word(s) in a file
# with open("sample.txt", "r") as f:
#     words = f.read().split()
#     longest = max(words, key=len)
#     print("Longest word:", longest)

# # 19. Count the number of lines in a file
# with open("sample.txt", "r") as f:
#     line_count = sum(1 for _ in f)
# print("Line count:", line_count)

# # 20. Count the frequency of words in a file
# from collections import Counter
# with open("sample.txt", "r") as f:
#     word_counts = Counter(f.read().split())
# print(word_counts)

# # 21. Get the file size of a plain text file

# print("File size:", os.path.getsize("sample.txt"), "bytes")

# # 22. Write a list to a file
# my_list = ["apple", "banana", "cherry"]
# with open("list.txt", "w") as f:
#     for item in my_list:
#         f.write(item + "\n")

# # 23. Copy contents of one file to another
# with open("sample.txt", "r") as src:
#     with open("copy.txt", "w") as dest:
#         dest.write(src.read())

# #  24. Combine each line from two files line by line
# with open("list.txt") as f1, open("sample.txt") as f2:
#     for l1, l2 in zip(f1, f2):
#         print(l1.strip() + " " + l2.strip())

# # 25. Read a random line from a file
# with open("sample.txt") as f:
#     lines = f.readlines()
#     print(random.choice(lines).strip())

# 26. Check if a file is closed or not
# f = open("sample.txt")
# print("Closed?", f.closed)
# f.close()
# print("Closed?", f.closed)

# # 27. Remove newline characters from a file
# with open("sample.txt") as f:
#     lines = [line.strip() for line in f]
# print(lines)

# # 28. Count the number of words in a file
# with open("sample.txt") as f:
#     text = f.read().replace(",", " ")
#     print("Word count:", len(text.split()))

# # 29. Extract characters from multiple files into a list
# chars = []
# for filename in ["sample.txt", "list.txt"]:
#     with open(filename) as f:
#         chars.extend(list(f.read()))
# print(chars)

# # 30. Generate 26 text files: A.txt to Z.txt
# import string
# for letter in string.ascii_uppercase:
#     with open(f"{letter}.txt", "w") as f:
#         f.write(f"This is file {letter}.txt\n")

# # 31. Create file with alphabet letters and N per line
# n = 13
# with open("alphabet.txt", "w") as f:
#     for i in range(0, 26, n):
#         f.write(" ".join(string.ascii_uppercase[i:i+n]) + "\n")
