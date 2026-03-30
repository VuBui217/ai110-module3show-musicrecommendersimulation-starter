"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Starter example profile
    user_prefs = {"favorite_genre": "rock", "favorite_mood": "intense", "target_energy": 0.8, "likes_acoustic": False}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n" + "=" * 50)
    print("  TOP RECOMMENDATIONS")
    print("=" * 50)
    for i, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n#{i}  {song['title']}  —  {song['artist']}")
        print(f"    Genre: {song['genre']}  |  Mood: {song['mood']}  |  Energy: {song['energy']:.2f}")
        print(f"    Score: {score:.2f} / 5.00")
        reason_text = explanation.split(": ", 1)[-1] if ": " in explanation else explanation
        print(f"    Why:   {reason_text}")
    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()
