from flask import Flask, request, jsonify
from flask_cors import CORS
from supabase import create_client

app = Flask(__name__)
CORS(app)
@app.route("/")
def home():
    return "AI Mitra Backend Running"
# Supabase setup
SUPABASE_URL = "https://sgvxmtodisrztmvoytnv.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNndnhtdG9kaXNyenRtdm95dG52Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzMwMTc1ODgsImV4cCI6MjA4ODU5MzU4OH0.n96Q7MVxs1X-HQ5PgYknGJ6cnkagcxxzrnm5P-uPw9U"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


@app.route("/analyze", methods=["POST"])
def analyze():

    text = request.json.get("text", "")

    # Simple fraud detection
    if "lottery" in text.lower() or "click" in text.lower():
        fraud_risk = "High"
        trust_score = 20
    else:
        fraud_risk = "Low"
        trust_score = 90

    # Emotional risk detection
    if "depressed" in text.lower() or "hopeless" in text.lower():
        risk_level = "High"
        trust_score = 40
    else:
        risk_level = "Low"

    # Data to store in database
    data = {
        "text": text,
        "fraud_risk": fraud_risk,
        "risk_level": risk_level,
        "trust_score": trust_score
    }

    # Insert into Supabase
    supabase.table("analysis_results").insert(data).execute()

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)