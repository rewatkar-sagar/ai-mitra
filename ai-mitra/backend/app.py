from flask import Flask, request, jsonify
from ai_engine import analyze_text
from risk_analyzer import calculate_risk

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Mitra Backend Running"


@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.json
    user_text = data.get("text")

    score = analyze_text(user_text)
    risk = calculate_risk(score)

    return jsonify({
        "score": score,
        "risk_level": risk
    })


if __name__ == "__main__":
    app.run(debug=True)