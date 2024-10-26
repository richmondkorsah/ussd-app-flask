function showFlashMessage(message) {
    const modal = document.getElementById("flashModal");
    const modalMessage = document.getElementById("modalMessage");
    modalMessage.innerText = message;
    modal.style.display = "block"; 
}

// Function to close the modal and redirect to the home page
function closeModal(homeUrl) {
    const modal = document.getElementById("flashModal");
    modal.style.display = "none"; 
    window.location.href = homeUrl; 
}

// Show the PIN dialog when submitting the form
function showPinDialog() {
    document.getElementById('pinDialog').style.display = 'block';
}

// Close the PIN dialog
function closePinDialog() {
    document.getElementById('pinDialog').style.display = 'none';
}

// Submit the form with the PIN value
function submitForm() {
    const pin = document.getElementById('pin').value;
    if (pin.length === 0) {
        alert('Please enter your PIN');
        return;
    }

    // Add the PIN to the form
    const form = document.getElementById('depositForm');
    const pinInput = document.createElement('input');
    pinInput.type = 'hidden';
    pinInput.name = 'pin';
    pinInput.value = pin;
    form.appendChild(pinInput);

    // Submit the form
    form.submit();
}