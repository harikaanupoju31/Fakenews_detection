function checkNews() {

    let text = document.getElementById("newsText").value;

    if (text.trim() === "") {
        alert("Please enter some news!");
        return;
    }

    document.getElementById("loading").style.display = "block";
    document.getElementById("result").innerText = "";

    fetch("https://fakenews-detection-2p89.onrender.com/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: text })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Server error");
        }
        return response.json();
    })
    .then(data => {
        document.getElementById("loading").style.display = "none";

        let result = document.getElementById("result");
        result.innerText = data.prediction;

        if (data.prediction === "Real News") {
            result.style.color = "green";
        } else {
            result.style.color = "red";
        }
    })
    .catch(error => {
        document.getElementById("loading").style.display = "none";
        document.getElementById("result").innerText = "⚠️ Server error / Not connected";
        console.log(error);
    });
}

function clearText() {
    document.getElementById("newsText").value = "";
    document.getElementById("result").innerText = "";
}
