let isHidden = true;

function toggleBalance() {
    const balanceSpan = document.getElementById('balance');
    if (isHidden) {
        // Show the actual balance
        balanceSpan.textContent = '500.00 GHS';
    } else {
        // Hide the balance
        balanceSpan.textContent = '**********';
    }
    isHidden = !isHidden;
}
