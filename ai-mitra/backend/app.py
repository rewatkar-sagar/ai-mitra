from flask import Flask, request, jsonify
from ai_engine import analyze_text
from risk_analyzer import calculate_risk
from supabase_client import supabase

app = Flask(__name__)
CORS(app) # Enable Cross-Origin Resource Sharing

@app.route('/api/analyze', methods=['POST'])

@app.route("/")
def home():
    return "AI Mitra Backend Running"


# -------------------------
# AI ANALYSIS API
# -------------------------
@app.route("/analyze", methods=["POST"])

def analyze():

    data = request.json
    
    # Handle both 'message' and 'text' keys just in case the frontend changes it
    if not data:
        return jsonify({'error': 'No data provided in the request body.'}), 400
        
    user_message = data.get('message') or data.get('text')
    
    if not user_message:
        return jsonify({'error': 'No message provided.'}), 400

    score = analyze_text(user_text)
    risk = calculate_risk(score)

    # Store result in Supabase
    supabase.table("user_results").insert({
        "user_text": user_text,
        "risk_level": risk
    }).execute()

    return jsonify({
        "score": score,
        "risk_level": risk
    })


# -------------------------
# RUN SERVER
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)
