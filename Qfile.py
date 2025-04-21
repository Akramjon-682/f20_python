# 📄 1. Fayl ochish rejimlari (mode)
# Mode	Tavsifi
# "r"	Faqat o‘qish uchun ochadi (fayl mavjud bo‘lishi kerak).
# "w"	Faqat yozish uchun ochadi (faylni tozalab yozadi yoki yangisini yaratadi).
# "a"	Qo‘shib yozish uchun ochadi (fayl mavjud bo‘lsa oxiridan yozadi, bo‘lmasa yangisini yaratadi).
# "x"	Faqat yangi fayl yaratish uchun (agar fayl mavjud bo‘lsa xatolik beradi).
# "r+"	O‘qish va yozish uchun (fayl mavjud bo‘lishi kerak).
# "w+"	O‘qish va yozish uchun (faylni tozalab yozadi yoki yangisini yaratadi).
# "a+"	O‘qish va qo‘shib yozish uchun (oxiriga yozadi, mavjud bo‘lmasa yaratadi).
# "b"	Binary rejim (rasm, video fayllar uchun: masalan, "rb").
# "t"	Matn rejimi (default: "rt" deb yozmasangiz ham bo‘ladi).
# 🧪 2. open() bilan ishlatiladigan funksiyalar:
# python
# Копировать
# Редактировать
# # 1. Faylga yozish
# with open("sample.txt", "w") as f:
#     f.write("Hello, world!\n")
#     f.write("Python file writing.\n")

# with open('sample.txt', "w") as f :
#     f.write("this is first txt file \n")

# # 2. Faylga qo‘shib yozish (append)
# with open("sample.txt", "a") as f:
#     f.write("Appending new line.\n")

# # 3. Fayldan o‘qish
# with open("sample.txt", "r") as f:
#     content = f.read()
#     print(content)

# # 4. Har bir qatordan o‘qish (ro‘yxat sifatida)
# with open("sample.txt", "r") as f:
#     lines = f.readlines()
#     for line in lines:
#         print(line.strip())

# # 5. Fayldan qatorma-qator o‘qish
# with open("sample.txt", "r") as f:
#     for line in f:
#         print(line.strip())

# # 6. Fayl mavjud bo‘lmasa yaratish (x mode)
# try:
#     with open("newfile.txt", "x") as f:
#         f.write("This is a new file.")
# except FileExistsError:
#     print("File already exists.")

# # 7. Binary fayl o‘qish
# with open("image.png", "rb") as f:
#     data = f.read()

# # 8. Binary faylga yozish
# with open("copy.png", "wb") as f:
#     f.write(data)
# 📚 3. Foydali funksiyalar (metodlar):
# Funksiya	Tavsifi
# f.read()	Butun faylni o‘qiydi.
# f.readline()	Fayldan bitta qatordan o‘qiydi.
# f.readlines()	Faylni qatorlarga ajratib, ro‘yxat sifatida o‘qiydi.
# f.write("text")	Matn yozadi.
# f.writelines(["a\n", "b\n"])	Ro‘yxatdagi barcha elementlarni yozadi.
# f.seek(n)	Fayldagi kursorni n baytga joylashtiradi.
# f.tell()	Kursorning hozirgi pozitsiyasini ko‘rsatadi.
# f.close()	Faylni yopadi (agar with open() ishlatilmasa).