from flask import Flask, request, jsonify
from supabase_client import supabase
from ai_engine import analyze_text
from risk_analyzer import calculate_risk

app = Flask(__name__)
@app.route('/analyze', methods=['POST'])
def analyze():

    data = request.json
    user_text = data.get("text")

    ai_result = analyze_text(user_text)
    risk = calculate_risk(user_text)

    supabase.table("user_results").insert({
        "user_text": user_text,
        "risk_level": risk
    }).execute()

    return jsonify({
        "risk_level": risk,
        "explanation": ai_result["explanation"],
        "verification_tip": ai_result["verification_tip"]
    })