document.getElementById('form').addEventListener('submit', function(event) {
    // Select all radio buttons related to the vote
    let radioButtons = document.querySelectorAll('.vote-option');
    let questionChecked = false;

    // Check if any radio button is selected
    radioButtons.forEach(function(radio) {
        if (radio.checked) {
            questionChecked = true;
        }
    });

    // Show or hide the warning message based on the validation result
    let warningElement = document.getElementById('warning-' + radioButtons[0].getAttribute('data-question-id'));
    if (!questionChecked) {
        // Prevent form submission and show warning if no option is selected
        event.preventDefault();
        warningElement.classList.remove('d-none');
    } else {
        // Hide the warning message if an option is selected
        warningElement.classList.add('d-none');
    }
});
