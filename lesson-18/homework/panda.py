import pandas as pd

# Homework 2 - StackOverflow QA dataset
df = pd.read_csv('task\\stackoverflow_qa.csv')

# 1. Find all questions that were created before 2014
q1 = df[df['creationdate'] < '2014-01-01']

# 2. Find all questions with a score more than 50
q2 = df[df['score'] > 50]

# 3. Find all questions with a score between 50 and 100
q3 = df[(df['score'] >= 50) & (df['score'] <= 100)]

# 4. Find all questions answered by Scott Boston
q4 = df[df['ans_name'] == 'Scott Boston']

# 5. Find all questions answered by the following 5 users
users = ['unutbu', 'jezrael', 'MaxU', 'Scott Boston', 'Wen']
q5 = df[df['ans_name'].isin(users)]

# 6. Find all questions created between March 2014 and October 2014, answered by Unutbu, score < 5
q6 = df[
    (df['creationdate'] >= '2014-03-01') &
    (df['creationdate'] <= '2014-10-31') &
    (df['ans_name'] == 'unutbu') &
    (df['score'] < 5)
]

# 7. Find all questions with score between 5 and 10 or view count greater than 10,000
q7 = df[(df['score'].between(5, 10)) | (df['viewcount'] > 10000)]

# 8. Find all questions NOT answered by Scott Boston
q8 = df[df['ans_name'] != 'Scott Boston']

# ===============================================================

# Homework 3 - Titanic dataset
titanic_df = pd.read_csv('task\\titanic.csv')

# 1. Select Female Passengers in Class 1 with Ages between 20 and 30
h3_q1 = titanic_df[
    (titanic_df['Sex'] == 'female') &
    (titanic_df['Pclass'] == 1) &
    (titanic_df['Age'].between(20, 30))
]

# 2. Filter Passengers Who Paid More than $100
h3_q2 = titanic_df[titanic_df['Fare'] > 100]

# 3. Select Passengers Who Survived and Were Alone
h3_q3 = titanic_df[
    (titanic_df['Survived'] == 1) &
    (titanic_df['SibSp'] == 0) &
    (titanic_df['Parch'] == 0)
]

# 4. Filter Passengers Embarked from 'C' and Paid More Than $50
h3_q4 = titanic_df[
    (titanic_df['Embarked'] == 'C') &
    (titanic_df['Fare'] > 50)
]

# 5. Select Passengers with Siblings or Spouses and Parents or Children
h3_q5 = titanic_df[
    (titanic_df['SibSp'] > 0) &
    (titanic_df['Parch'] > 0)
]

# 6. Filter Passengers Aged 15 or Younger Who Didn't Survive
h3_q6 = titanic_df[
    (titanic_df['Age'] <= 15) &
    (titanic_df['Survived'] == 0)
]

# 7. Select Passengers with Cabins and Fare Greater Than $200
h3_q7 = titanic_df[
    (titanic_df['Cabin'].notnull()) &
    (titanic_df['Fare'] > 200)
]

# 8. Filter Passengers with Odd-Numbered Passenger IDs
h3_q8 = titanic_df[titanic_df['PassengerId'] % 2 != 0]

# 9. Select Passengers with Unique Ticket Numbers
h3_q9 = titanic_df[titanic_df.duplicated('Ticket', keep=False) == False]

# 10. Filter Passengers with 'Miss' in Their Name and Were in Class 1
h3_q10 = titanic_df[
    (titanic_df['Name'].str.contains('Miss')) &
    (titanic_df['Pclass'] == 1)
]
