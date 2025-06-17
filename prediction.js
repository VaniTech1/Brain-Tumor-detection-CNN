function predict() {
    const imageInput = document.getElementById('patientImage').files[0];
    const outputDiv = document.getElementById('predictionOutput');

    const formData = new FormData();
    formData.append("image", imageInput);

    fetch("http://127.0.0.1:5001/predict", {
        method: "POST",
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            outputDiv.classList.remove('hidden');
            outputDiv.innerHTML = `
            <strong>Prediction:</strong> ${data.prediction}<br>
            <strong>Confidence:</strong> ${data.confidence.toFixed(2)}%<br>
            <strong>Description:</strong> ${data.description || 'No description available'}
        `;
        })
        .catch(error => {
            console.error("Error during prediction:", error);
            alert("Failed to get prediction. Please try again.");
        });
}