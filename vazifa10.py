# Homework 1: ToDo List Application

# class Task:
#     def __init__(self, title, due_date, description="", status=False):
#         self.title = title
#         self.due_date = due_date
#         self.description = description
#         self.status = status  # False = bajarilmagan, True = bajarilgan

#     def mark_complete(self):
#         self.status = True


# class ToDoList:
#     def __init__(self):
#         self.tasks = []

#     def add_task(self, task):
#         self.tasks.append(task)
#         print(f"✅ VAZIFA qo‘shildi: {task.title}")

#     def list_tasks(self):
#         print("\n📋 BARCHA VAZIFALAR:")
#         for i, task in enumerate(self.tasks, 1):
#             status = "✅ Bajarilgan" if task.status else "❌ Bajarilmagan"
#             print(f"{i}. {task.title} (Tugash sanasi: {task.due_date}) → {status}")

#     def list_incomplete_tasks(self):
#         print("🔔 BAJARILMAGAN VAZIFALAR:")
#         for i, task in enumerate(self.tasks, 1):
#             if not task.status:
#                 print(f"{i}. {task.title} (Tugash sanasi: {task.due_date})
                      

# # ToDoList obyektini yaratamiz
# my_list = ToDoList()

# # Yangi vazifalar qo‘shamiz
# task1 = Task("Python darsini qilish", "2025-04-12")
# task2 = Task("Ingliz tili mashqi", "2025-04-13")
# task3 = Task("Matematika", "2025-04-15")

# my_list.add_task(task1)
# my_list.add_task(task2)
# my_list.add_task(task3)



# # 2-vazifani bajarilgan deb belgilang
# task2.mark_complete()

# # Barcha vazifalarni ko‘rsatamiz
# my_list.list_tasks()

# # Faqat bajarilmaganlarini ko‘rsatamiz
# my_list.list_incomplete_tasks()

# Homework 2: Simple Blog System

# class Post:
#     def __init__(self, title, content, author):
#         self.title = title
#         self.content = content
#         self.author = author

# class Blog:
#     def __init__(self):
#         self.posts = []

#     def add_post(self, post):
#         self.posts.append(post)

#     def list_posts(self):
#         for post in self.posts:
#             print(f"Title: {post.title} | Author: {post.author}")

#     def posts_by_author(self, author):
#         for post in self.posts:
#             if post.author == author:
#                 print(f"Title: {post.title} | Content: {post.content}")

#     def delete_post(self, title):
#         self.posts = [p for p in self.posts if p.title != title]

#     def edit_post(self, title, new_content):
#         for post in self.posts:
#             if post.title == title:
#                 post.content = new_content



# blog = Blog()

# # Yangi postlar
# post1 = Post("Python", "Python juda qulay til", "Ali")
# post2 = Post("Django", "Django bu web framework", "Ali")
# post3 = Post("PowerBI", "Bugun havo yaxshi", "Vali")

# # Qo‘shish
# blog.add_post(post1)
# blog.add_post(post2)
# blog.add_post(post3)

# # Barcha postlarni ko‘rish
# blog.list_posts()

# # Faqat Ali yozgan postlar
# print("\nAli yozgan postlar:")
# blog.posts_by_author("Ali")

# # Bittasini o‘chiramiz
# blog.delete_post("Django")

# # Tahrirlash
# blog.edit_post("Python", "Python tilini o‘rganish oson.")

# # Yana ro‘yxatni chiqarish
# print("\nTahrirdan keyin:")
# blog.list_posts()

# # Homework 3: Simple Banking System

class Account:
    def __init__(self, number, holder, balance=0):
        self.number = number
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"💰 {amount} so'm qo‘shildi. Yangi balans: {self.balance} so'm")

    def withdraw(self, amount):
        if amount > self.balance:
            print("❌ Yetarli mablag‘ mavjud emas!")
        else:
            self.balance -= amount
            print(f"💸 {amount} so'm yechildi. Yangi balans: {self.balance} so'm")

    def display(self):
        print(f"📄 Hisob raqami: {self.number}, Egasi: {self.holder}, Balans: {self.balance} so'm")


class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
        print("✅ Hisob muvaffaqiyatli yaratildi!")

    def find_account(self, number):
        for acc in self.accounts:
            if acc.number == number:
                return acc
        return None
 
    def transfer(self, from_acc, to_acc, amount):
        sender = self.find_account(from_acc)
        receiver = self.find_account(to_acc)

        if sender and receiver:
            if sender.balance >= amount:
                sender.balance -= amount
                receiver.balance += amount
                print(f"✅ {amount} so'm {from_acc} dan {to_acc} ga o‘tkazildi.")
            else:
                print("❌ Yetarli balans mavjud emas.")
        else:
            print("❌ Hisob raqami topilmadi.")


# 🖥 CLI INTERFACE
bank = Bank()

def main():
    while True:
        print("\n=== 🏦 BANKING SYSTEM MENU ===")
        print("1. Hisob qo‘shish")
        print("2. Balansni ko‘rish")
        print("3. Pul qo‘yish")
        print("4. Pul yechish")
        print("5. Pul o‘tkazish")
        print("6. Barcha hisoblarni ko‘rish")
        print("0. Chiqish")

        choice = input("👉 Tanlovingizni kiriting: ")

        if choice == "1":
            number = input("Hisob raqami: ")
            holder = input("Ism: ")
            account = Account(number, holder)
            bank.add_account(account)

        elif choice == "2":
            number = input("Hisob raqamini kiriting: ")
            acc = bank.find_account(number)
            if acc:
                acc.display()
            else:
                print("❌ Hisob topilmadi!")
   
        elif choice == "3": 
            number = input("Hisob raqami: ")
            amount = int(input("Miqdor: "))
            acc = bank.find_account(number)
            if acc:
                acc.deposit(amount)
            else:
                print("❌ Hisob topilmadi!")

        elif choice == "4":
            number = input("Hisob raqami: ")
            amount = int(input("Miqdor: "))
            acc = bank.find_account(number)
            if acc:
                acc.withdraw(amount)
            else:
                print("❌ Hisob topilmadi!")

        elif choice == "5":
            from_acc = input("Jo‘natuvchi hisob raqami: ")
            to_acc = input("Qabul qiluvchi hisob raqami: ")
            amount = int(input("Miqdor: "))
            bank.transfer(from_acc, to_acc, amount)

        elif choice == "6":
            print("\n📋 Barcha hisoblar:")
            for acc in bank.accounts:
                acc.display()

        elif choice == "0":
            print("👋 Dasturdan chiqildi.")
            break
        else:
            print("❌ Noto‘g‘ri tanlov. Qaytadan urinib ko‘ring.")

main()

