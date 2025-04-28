# Task 1: JSON Parsing - Read and print student details from 'students.json'
import json
import requests
import random

# Reading and printing student details
# try:
#     with open('students.json', 'r') as file:
#         students = json.load(file)
#         print("Student Details:")
#         for student in students:
#             print(f"Name: {student.get('name')}, Age: {student.get('age')}, Grade: {student.get('grade')}")
# except FileNotFoundError:
#     print("students.json file not found.")

# # Task 2: Weather API - Fetch and display weather data for Tashkent
# def get_weather(city):
#     api_key = 'my_api_key_here'  # Replace with your OpenWeatherMap API key
#     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
#     try:
#         response = requests.get(url)
#         data = response.json()
#         if response.status_code == 200:
#             print(f"\nWeather in {city}:")
#             print(f"Temperature: {data['main']['temp']}°C")
#             print(f"Humidity: {data['main']['humidity']}%")
#             print(f"Description: {data['weather'][0]['description']}")
#         else:
#             print(f"Error fetching weather data: {data.get('message', 'Unknown error')}")
#     except requests.exceptions.RequestException as e:
#         print(f"Request error: {e}")

# get_weather("Tashkent")

# Task 3: JSON Modification - Add, update, and delete books in 'books.json'
def modify_books():
    try:
        with open('books.json', 'r') as file:
            books = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        books = []

    # Add a new book
    new_book = {"title": "New Book", "author": "Author Name"}
    books.append(new_book)

    # Update an existing book
    for book in books:
        if book.get('title') == "Old Book Title":
            book['author'] = "Updated Author"

    # Delete a book
    books = [book for book in books if book.get('title') != "Book to Delete"]

    # Write changes back to the file
    with open('books.json', 'w') as file:
        json.dump(books, file, indent=4)

    print("\nUpdated books.json file.")

modify_books()

# Task 4: Movie Recommendation System - Recommend a random movie by genre
def recommend_movie(genre):
    api_key = 'my_api_key_here'  # Replace with your OMDb API key
    url = f"http://www.omdbapi.com/?apikey={api_key}&type=movie&s={genre}"
    try:
        response = requests.get(url)
        data = response.json()
        if data.get('Response') == 'True':
            movies = data.get('Search', [])
            if movies:
                movie = random.choice(movies)
                print(f"\nRecommended {genre} Movie:")
                print(f"Title: {movie.get('Title')}")
                print(f"Year: {movie.get('Year')}")
                print(f"IMDb ID: {movie.get('imdbID')}")
            else:
                print(f"No movies found for genre: {genre}")
        else:
            print(f"Error fetching movies: {data.get('Error')}")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")

recommend_movie("Action")
