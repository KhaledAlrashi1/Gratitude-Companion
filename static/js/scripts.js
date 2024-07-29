document.addEventListener('DOMContentLoaded', (event) => {
    clearChatHistory(); // Clear chat history on page load
    loadGreeting(); // Load a unique greeting from the server
});

/**
 * Clears the chat history from sessionStorage and the response div.
 */
function clearChatHistory() {
    sessionStorage.removeItem('chatHistory');
    const responseDiv = document.getElementById('response');
    responseDiv.innerHTML = '';
}

/**
 * Saves the current chat history from the response div to sessionStorage.
 */
function saveChatHistory() {
    const responseDiv = document.getElementById('response');
    sessionStorage.setItem('chatHistory', responseDiv.innerHTML);
}

/**
 * Loads the chat history from sessionStorage and displays it in the response div.
 */
function loadChatHistory() {
    const responseDiv = document.getElementById('response');
    const chatHistory = sessionStorage.getItem('chatHistory');
    if (chatHistory) {
        responseDiv.innerHTML = chatHistory;
    }
}

/**
 * Loads a unique greeting message from the server and displays it.
 */
function loadGreeting() {
    document.getElementById('loading-greeting').style.display = 'flex'; // Show spinner while loading

    fetch('/greeting')
        .then(response => response.json())
        .then(data => {
            const initialMessageDiv = document.getElementById('initial-message');
            initialMessageDiv.innerText = data.greeting;
            initialMessageDiv.style.display = 'block'; // Show the greeting
            document.getElementById('loading-greeting').style.display = 'none'; // Hide spinner once loaded
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('loading-greeting').style.display = 'none'; // Hide spinner on error
        });
}

/**
 * Sends a user message to the server and handles the response.
 */
function sendMessage() {
    var message = document.getElementById('message').value;
    if (message.trim() === "") return;

    document.getElementById('message').value = "";

    const initialMessageDiv = document.getElementById('initial-message');
    if (initialMessageDiv) {
        initialMessageDiv.style.display = 'none'; // Hide the greeting after the first response
    }

    const responseDiv = document.getElementById('response');
    const userMessage = `<p>You: ${message}</p>`;
    responseDiv.innerHTML += userMessage; // Store the user's message

    document.getElementById('loading').style.display = 'flex'; // Show spinner while waiting for response
    responseDiv.style.display = 'none'; // Hide the response div

    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: message })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            const limitMessage = `<p>You have reached the maximum number of API requests allowed for today.</p>`;
            responseDiv.innerHTML = limitMessage;
            document.getElementById('loading').style.display = 'none'; // Hide spinner on error
            responseDiv.style.display = 'block'; // Show the response div
            return;
        }

        const botMessage = `<p>${data.response}</p>`; // Display the bot's response

        // Store the bot's response but only display the latest one
        const allMessages = responseDiv.innerHTML + botMessage;
        responseDiv.innerHTML = botMessage; // Only show the latest bot's response

        sessionStorage.setItem('chatHistory', allMessages); // Save full chat history for downloading
        document.getElementById('loading').style.display = 'none'; // Hide spinner once loaded
        responseDiv.style.display = 'block'; // Show the response div

        // Show download dropdown and button
        document.getElementById('download-container').style.display = 'block';
    })
    .catch(error => {
        console.error('Error:', error);
        const errorMessage = `<p>Error: ${error.message}</p>`;
        responseDiv.innerHTML = errorMessage;
        document.getElementById('loading').style.display = 'none'; // Hide spinner on error
        responseDiv.style.display = 'block'; // Show the response div on error
    });
}

/**
 * Initiates the download of the conversation history in the selected format.
 */
function downloadConversation() {
    const format = document.getElementById('download-format').value;
    if (format === 'TXT') {
        downloadConversationAsTxt();
    } else if (format === 'DOCX') {
        downloadConversationAsDocx();
    }
}

/**
 * Downloads the conversation history as a text file.
 */
function downloadConversationAsTxt() {
    const initialMessage = document.getElementById('initial-message').innerText;
    const chatHistory = sessionStorage.getItem('chatHistory');
    const allMessages = initialMessage + '\n\n' + chatHistory;
    const blob = new Blob([allMessages], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'conversation.txt';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
}

/**
 * Downloads the conversation history as a DOCX file.
 */
function downloadConversationAsDocx() {
    fetch('/export/docx')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.blob();
        })
        .then(blob => {
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.style.display = 'none';
            a.href = url;
            a.download = 'conversation.docx';
            document.body.appendChild(a);
            a.click();
            window.URL.revokeObjectURL(url);
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

// Add event listener for the Enter key to send a message
document.getElementById('message').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        e.preventDefault(); // Prevent form submission
        sendMessage();
    }
});