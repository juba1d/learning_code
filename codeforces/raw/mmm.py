t = int(input())

for _ in range(t):
    n = int(input())
    first_movie_reviews = list(map(int, input().split()))
    second_movie_reviews = list(map(int, input().split()))
    
    rating_first_movie = sum(first_movie_reviews)
    rating_second_movie = sum(second_movie_reviews)
    
    print(max(rating_first_movie, rating_second_movie))
