from flask import Flask, request, jsonify
from ai_engine import analyze_text
from risk_analyzer import calculate_risk
from supabase_client import supabase

app = Flask(__name__)

# -------------------------
# HOME ROUTE
# -------------------------
@app.route("/")
def home():
    return "AI Mitra Backend Running"


# -------------------------
# AI ANALYSIS API
# -------------------------
@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.json
    user_text = data.get("text")

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