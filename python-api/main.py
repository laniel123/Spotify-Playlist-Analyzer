from flask import Flask, request, jsonify
from utils.spotify_api import analyze_playlist

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    playlist_link = data.get('playlist_link')
    if not playlist_link:
        return jsonify({"error": "Missing playlist_link"}), 400

    result = analyze_playlist(playlist_link)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)