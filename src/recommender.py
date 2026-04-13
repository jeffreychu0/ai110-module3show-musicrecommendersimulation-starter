from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        """Initialize recommender with a list of Song objects."""
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Score and rank songs against user profile, returning top K matches."""
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Generate human-readable explanation for why a song was recommended."""
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from CSV file and return as list of dictionaries with typed numeric fields."""
    songs = []
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert numeric fields to appropriate types
            song = {
                'id': int(row['id']),
                'title': row['title'],
                'artist': row['artist'],
                'genre': row['genre'],
                'mood': row['mood'],
                'energy': float(row['energy']),
                'tempo_bpm': float(row['tempo_bpm']),
                'valence': float(row['valence']),
                'danceability': float(row['danceability']),
                'acousticness': float(row['acousticness'])
            }
            songs.append(song)
        print(f"Loading songs from {csv_path}: {len(songs)} songs loaded.")

    return songs

def score_song(user_prefs: Dict, song: Dict) -> float:
    """Compute numerical score for song based on genre, mood, energy, and acousticness preferences."""
    score = 0.0

    # Genre match: +3 points
    if song['genre'].lower() == user_prefs['genre'].lower():
        score += 3

    # Mood match: +2 points
    if song['mood'].lower() == user_prefs['mood'].lower():
        score += 2

    # Energy similarity: +1 x (1 - difference)
    # Higher similarity (smaller difference) = higher score
    energy_similarity = 1 - abs(user_prefs['energy'] - song['energy'])
    score += energy_similarity

    # Acousticness bonus: +1 if user likes acoustic
    if user_prefs.get('likes_acoustic', False) and song['acousticness'] > 0.5:
        score += 1

    return score

def explain_song(user_prefs: Dict, song: Dict) -> str:
    """Generate human-readable explanation of which song attributes matched user preferences."""
    reasons = []

    if song['genre'].lower() == user_prefs['genre'].lower():
        reasons.append(f"Matches your {user_prefs['genre']} genre preference")

    if song['mood'].lower() == user_prefs['mood'].lower():
        reasons.append(f"Matches your {user_prefs['mood']} mood preference")

    energy_diff = abs(user_prefs['energy'] - song['energy'])
    if energy_diff < 0.2:
        reasons.append("Good energy level match")

    if user_prefs.get('likes_acoustic', False) and song['acousticness'] > 0.5:
        reasons.append("High acoustic quality (as you prefer)")

    return " • ".join(reasons) if reasons else "Song profile matched your preferences"

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score all songs, sort by score descending, and return top K as (song, score, explanation) tuples."""
    # Score all songs and create (song, score, explanation) tuples
    scored_songs = [
        (song, score_song(user_prefs, song), explain_song(user_prefs, song))
        for song in songs
    ]
    
    # Sort by score (descending) and return top k
    return sorted(scored_songs, key=lambda x: x[1], reverse=True)[:k]
