async function checkNews() {
    const text = document.getElementById("newsText").value;

    document.getElementById("result").innerText = "Checking...";

    const response = await fetch("https://fakenews-detector-95lm.onrender.com/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: text })
    });

    const data = await response.json();
    document.getElementById("result").innerText = data.prediction;
}

function clearText() {
    document.getElementById("newsText").value = "";
    document.getElementById("result").innerText = "";
}
