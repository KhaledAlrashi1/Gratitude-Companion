document.addEventListener('DOMContentLoaded', (event) => {
    clearChatHistory(); // Clear chat history on page load
    loadGreeting(); // Load a unique greeting from the server
});

function clearChatHistory() {
    sessionStorage.removeItem('chatHistory');
    const responseDiv = document.getElementById('response');
    responseDiv.innerHTML = '';
}

function saveChatHistory() {
    const responseDiv = document.getElementById('response');
    sessionStorage.setItem('chatHistory', responseDiv.innerHTML);
}

function loadChatHistory() {
    const responseDiv = document.getElementById('response');
    const chatHistory = sessionStorage.getItem('chatHistory');
    if (chatHistory) {
        responseDiv.innerHTML = chatHistory;
    }
}

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
        const botMessage = `<p>${data.response}</p>`; // Remove "Bot:" label

        // Store the bot's response but only display the latest one
        const allMessages = responseDiv.innerHTML + botMessage;
        responseDiv.innerHTML = botMessage; // Only show the latest bot's response

        sessionStorage.setItem('chatHistory', allMessages); // Save full chat history for downloading
        document.getElementById('loading').style.display = 'none'; // Hide spinner once loaded
        responseDiv.style.display = 'block'; // Show the response div

        document.getElementById('download-conversation').style.display = 'block'; // Show download button
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('loading').style.display = 'none'; // Hide spinner on error
        responseDiv.style.display = 'block'; // Show the response div on error
    });
}

function downloadConversation() {
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

document.getElementById('message').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        e.preventDefault(); // Prevent form submission
        sendMessage();
    }
});