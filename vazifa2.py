import random
import string



# # 1. Age Calculator
# name = input("Enter your name: ")
# birth_year = int(input("Enter your birth year: "))
# age = 2025 - birth_year
# print(f"{name}, you are {age} years old.")

# # 2. Extract Car Names (from scrambled string 'LMaasleitbtui')
# txt = 'LMaasleitbtui'
# car1 = txt[1:4]   # 'Mas'
# car2 = txt[5:9]   # 'leti' (rearranged could be 'Tesla' or similar, but unclear)
# print("Possible car names:", car1, car2)

# 3. Extract Car Names (from scrambled string 'MsaatmiazD')
# txt = 'AsaatmiazD'
# car = txt[0:3] + txt[-1]  # 'AsaD' (rearranged: 'Amsa' → maybe 'Datsun'?, not obvious)
# print("Possible car name:", car)

# # 4. Extract Residence Area
# txt = "I'am John. I am from London"
# area = txt.split("from")[-1].strip()
# print(f"Residence Area: {area} ")
# print(f"Residence Area:", area)


# # 5. Reverse String
# user_input = input("Enter a string: ")
# reversed_string = user_input[::-1]
# print("Reversed:", reversed_string)

# # 6. Count Vowels
vowels = 'aeiouAEIOU'
string = input("Enter a string: ")
# count = sum(1 for char in string if char in vowels)
c = sum(1 for t in string  if  t  in vowels )
print("Number of vowels:", c)

# # 7. Find Maximum Value
# numbers = list(map(int, input("Enter numbers separated by space: ").split()))
# maximum = max(numbers)
# print("Maximum value:", maximum)

# # 8. Check Palindrome
# word = input("Enter a word: ")
# if word == word[::-1]:
#     print("Palindrome")
# else:
#     print("Not a palindrome")

# # 9. Extract Email Domain
# email = input("Enter your email: ")
# domain = email.split("@")[-1]
# print("Domain:", domain)

# # 10. Generate Random Password

# length = int(input("Enter password length: "))
# characters = string.ascii_letters + string.digits + string.punctuation
# password = ''.join(random.choice(characters) for _ in range(length))
# print("Generated Password:", password)
