// Add input validation for the ticker symbol
document.addEventListener('DOMContentLoaded', function() {
    const tickerInput = document.getElementById('ticker');
    if (tickerInput) {
        tickerInput.addEventListener('input', function(e) {
            // Convert to uppercase and remove any non-alphanumeric characters
            this.value = this.value.toUpperCase().replace(/[^A-Z0-9.]/g, '');
        });
    }
});

// Add loading state to the analyze button
const analyzeForm = document.querySelector('form');
if (analyzeForm) {
    analyzeForm.addEventListener('submit', function(e) {
        const submitButton = this.querySelector('button[type="submit"]');
        if (submitButton) {
            submitButton.disabled = true;
            submitButton.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Analyzing...';
        }
    });
} 