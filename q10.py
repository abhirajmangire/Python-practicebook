#ask user to enter names to their 3 favorite movies and store them in a list
movies = []

for i in range(3):
    movie = input("Enter your favorite movies: ")
    movies.append(movie)
print("Your fav movires are",movies)
