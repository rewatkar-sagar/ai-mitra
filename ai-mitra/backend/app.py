from flask import Flask, request, jsonify

from risk_analyzer import calculate_risk
from trust_meter import trust_meter
from fraud_checker import fraud_check
from quiz_engine import get_quiz
from certificate import generate_certificate

app = Flask(__name__)


@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.json
    text = data.get("text")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    # simple emotion detection
    if "stress" in text.lower() or "sad" in text.lower():
        score = 2
    else:
        score = 0

    risk_level = calculate_risk(score)

    trust_score = trust_meter(text)

    fraud_risk = fraud_check(text)

    result = {
        "text": text,
        "risk_level": risk_level,
        "trust_score": trust_score,
        "fraud_risk": fraud_risk
    }

    return jsonify(result)


@app.route("/quiz", methods=["GET"])
def quiz():
    return jsonify(get_quiz())


@app.route("/certificate", methods=["POST"])
def certificate():

    data = request.json
    name = data.get("name")

    cert = generate_certificate(name)

    return jsonify({
        "certificate": cert
    })


if __name__ == "__main__":
    app.run(debug=True)