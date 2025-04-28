# string_utils.py
import string_utils

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

if __name__ == "__main__":

    n = string_utils.reverse_string("aksjfsasdf")
    m = string_utils.count_vowels("afsdfawerqwtasdfasqasfd")
    print(n)
    print(m)