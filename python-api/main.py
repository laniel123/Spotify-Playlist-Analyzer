from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from utils.spotify_api import analyze_playlist  # ✅ update path if needed

app = Flask(__name__)
CORS(app)

@app.route('/analyze', methods=['POST', 'OPTIONS'])
def analyze():
    # Handle CORS preflight (OPTIONS)
    if request.method == 'OPTIONS':
        print("DEBUG: Received OPTIONS preflight request")
        response = make_response()
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add("Access-Control-Allow-Headers", "Content-Type")
        response.headers.add("Access-Control-Allow-Methods", "POST")
        return response

    # Handle POST request
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