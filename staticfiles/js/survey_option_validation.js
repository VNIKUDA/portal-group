document.getElementById('form').addEventListener('submit', function(event) {
    console.log("hahah")
    let multipleChoiceQuestions = document.querySelectorAll('.multiple-choice');
    let singleChoiceQuestions = document.querySelectorAll('.single-choice');
    let questionChecked = {};

    // Initialize an object to track which questions have at least one option checked
    multipleChoiceQuestions.forEach(function(checkbox) {
        let questionId = checkbox.getAttribute('data-question-id');
        if (!questionChecked[questionId]) {
            questionChecked[questionId] = false;
        }

        // If any checkbox in the group is checked, mark the question as valid
        if (checkbox.checked) {
            questionChecked[questionId] = true;
        }
    });

    singleChoiceQuestions.forEach(function(radio) {
        let questionId = radio.getAttribute('data-question-id');
        if (!questionChecked[questionId]) {
            questionChecked[questionId] = false;
        }

        // If any radio button in the group is checked, mark the question as valid
        if (radio.checked) {
            questionChecked[questionId] = true;
        }
    });

    // Validate all questions
    let allValid = true;
    for (let questionId in questionChecked) {
        let warningElement = document.getElementById('warning-' + questionId);
        if (!questionChecked[questionId]) {
            allValid = false;
            // Show the warning message
            warningElement.classList.remove('d-none');
        } else {
            // Hide the warning message if the question is valid
            warningElement.classList.add('d-none');
        }
    }

    // If not all questions are valid, prevent form submission
    if (!allValid) {
        event.preventDefault();
    }
});