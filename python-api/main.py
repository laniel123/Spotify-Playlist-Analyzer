from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.spotify_api import analyze_playlist  # update path if needed


app = Flask(__name__)
CORS(app)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    print("DEBUG: Received data:", data)

    playlist_link = data.get('playlist_link')
    print("DEBUG: Playlist link:", playlist_link)

    if not playlist_link:
        print("ERROR: Missing playlist link!")
        return jsonify({"error": "Missing playlist_link"}), 400

    try:
        result = analyze_playlist(playlist_link)
        print("DEBUG: Analysis result:", result)
        return jsonify(result)
    except Exception as e:
        print("ERROR during analysis:", str(e))
        return jsonify({"error": "Server error", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)