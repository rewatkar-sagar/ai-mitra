<<<<<<< HEAD
function startVoiceInput() {

    if (!('webkitSpeechRecognition' in window)) {
        alert("Voice recognition not supported in this browser. Use Chrome.");
        return;
    }

    const recognition = new webkitSpeechRecognition();

    recognition.lang = "en-US";
    recognition.continuous = false;
    recognition.interimResults = false;

    recognition.start();

    recognition.onstart = function () {
        console.log("Voice recognition started...");
    };

    recognition.onresult = function (event) {

        const transcript = event.results[0][0].transcript;

        document.getElementById("textInput").value = transcript;

        console.log("Voice input:", transcript);
    };

    recognition.onerror = function (event) {
        console.error("Voice error:", event.error);
    };

    recognition.onend = function () {
        console.log("Voice recognition ended.");
    };
=======
function speakText(text){

const lang =
localStorage.getItem("lang") || "en-US";

const speech =
new SpeechSynthesisUtterance();

speech.text = text;
speech.lang = lang;

window.speechSynthesis.speak(speech);

>>>>>>> c41ce8a9ce5eda57a152358a3a6158d6b1cc4b4d
}