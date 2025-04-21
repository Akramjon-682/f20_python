import threading

# Tub son ekanligini tekshiruvchi funksiya
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Har bir thread uchun ishlaydigan funksiya
def check_primes_in_range(start, end, result):
    for number in range(start, end):
        if is_prime(number):
            result.append(number)

# Asosiy funksiya
def main():
    start_range = 1
    end_range = 100
    num_threads = 4

    threads = []
    results = []

    # Har bir thread o‘ziga natijalar ro‘yxatini yaratadi
    thread_results = [[] for _ in range(num_threads)]

    # Oraliqni bo‘lib chiqamiz
    step = (end_range - start_range) // num_threads

    for i in range(num_threads):
        start = start_range + i * step
        end = start + step if i < num_threads - 1 else end_range
        thread = threading.Thread(target=check_primes_in_range, args=(start, end, thread_results[i]))
        threads.append(thread)
        thread.start()

    # Barcha threadlar tugaguncha kutamiz
    for thread in threads:
        thread.join()

    # Barcha natijalarni bitta ro‘yxatga birlashtiramiz
    for r in thread_results:
        results.extend(r)

    print("Prime numbers:", sorted(results))

if __name__ == "__main__":
    main()
