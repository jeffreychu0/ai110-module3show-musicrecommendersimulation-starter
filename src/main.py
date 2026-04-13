"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    # Format and display recommendations
    print("\n" + "=" * 70)
    print("TOP 5 MUSIC RECOMMENDATIONS")
    print("=" * 70)
    print(f"\nUser Profile: {user_prefs['genre'].title()} genre, {user_prefs['mood'].title()} mood, Energy: {user_prefs['energy']}\n")

    for idx, rec in enumerate(recommendations, 1):
        song, score, explanation = rec
        print(f"{idx}. {song['title'].upper()}")
        print(f"   Artist: {song['artist']}")
        print(f"   Score: {score:.2f}")
        print(f"   Why: {explanation}")
        print()

    print("=" * 70)


if __name__ == "__main__":
    main()
