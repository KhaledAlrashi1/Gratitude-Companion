document.addEventListener('DOMContentLoaded', (event) => {
    // Set the initial message once at the top
    document.getElementById('initial-message').style.display = 'block';
    document.getElementById('response').innerHTML = '';
});

function sendMessage() {
    var message = document.getElementById('message').value;
    document.getElementById('loading').style.display = 'block';
    document.getElementById('response').style.display = 'none';
    document.getElementById('initial-message').style.display = 'none'; // Hide the initial message
    document.getElementById('response').innerHTML = '';
    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: message })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('loading').style.display = 'none';
        document.getElementById('response').style.display = 'block';
        document.getElementById('response').innerHTML = '<p>' + data.response + '</p>';
        document.getElementById('message').value = ''; // Clear input field
    })
    .catch(error => {
        document.getElementById('loading').style.display = 'none';
        console.error('Error:', error);
    });
}

document.getElementById('message').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        e.preventDefault();
        sendMessage();
    }
});