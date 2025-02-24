
// Select elements
const userMessageInput = document.getElementById("userMessage");
const submitButton = document.getElementById("submitButton");
const messageBoard = document.getElementById("messageBoard");

// Event listener for the Submit button
submitButton.addEventListener("click", function() {

    // Get the user input
    const userMessage = userMessageInput.value;

    // Sanitise the userMessage
    const sanitisedMessage = sanitiseInput(userMessage)

    // Display the sanitised message on the message board
    displayMessage(sanitisedMessage);

    // Clear the input field
    userMessageInput.value = "";
});


function sanitiseInput(input) {
    // Replace each unwanted character with its HTML-encoded equivalent
    return input
        .replaceAll("/", "&#47;")  // Replace & with &#47;
        .replaceAll("<", "&lt;")   // Replace < with &lt;
        .replaceAll(">", "&gt;");  // Replace > with &gt;
}


// Function to display the message on the message board
function displayMessage(message) {

    // Create a new paragraph html element
    const messageElement = document.createElement("p");

    // Set the text content of the paragraph to the message
    messageElement.textContent = message;

    // Add the message to the end of the message board list
    messageBoard.appendChild(messageElement);
}




