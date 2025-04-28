import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# ========== AUTHENTICATION ==========
def authenticate_spotify():
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id="78e6a0058e734633b7a089734a361292",
        client_secret="687d40e1362a463a84ada8b73915a7fa"
    ))
    return sp

# ========== COUNT RADIOHEAD SONGS & DETECT SPECIAL SONGS ==========
def analyze_playlist(sp, playlist_link):
    playlist_id = playlist_link.split("/")[-1].split("?")[0]

    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']

    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])

    total_songs = len(tracks)
    radiohead_songs = 0
    special_songs_found = []

    for item in tracks:
        track = item['track']
        if track is not None:
            track_name = track['name'].lower()
            artists = [artist['name'].lower() for artist in track['artists']]

            if "radiohead" in artists:
                radiohead_songs += 1

            # Special Song Detection (Fuzzy match inside title)
            if "creep" in track_name and "radiohead" in artists:
                special_songs_found.append(track_name)
            if "exit music (for a film)" in track_name and "radiohead" in artists:
                special_songs_found.append(track_name)
            if "true love waits" in track_name and "radiohead" in artists:
                special_songs_found.append(track_name)

    return total_songs, radiohead_songs, special_songs_found

# ========== DIAGNOSIS BASED ON RADIOHEAD % ==========
def funny_diagnosis(playlist_name, total_songs, radiohead_songs, special_songs_found):
    print(f"\n📜 Playlist Analysis for '{playlist_name}' 📜")
    print(f"Total Songs: {total_songs}")
    print(f"Radiohead Songs: {radiohead_songs}")

    if total_songs == 0:
        print("\nDiagnosis: Empty playlist detected. Please seek help.")
        return

    radiohead_percentage = (radiohead_songs / total_songs) * 100

    # LOWERCASE the detected special songs
    lowercase_specials = [song.lower() for song in special_songs_found]

    # YOUR CUSTOM PRINTS (unchanged)
    if "creep" in lowercase_specials:
        print("\nWe Detected Creep. Therapy is recommended.")
    if "exit music (for a film)" in lowercase_specials:
        print("\nDetected 'Exit Music (for a Film)'. Immediate hug required.")
    if "true love waits" in lowercase_specials:
        print("\nWe Detected True Love Waits. Do you need a hug??")
    if "true love waits-live in oslo" in lowercase_specials:
        print("\nWe Detected True Love Waits... LIVE IN OSLO??. Do you need a hug?? Like really.. do you need a hug??")

    if not special_songs_found:
        print("\nNo special songs detected. You are safe ... for now.")

    # Normal Radiohead percentage diagnosis
    if radiohead_percentage >= 90:
        print("\nDiagnosis: You repell women.'")
    elif radiohead_percentage >= 70:
        print("\nDiagnosis: You try to talk to women but they find you offputting")
    elif radiohead_percentage >= 40:
        print("\nDiagnosis: You sometimes think about texting her but end up just listening to 'How to Disappear Completely.'")
    elif radiohead_percentage >= 10:
        print("\nDiagnosis: You go outside. Good job :D ")
    else:
        print("\nDiagnosis: You're surprisingly well adjusted. Are you sure you even listen to Radiohead?")

# ========== MAIN ==========
def main():
    sp = authenticate_spotify()

    playlist_link = input("\nPaste a Spotify playlist link to analyze: ")

    playlist_id = playlist_link.split("/")[-1].split("?")[0]
    playlist_info = sp.playlist(playlist_id)
    playlist_name = playlist_info['name']

    total_songs, radiohead_songs, special_songs_found = analyze_playlist(sp, playlist_link)

    funny_diagnosis(playlist_name, total_songs, radiohead_songs, special_songs_found)

# Run it
if __name__ == "__main__":
    main()