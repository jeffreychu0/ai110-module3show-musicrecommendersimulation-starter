"""
Command line runner for the Music Recommender Simulation.

Tests the recommender with multiple user profiles covering various preferences
and edge cases (high/low energy, different genres, mood preferences, etc.).
"""

from .recommender import load_songs, recommend_songs


# Define user profiles covering different preference combinations
USER_PROFILES = {
    "Pop Happy High Energy": {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.8,
        "likes_acoustic": False,
        "description": "Typical pop music fan - wants upbeat, happy songs"
    },

    "Chill Lofi Acoustic Lover": {
        "genre": "lofi",
        "mood": "chill",
        "energy": 0.3,
        "likes_acoustic": True,
        "description": "Low energy, relaxed listening with acoustic preferences"
    },

    "Intense Metal Rock Fan": {
        "genre": "metal",
        "mood": "intense",
        "energy": 0.95,
        "likes_acoustic": False,
        "description": "High energy aggressive music fan"
    },

    "Classical Peaceful Minimalist": {
        "genre": "classical",
        "mood": "peaceful",
        "energy": 0.25,
        "likes_acoustic": True,
        "description": "Very low energy, quiet, acoustic classical listener"
    },

    "Electronic Dark Energetic": {
        "genre": "electronic",
        "mood": "dark",
        "energy": 0.87,
        "likes_acoustic": False,
        "description": "Dark synth/electronic fan with high energy"
    }
}


def main() -> None:
    """Load songs and test recommender with multiple user profiles."""
    songs = load_songs("data/songs.csv")

    print("\n" + "=" * 90)
    print("MUSIC RECOMMENDER - TESTING MULTIPLE USER PROFILES")
    print("=" * 90)

    for profile_name, profile_data in USER_PROFILES.items():
        user_prefs = {
            "genre": profile_data["genre"],
            "mood": profile_data["mood"],
            "energy": profile_data["energy"],
            "likes_acoustic": profile_data["likes_acoustic"]
        }

        recommendations = recommend_songs(user_prefs, songs, k=5)

        print(f"\n{profile_name.upper()}")
        print(f"Description: {profile_data['description']}")
        print(f"Profile: {user_prefs['genre'].title()} | {user_prefs['mood'].title()} | Energy: {user_prefs['energy']} | Acoustic: {user_prefs['likes_acoustic']}")
        print("-" * 90)

        for idx, (song, score, explanation) in enumerate(recommendations, 1):
            print(f"  {idx}. {song['title']} by {song['artist']} (Score: {score:.2f})")
            print(f"     Why: {explanation}")

    print("\n" + "=" * 90)


if __name__ == "__main__":
    main()
