from flask import Flask, request, jsonify
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from classification import tracked_artists, artist_class   # ✅ KEEP if you have these files

app = Flask(__name__)

# ========== AUTHENTICATE ==========
def authenticate_spotify():
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id="78e6a0058e734633b7a089734a361292",      # ✏️ EDIT: your CLIENT ID
        client_secret="687d40e1362a463a84ada8b73915a7fa"   # ✏️ EDIT: your CLIENT SECRET
    ))
    return sp

def analyze_playlist(sp, playlist_link):
    playlist_id = playlist_link.split("/")[-1].split("?")[0]
    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']

    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])

    total_songs = len(tracks)
    radiohead_songs = 0
    weezer_songs = 0
    loser_songs = 0
    special_messages = []

    for item in tracks:
        track = item['track']
        if track is not None and track.get('name') and track.get('artists'):
            track_name = track['name'].lower()
            artists = [artist['name'].lower() for artist in track['artists'] if artist.get('name')]

            for tracked_artist, artist_data in tracked_artists.items():   # ✅ KEEP (matches your current logic)
                if tracked_artist in artists:
                    if tracked_artist in artist_class:                  # ✅ KEEP
                        loser_songs += 1

                    if tracked_artist == "radiohead":
                        radiohead_songs += 1
                    if tracked_artist == "weezer":
                        weezer_songs += 1

                    # Special songs detection
                    for special_song, special_message in artist_data["special_songs"].items():
                        if special_song in track_name:
                            special_messages.append(special_message)

    return {
        "total_songs": total_songs,
        "radiohead_songs": radiohead_songs,
        "weezer_songs": weezer_songs,
        "loser_songs": loser_songs,
        "special_messages": special_messages
    }
    
@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    playlist_link = data.get('playlist_link')    # ✅ KEEP

    if not playlist_link:
        return jsonify({"error": "Missing playlist_link"}), 400

    sp = authenticate_spotify()
    result = analyze_playlist(sp, playlist_link)
    return jsonify(result) 