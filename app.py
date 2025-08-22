from flask import Flask, request, jsonify
from textblob import TextBlob
from flask_cors import CORS

app = Flask(__name__)
# For first test, allow all origins. Later, restrict to your domain:
# CORS(app, resources={r"/sentiment": {"origins": "https://YOUR-DOMAIN"}})
CORS(app)

@app.route('/sentiment', methods=['POST'])
def sentiment():
    data = request.get_json(silent=True) or {}
    text = data.get('comment', '').strip()
    if not text:
        return jsonify({'error': 'No comment provided'}), 400

    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0.1:
        senti = 'Positive'
    elif polarity < -0.1:
        senti = 'Negative'
    else:
        senti = 'Neutral'
    return jsonify({'sentiment': senti})

# No need to call app.run() in production; Render will use gunicorn.
