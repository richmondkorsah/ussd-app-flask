let isHidden = true;

function toggleBalance() {
    const balanceSpan = document.getElementById('balance');
    if (isHidden) {
        balanceSpan.textContent = '500.00 GHS';
    } else {
        balanceSpan.textContent = '**********';
    }
    isHidden = !isHidden;
}

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