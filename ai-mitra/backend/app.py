from flask import Flask, request, jsonify
from ai_engine import analyze_text
from flask_cors import CORS 
from risk_analyzer import calculate_risk

app = Flask(__name__)
CORS(app) # Enable Cross-Origin Resource Sharing

@app.route('/api/analyze', methods=['POST'])

@app.route("/")
def home():
    return "AI Mitra Backend Running"


@app.route('/api/analyze', methods=['POST'])
@app.route('/api/analyse', methods=['POST'])
@app.route('/analyze', methods=['POST'])
@app.route('/analyse', methods=['POST'])

def analyze():
    """
    Main endpoint for AI Mitra. 
    Receives user message from the frontend, analyzes it, and returns the risk assessment.
    """
    data = request.json
    
    # Handle both 'message' and 'text' keys just in case the frontend changes it
    if not data:
        return jsonify({'error': 'No data provided in the request body.'}), 400
        
    user_message = data.get('message') or data.get('text')
    
    if not user_message:
        return jsonify({'error': 'No message provided.'}), 400

    score = analyze_text(user_text)
    risk = calculate_risk(score)

    return jsonify({
        "score": score,
        "risk_level": risk
    })


if __name__ == "__main__":
    app.run(debug=True)
