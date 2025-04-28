import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from classification import tracked_artists

#To run paste in terminal : cd (backend folder path here)
# and then streamlit run ui.py



# ========== AUTHENTICATION ==========
def authenticate_spotify():
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id="78e6a0058e734633b7a089734a361292",
        client_secret="687d40e1362a463a84ada8b73915a7fa"
    ))
    return sp

# ========== ANALYZE PLAYLIST ==========
def analyze_playlist(sp, playlist_link):
    playlist_id = playlist_link.split("/")[-1].split("?")[0]
    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']

    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])

    total_songs = len(tracks)
    loser_songs = 0
    special_messages = []

    for item in tracks:
        track = item['track']
        if track is not None:
            track_name = track['name'].lower()
            artists = [artist['name'].lower() for artist in track['artists']]

            for tracked_artist, artist_data in tracked_artists.items():
                if tracked_artist in artists:
                    if tracked_artist == "weezer": 
                        loser_songs += 1
                        
                    elif tracked_artist == "radiohead":
                        loser_songs += 1

                    for special_song, special_message in artist_data["special_songs"].items():
                        if special_song in track_name:
                            special_messages.append(special_message)

    return total_songs, loser_songs, special_messages

# ========== FUNNY DIAGNOSIS ==========
def funny_diagnosis(total_songs, loser_songs, special_messages):
    st.subheader("Special Songs Detected")
    if special_messages:
        for message in special_messages:
            st.write(f"- {message}")
    else:
        st.write("No special songs detected. You are safe... for now.")

    st.subheader("So do you?")
    
    if loser_songs >= 50:
        st.write("\nDiagnosis: You absolutely repell women.")
        
    elif loser_songs >= 40:
        st.write("\nDiagnosis: You havent talked to a woman in years have you??")
        
    elif loser_songs >= 30:
        st.write("\nDiagnosis: You once made eye contact with a woman and still havent forgotten them.")
        
    elif loser_songs >= 20:
        st.write("\nDiagnosis: You try to talk to women but end up scaring them away... aww :(.")
        
    elif loser_songs >= 10:
        st.write("\nDiagnosis: You think about texting women, but never do. You are a coward.")
        
    elif loser_songs >= 1:
        st.write("\nDiagnosis: You talk to women good job!")
    else:
        st.write("\nDiagnosis: You go outside and talk to women. Good Job!")


# ========== STREAMLIT UI ==========
def main():
    st.title("Do You Talk To Women?")

    playlist_link = st.text_input("Paste a Spotify playlist link here:")

    if st.button("Analyze Playlist"):
        if playlist_link:
            with st.spinner("Analyzing playlist..."):
                sp = authenticate_spotify()
                try:
                    total_songs, loser_songs, special_messages = analyze_playlist(sp, playlist_link)

                    st.write(f"Detected {loser_songs} Radiohead songs out of {total_songs} total songs.")
                    funny_diagnosis(total_songs, loser_songs, special_messages)

                except Exception as e:
                    st.error(f"Error analyzing playlist: {e}")
        else:
            st.error("Please paste a playlist link!")

if __name__ == "__main__":
    main()