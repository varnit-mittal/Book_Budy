import transformers

from transformers import pipeline

def recommend_genres_for_movie(movie_title):
    nlp = pipeline("zero-shot-classification",model='roberta-large-mnli')

    genres = ["Action", "Comedy", "Drama", "Horror", "Romance", "Science Fiction"]

    # Provide a prompt that includes the movie title and the available genres.
    prompt = f"Which genre does the movie '{movie_title}' belong to: {', '.join(genres)}?"

    # Get the zero-shot classification result to predict the genre.
    genre_result = nlp(prompt, genres)

    # Extract the genre with the highest score (predicted probability).
    recommended_genre = genre_result["labels"][0]

    return recommended_genre

def main():
    print("Welcome to the Movie Genre Recommender!")
    movie_title = input("Enter the movie title: ")

    recommended_genre = recommend_genres_for_movie(movie_title)

    print(f"\nThe recommended genre for the movie '{movie_title}' is: {recommended_genre}")

if __name__ == "__main__":
    main()
