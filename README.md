# Gratitude Companion
![Gratitude](/images/Gratitude.png)

## Overview
Gratitude Companion is a friendly and supportive chatbot designed to help users practice gratitude. The chatbot encourages users to think about the positive aspects of their lives and helps them build a habit of gratitude through empathetic, cheerful, and motivating interactions.

---
## Features

- Generates unique greeting messages to welcome users.
- Engages users in meaningful conversations about gratitude.
- Stores conversation history for a personalized experience.
- Responsive web interface with real-time chat capabilities.

---
## Installation

### Prerequisites

- Python 3.7 or higher
- Flask
- OpenAI API key


### Setup

1. Clone this repository or download the files.

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Set your OpenAI API key as an environment variable:
```bash
export OPENAI_API_KEY='your-openai-api-key'  # On Windows, use `set OPENAI_API_KEY=your-openai-api-key`
```

6. Run the Flask app:
```bash
python app.py
```

7. Open your web browser and go to `http://127.0.0.1:5000` to interact with the chatbot.

---
## Usage
1.	Run the application:
```bash
python app.py
```

2. Open your browser and navigate to:
```bash
http://127.0.0.1:5000
```

3.	Interact with the Gratitude Companion chatbot.

---
## Project Structure
      gratitude-companion/
      |── app.py
      |── config.py
      |── routes.py
      |── templates/
      |   |── index.html
      |── static/
      |   |── css/
      |   |   |── styles.css
      |   |── js/
      |       |── scripts.js
      |── requirements.txt
      |── README.md

---
## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

1.	Fork the repository
2.	Create your feature branch:
```bash
git checkout -b feature/YourFeature
```
3. Commit your changes:
```bash
git commit -m 'Add your feature'
```
4. Push to the branch:
```bash
git push origin feature/YourFeature
```
5. Create a pull request

---
## Acknowledgments

- Thanks to OpenAI for providing the GPT-4 API.
- Special thanks to everyone who has contributed to this project.

--- 
## Detailed Breakdown of Files

### app.py

- Sets up the Flask application.
- Configures logging and OpenAI API key.
- Defines routes for index, greeting, and chat.
- Manages conversation history using Flask sessions.

### config.py

- Loads OpenAI API key from environment variables.
- Raises an error if the API key is not set.

### routes.py

- Defines Flask Blueprint for main routes.
- Handles user ID management and initial greeting message.
- Manages conversation history and interactions with the OpenAI API.

### index.html

- Basic HTML template for the web interface.
- Includes placeholders for greeting messages and chat responses.

### scripts.js

- JavaScript to handle chat interactions and manage session storage.
- Includes functions to load greeting messages and send user messages.
 
---
Please let me know if you need any changes or additional details!
