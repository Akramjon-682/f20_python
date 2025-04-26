import threading
from collections import Counter
# import os

# # Tub son ekanligini tekshiruvchi funksiya
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# # Har bir thread uchun ishlaydigan funksiya
# def check_primes_in_range(start, end, result):
#     for number in range(start, end):
#         if is_prime(number):
#             result.append(number)

# # Asosiy funksiya
# def main():
#     start_range = 1
#     end_range = 100
#     num_threads = 4

#     threads = []
#     results = []

#     # Har bir thread o‘ziga natijalar ro‘yxatini yaratadi
#     thread_results = [[] for _ in range(num_threads)]

#     # Oraliqni bo‘lib chiqamiz
#     step = (end_range - start_range) // num_threads

#     for i in range(num_threads):
#         start = start_range + i * step
#         end = start + step if i < num_threads - 1 else end_range
#         thread = threading.Thread(target=check_primes_in_range, args=(start, end, thread_results[i]))
#         threads.append(thread)
#         thread.start()

#     # Barcha threadlar tugaguncha kutamiz
#     for thread in threads:
#         thread.join()

#     # Barcha natijalarni bitta ro‘yxatga birlashtiramiz
#     for r in thread_results:
#         results.extend(r)

#     print("Prime numbers:", sorted(results))

# if __name__ == "__main__":
#     main()


# Write a program that reads a large text file containing lines of text.
# Implement a threaded solution to count the occurrence of each word in the file. Each thread should process a portion of the file, 
# and the main program should display a summary of word occurrences across all threads.

# Shared list for thread results
results = []
lock = threading.Lock()

def process_lines(lines):
    word_count = Counter()
    for line in lines:
        words = line.strip().lower().split()
        word_count.update(words)

    with lock:
        results.append(word_count)


def main():
    filename = "sample.txt"
    threads = []
    chunk_size = 100  # number of lines per thread

    # Read all lines
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Create threads for chunks
    for i in range(0, len(lines), chunk_size):
        chunk = lines[i:i + chunk_size]
        thread = threading.Thread(target=process_lines, args=(chunk,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    # Aggregate results
    final_count = Counter()
    for counter in results:
        final_count.update(counter)

    # Print summary
    for word, count in final_count.most_common(10):  # Top 10 words
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()


