function submitDetails() {
    const patientName = document.getElementById('patientName').value;
    const dob = document.getElementById('dob').value;
    const bloodGroup = document.getElementById('bloodGroup').value;
    const patientImage = document.getElementById('patientImage');

    if (!patientName || !dob || !bloodGroup || !patientImage.files.length) {
        alert("Please fill in all details and upload an image.");
        return;
    }

    const dobFormatted = new Date(dob).toLocaleDateString("en-GB");

    document.getElementById('patientDetails').innerHTML = `
        <strong>Name:</strong> ${patientName}<br>
        <strong>Date of Birth:</strong> ${dobFormatted}<br>
        <strong>Blood Group:</strong> ${bloodGroup}<br>
        <strong>Uploaded Image:</strong> 
        <img src="${URL.createObjectURL(patientImage.files[0])}" alt="Patient MRI" 
             style="display: block; margin: 20px auto; width: 80%; max-width: 300px; 
             border: 1px solid #ccc; border-radius: 5px;">
    `;

    window.location.href = 'prediction.html'; // Redirect to Prediction Page
}