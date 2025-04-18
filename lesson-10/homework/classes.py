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

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False

    def transfer(self, target_account, amount):
        if self.withdraw(amount):
            target_account.deposit(amount)

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.number] = account

    def get_account(self, number):
        return self.accounts.get(number)

    def show_accounts(self):
        for acc in self.accounts.values():
            print(f"Account: {acc.number} | Holder: {acc.holder} | Balance: {acc.balance}")


# Hisoblar ochamiz
acc1 = Account("001", "Ali", 500)
acc2 = Account("002", "Vali", 300)

# Bank yaratamiz
my_bank = Bank()

# Hisoblarni qo‘shamiz
my_bank.add_account(acc1)
my_bank.add_account(acc2)

# Ali hisobiga yana 200 so‘m qo‘shamiz
acc1.deposit(200)

# Vali hisobidan 100 so‘m yechamiz
acc2.withdraw(100)

# Ali hisobidan Vali hisobiga 150 so‘m o‘tkazamiz
acc1.transfer(acc2, 150)

# Barcha hisoblarni ko‘rsatamiz
my_bank.show_accounts()
