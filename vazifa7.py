# 1. is_prime(n) funksiyasi
# n soni tub bo‘lsa True, aks holda False qaytarsin.
# m = int(input(' funksiyasiga son kiriting : '))
# def isprime(n):
#     if n <=1 :
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True

# # Test:
# print("1. is_prime:")

# print(isprime(m))  # True


# 2. digit_sum(k) funksiyasi
# # k sonining raqamlari yig'indisini hisoblaydi.
# def digit_sum(k):
#     return sum(int(digit) for digit in str(k))

# # Test:
# print("\n2. digit_sum:")
# print(digit_sum(24))   # 6
# print(digit_sum(502))  # 7


 
# # 4. map va filter funksiyalari bilan lambda misollar:

# # map - har bir elementni 2 ga ko‘paytirish:
# numbers = [1, 2, 3, 4, 5]
# doubled = list(map(lambda x: x * 2, numbers))
# print("\n4. map example (x2):", doubled)

# # filter - faqat juft sonlarni olish:
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print("4. filter example (even numbers):", even_numbers)
