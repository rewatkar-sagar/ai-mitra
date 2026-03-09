async function analyzeMessage(){

const msg =
document.getElementById("userMessage").value;

const response =
await fetch("http://localhost:5000/analyze",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({
message:msg
})

});

const data = await response.json();

document.getElementById("riskMeter")
.innerText = data.risk + "%";

document.getElementById("explanation")
.innerText = data.explanation;

speakText(data.explanation);

}