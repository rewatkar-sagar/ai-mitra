from flask import Flask, request, jsonify
from ai_engine import analyze_text
from flask_cors import CORS 
from risk_analyzer import calculate_risk

app = Flask(__name__)
<<<<<<< HEAD
CORS(app) # Enable Cross-Origin Resource Sharing

@app.route('/api/analyze', methods=['POST'])
=======

@app.route("/")
def home():
    return "AI Mitra Backend Running"


@app.route("/analyze", methods=["POST"])
>>>>>>> 441a793c5370f208524248f6d619bec890753051
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

<<<<<<< HEAD
    # 1. Call the AI Engine (Ollama integration running on your RTX 4050)
    ai_analysis = analyze_text(user_message)

    # 2. Call the Rule-based Risk Analyzer (Member 4's component)
    rule_analysis = calculate_risk(user_message)
    
    # Merge the results
    ai_analysis["rule_based_risk"] = rule_analysis.get("rule_based_risk", "Pending")

    # 3. Return the JSON response to the frontend
    return jsonify(ai_analysis)

if __name__ == '__main__':
    # Run the Flask app on port 5000
    print("Starting AI Mitra Backend Server...")
    print("Ensure Ollama is running in the background!")
    app.run(debug=True, port=5000)
=======
    score = analyze_text(user_text)
    risk = calculate_risk(score)

    return jsonify({
        "score": score,
        "risk_level": risk
    })


if __name__ == "__main__":
    app.run(debug=True)
>>>>>>> 441a793c5370f208524248f6d619bec890753051
