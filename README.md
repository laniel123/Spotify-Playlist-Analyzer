## Do You Talk To Women? 

Welcome to the ultimate self-diagnosis tool for Radiohead fans.

This app analyzes your Spotify playlist and jokingly tells you, based on your Radiohead song count, how likely you are to interact with women.


---

## Features

- Paste any Spotify playlist
- Detects how many Radiohead songs you have
- Special detection for various songs notable within the band's communities.
- Gives a humorous diagnosis about your social life
- Displays different images depending on how doomed you are

---

## How It Works

1. Paste your Spotify playlist link.
2. The app scans your songs.
3. Diagnoses your emotional well-being (and relationship prospects) based on Radiohead saturation.
4. Laugh. Cry. Make another sad playlist.

---

## Built With

- Python
- Streamlit
- Spotipy (Spotify API wrapper)

---
## Requirements

To run this project locally, follow these steps:

### 1. Install Python Packages

Install the required Python libraries using pip:

```bash
pip install spotipy streamlit
```

### 2. Set Up Spotify API Access

You will need a Spotify Developer account to access playlist and artist data.

1. Go to https://developer.spotify.com.
2. Log in and create an app.
3. Copy your **Client ID** and **Client Secret**.
4. In the Python code, replace the placeholders:

```python
client_id="YOUR_CLIENT_ID"
client_secret="YOUR_CLIENT_SECRET"
```

### 3. Run the App Locally

Run the Streamlit app within the terminal with:

```bash
cd (file path to backend folder here)
```

```bash
streamlit run yourfile.py
```
---

## Future Ideas

- Support for other artists (Weezer, Elliott Smith, The Smiths, etc.)
- Create a Java-based website.
- Dynamic memes
- Therapy resources link 

---

## License

This project is just for fun. Feel free to fork it, modify it, or stare blankly at it while "How to Disappear Completely" plays.
