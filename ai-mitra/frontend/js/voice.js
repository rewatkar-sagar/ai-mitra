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
}