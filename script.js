function checkNews() {
    let text = document.getElementById("newsText").value;

    if (text.trim() === "") {
        alert("Please enter news!");
        return;
    }

    document.getElementById("loading").style.display = "block";
    document.getElementById("result").innerText = "";

    fetch("/predict", {   // 🔥 IMPORTANT CHANGE
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: text })
    })
    .then(response => response.json())
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
        console.error("Error:", error);
        document.getElementById("loading").style.display = "none";
    });
}
