import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# ========== AUTHENTICATION ==========
def authenticate_spotify():
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id="78e6a0058e734633b7a089734a361292",
        client_secret="687d40e1362a463a84ada8b73915a7fa"
    ))
    return sp

# ========== COUNT RADIOHEAD SONGS ==========
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

            # Special Song Detection
            if "creep" in track_name and "radiohead" in artists:
                special_songs_found.append(track_name)
            if "exit music (for a film)" in track_name and "radiohead" in artists:
                special_songs_found.append(track_name)
            if "true love waits" in track_name and "radiohead" in artists:
                special_songs_found.append(track_name)

    return total_songs, radiohead_songs, special_songs_found

# ========== FUNNY DIAGNOSIS BASED ON RADIOHEAD SONG COUNT ==========
def funny_diagnosis(total_songs, radiohead_songs, special_songs_found):
    lowercase_specials = [song.lower() for song in special_songs_found]

    if "creep" in lowercase_specials:
        st.write("\nWe Detected Creep. Therapy is recommended.")

    if "exit music (for a film)" in lowercase_specials:
        st.write("\nDetected Exit Music (for a Film). Im sorry you are hurting man....")

    if "true love waits" in lowercase_specials:
        st.write("\nWe Detected True Love Waits. Do you need a hug??")
        
    if "true love waits - live in oslo" in lowercase_specials:
        st.write("\nWe Detected True Love Waits... LIVE IN OSLO??. Do you need a hug?? Like really.. do you need a hug??")

    if not special_songs_found:
        st.write("\nNo special songs detected. You are safe ... for now.")

    # Diagnosis based on TOTAL radiohead songs (NOT talk score)

    if radiohead_songs >= 50:
        st.write("\nDiagnosis: You absolutely repell women.")
    elif radiohead_songs >= 40:
        st.write("\nDiagnosis: You havent talked to a woman in years have you??")
    elif radiohead_songs >= 30:
        st.write("\nDiagnosis: You once made eye contact with a woman... and wrote 3 sad playlists about it.")
    elif radiohead_songs >= 20:
        st.write("\nDiagnosis: You try to talk to women but end up scaring them away... aww.")
    elif radiohead_songs >= 10:
        st.write("\nDiagnosis: You think about texting women, but Radiohead is louder than your hope.")
    elif radiohead_songs >= 1:
        st.write("\nDiagnosis: You talk to women good job!")
    else:
        st.write("\nDiagnosis: You're surprisingly well-adjusted. Touch grass maybe?")

# ========== STREAMLIT UI ==========
def main():
    st.title("Do You Talk To Women?")

    playlist_link = st.text_input("Paste a Spotify playlist link here:")

    if st.button("Analyze Playlist"):
        if playlist_link:
            sp = authenticate_spotify()
            try:
                total_songs, radiohead_songs, special_songs_found = analyze_playlist(sp, playlist_link)

                st.write(f"\nDetected {radiohead_songs} Radiohead songs out of {total_songs} total songs.")
                st.write('-----------------------')
                funny_diagnosis(total_songs, radiohead_songs, special_songs_found)

            except Exception as e:
                st.error(f"Error analyzing playlist: {e}")
        else:
            st.error("Please paste a playlist link!")

if __name__ == "__main__":
    main()