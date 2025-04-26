from datetime import datetime, timedelta
import time
import re

199
# 1. Age Calculator
# birth_date = datetime.strptime(input("Enter your birthdate (YYYY-MM-DD): "), "%Y-%m-%d")
# today = datetime.today()
# age_days = (today - birth_date).days
# age_years = age_days // 365
# age_months = (age_days % 365) // 30
# age_days = (age_days % 365) % 30
# print(f"You are {age_years} years, {age_months} months, and {age_days} days old.")

# # 2. Days Until Next Birthday
# next_birthday = datetime(today.year, birth_date.month, birth_date.day)
# if next_birthday < today:
#     next_birthday = datetime(today.year + 1, birth_date.month, birth_date.day)
# days_left = (next_birthday - today).days
# print(f"Days until next birthday: {days_left}")

# 3. Meeting Scheduler
# current_time = datetime.strptime(input("Enter current date and time (YYYY-MM-DD HH:MM): "), "%Y-%m-%d %H:%M")
# hours = int(input("Enter meeting duration hours: "))
# minutes = int(input("Enter meeting duration minutes: "))
# end_time = current_time + timedelta(hours=hours, minutes=minutes)
# print(f"Meeting will end at: {end_time.strftime('%Y-%m-%d %H:%M')}")

# # 4. Timezone Converter (simple version without real timezone lib)
# current_dt = datetime.strptime(input("Enter date and time (YYYY-MM-DD HH:MM): "), "%Y-%m-%d %H:%M")
# current_offset = int(input("Enter your timezone offset from UTC (e.g., +5, -3): "))
# target_offset = int(input("Enter target timezone offset from UTC: "))
# time_difference = timedelta(hours=target_offset - current_offset)
# converted_dt = current_dt + time_difference
# print(f"Converted date and time: {converted_dt.strftime('%Y-%m-%d %H:%M')}")

# # 5. Countdown Timer
# future_time = datetime.strptime(input("Enter future date and time (YYYY-MM-DD HH:MM): "), "%Y-%m-%d %H:%M")
# while True:
#     now = datetime.now()
#     if future_time <= now:
#         print("Countdown complete!")
#         break
#     remaining = future_time - now
#     print(f"Time left: {remaining}")
#     time.sleep(1)

# # 6. Email Validator
# email = input("Enter an email address: ")
# pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$'
# if re.match(pattern, email):
#     print("Valid email address.")
# else:
#     print("Invalid email address.")

# # 7. Phone Number Formatter
# number = input("Enter a 10-digit phone number: ")
# if len(number) == 10 and number.isdigit():
#     formatted = f"({number[:3]}) {number[3:6]}-{number[6:]}"
#     print(f"Formatted number: {formatted}")
# else:
#     print("Invalid phone number.")

# # 8. Password Strength Checker
# password = input("Enter a password: ")
# if (len(password) >= 8 and
#     any(c.isupper() for c in password) and
#     any(c.islower() for c in password) and
#     any(c.isdigit() for c in password)):
#     print("Strong password.")
# else:
#     print("Weak password.")

# # 9. Word Finder
# text = "This is a simple sample text for testing. Sample words are here."
# word_to_find = input("Enter word to find: ").lower()
# words = text.lower().split()
# found = [i for i, w in enumerate(words) if w == word_to_find]
# print(f"Word '{word_to_find}' found at positions: {found}")

# # 10. Date Extractor
sample_text = input("Enter text containing dates: ")
date_pattern = r'\\b\\d{4}-\\d{2}-\\d{2}\\b'
dates = re.findall(date_pattern, sample_text)
print(f"Dates found: {dates}")
