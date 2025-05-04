
"""
This version of the playlist analyzer is based purely on GENRE matching.

Main Difference from Previous Version:
- Previous version: Focused on specific tracked artists (e.g., Radiohead, Weezer) and special songs (e.g., 'Creep', 'Undone').
- This version: Ignores specific artists and songs. 
  It only cares if an artist's Spotify genres overlap with a predefined set of 'sad' genres (bedroom pop, sad indie, shoegaze, etc).

Summary:
- No artist tracking.
- No special song detection.
- Only genre matching to detect the emotional vibe of the playlist.
- Diagnosis is still based on the number of loser (sad genre) songs detected.
"""

# --- IMPORTS ---
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import streamlit as st

#to run this code,type: cd (file path to backend folder here) and run the command: streamlit run alt_website.py into the terminal. 


# --- SAD/LOSER GENRES ---
loser_genres = {
    "bedroom pop", "sad indie", "indie rock", "art rock", "dream pop",
    "shoegaze", "melancholia", "lo-fi", "acoustic", "emo", "slowcore",
    "folk rock", "sadcore", "experimental rock"
}

# --- SPOTIPY AUTHENTICATION ---
def authenticate_spotify():
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id="YOUR_CLIENT_ID",
        client_secret="YOUR_CLIENT_SECRET"
    ))
    return sp

# --- ANALYZE PLAYLIST ---
def analyze_playlist(sp, playlist_link):
    playlist_id = playlist_link.split("/")[-1].split("?")[0]
    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']

    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])

    playlist_genre_pool = set()
    checked_artists = {}
    track_genre_map = {}

    for item in tracks:
        track = item['track']
        
        if track is not None and track.get('artists'):
            artists = track['artists']

            for artist in artists:
                artist_name = artist['name'].lower()
                artist_id = artist['id']

                # Fetch artist genres
                if artist_id and artist_id not in checked_artists:
                    try:
                        artist_info = sp.artist(artist_id)
                        artist_genres = set(artist_info.get("genres", []))
                        checked_artists[artist_id] = artist_genres
                    except:
                        artist_genres = set()
                else:
                    artist_genres = checked_artists.get(artist_id, set())

                playlist_genre_pool.update(artist_genres)
                track_genre_map[track['id']] = artist_genres

    # FINAL: Count songs with loser genres
    loser_song_count = 0
    for track_id, artist_genres in track_genre_map.items():
        if artist_genres & loser_genres:
            loser_song_count += 1

    return loser_song_count

# --- FUNNY LOSER DIAGNOSIS ---
def loser_song_diagnosis(loser_song_count):
    if loser_song_count >= 50:
        st.write("\nDiagnosis: You absolutely repel women.")
    elif loser_song_count >= 40:
        st.write("\nDiagnosis: You haven't talked to a woman in years have you??")
    elif loser_song_count >= 30:
        st.write("\nDiagnosis: You once made eye contact with a woman and still haven't forgotten them.")
    elif loser_song_count >= 20:
        st.write("\nDiagnosis: You try to talk to women but end up scaring them away... aww :(.")
    elif loser_song_count >= 10:
        st.write("\nDiagnosis: You think about texting women, but never do. You are a coward.")
    elif loser_song_count >= 5:
        st.write("\nDiagnosis: Hmmmmmmm..... I dunno, you are pushing it pal.")
    elif loser_song_count == 1:
        st.write("\nDiagnosis: Only one song, ok, you talk to women good job!")
    else:
        st.write("\nDiagnosis: 0 songs wow!! You go outside and talk to women!!! Good Job!")

# --- STREAMLIT UI ---
def main():
    st.title("Do You Talk to Women?")

    playlist_link = st.text_input("Enter your Spotify playlist link:")

    if st.button("Analyze Playlist"):
        if playlist_link:
            try:
                sp = authenticate_spotify()
                loser_song_count = analyze_playlist(sp, playlist_link)

                st.success(f"Total Sad/Loser Songs Detected: {loser_song_count}")
                loser_song_diagnosis(loser_song_count)

            except Exception as e:
                st.error(f"Error analyzing playlist: {e}")
        else:
            st.warning("Please enter a playlist link!")

if __name__ == "__main__":
    main()