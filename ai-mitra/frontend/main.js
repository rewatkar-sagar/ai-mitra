async function analyzeText() {
  console.log("Analyze button was clicked!");

  const text = document.getElementById("textInput").value;

  if (!text) {
    alert("Please enter or speak a message");
    return;
  }

  const response = await fetch("http://127.0.0.1:5000/analyze", {
    method: "POST",

    headers: {
      "Content-Type": "application/json",
    },

    body: JSON.stringify({ text: text }),
  });

  const data = await response.json();

  document.getElementById("fraud").innerText = data.fraud_risk;
  document.getElementById("risk").innerText = data.risk_level;
  document.getElementById("trust").innerText = data.trust_score + "%";

  document.getElementById("trustFill").style.width = data.trust_score + "%";
}
