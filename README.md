# Spotify Playlist Analyzer

**Spotify Playlist Analyzer** (also known as **“Do You Go Outside?”**) is a full-stack web application that evaluates one's Spotify playlists by analyzing the presence of emotionally introspective artists such as Radiohead and Weezer. While framed around inside jokes based on the two bands' communities, the app demonstrates skills in API integration, frontend design, and Flask-based backend development.

This project creatively uses music data to engage users through interactive analysis, multimedia feedback, and a responsive interface.

---

## Website Demo 

[![Watch the demo](https://img.youtube.com/vi/zjIqYCqgvKw/0.jpg)](https://youtu.be/zjIqYCqgvKw)]

---

## Features

- Accepts public Spotify playlist URLs
- Parses and counts songs by selected artists
- Recognizes key tracks and returns custom messages
- Displays a lighthearted “diagnosis” based on emotional tone
- Includes sound and animation effects for user feedback
- Fully responsive frontend with gradient animation and hover effects

---

## Tech Stack

**Frontend**
- HTML5, CSS3, JavaScript  
- Responsive design with animation and user feedback

**Backend**
- Python 3  
- Flask (REST API)  
- Spotipy (Spotify Web API wrapper)  
- Flask-CORS

---

##  Installation

### 1 Clone the Repository

```bash
git clone https://github.com/laniel123/Spotify-Playlist-Analyzer.git
cd Spotify-Playlist-Analyzer
```

### 2 Set Up Spotify Developer Credentials

1. Go to https://developer.spotify.com
2. Create an application and retrieve your **Client ID** and **Client Secret**
3. Replace the values in `main.py`:

```python
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
```
---

## Local Development Instructions

To run the project locally, follow the steps below.

### 1 Backend Setup

Navigate to the backend directory:

```bash
cd python_api
```

Install the necessary dependencies:

```bash
pip install -r requirements.txt
```

(Optional) Save the installed dependencies for future use:

```bash
pip freeze > requirements.txt
```

Start the Flask backend server:

```bash
python3 main.py
```

---

### 2 Frontend Setup

Navigate to the frontend directory:

```bash
cd ../frontend
```

(Optional) Serve the frontend locally with Python:

```bash
python3 -m http.server 8000
```

Then open your browser and go to:

```
http://localhost:8000
```

---

### Optional: Favicon Warning Fix

If you'd like to remove the missing favicon warning in the browser console, you can create a dummy icon file:

```bash
touch frontend/favicon.ico
```

---

##  Project Structure

- `python_api/` – Flask backend that processes playlist data using the Spotify API
- `frontend/` – Static HTML/CSS/JavaScript frontend served locally in the browser
- `css/` – Styling for the app interface (within frontend)
- `js/` – JavaScript logic for making API calls and UI interaction
- `images/` – App logos or images
- `sounds/` – Audio files 
- `index.html` – Main frontend page rendered in browser
- `main.py` – Python Flask application that powers the backend
- `requirements.txt` – Python dependencies used in the backend

---

##  Future Enhancements

- Add OAuth authentication for private playlist access
- Improved CSS styles 
- Expand artist recognition 
- Deploy to the web (frontend + backend)
- Add shareable results cards or memes

---

##  License

This project is licensed under the [MIT License](LICENSE.txt).
