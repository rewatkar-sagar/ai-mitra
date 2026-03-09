function speakText(text){

const lang =
localStorage.getItem("lang") || "en-US";

const speech =
new SpeechSynthesisUtterance();

speech.text = text;
speech.lang = lang;

window.speechSynthesis.speak(speech);

}