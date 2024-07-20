# Gratitude Companion
![Gratitude](/images/Gratitude.png)

## Overview
Gratitude Companion is a friendly and supportive chatbot designed to help users practice gratitude. The chatbot encourages users to think about the positive aspects of their lives and helps them build a habit of gratitude through empathetic, cheerful, and motivating interactions.


## Backgorund
I’ve been practicing the habit of gratitude ever since I read “The 7 Habits of Highly Effective People” by listing things I’m grateful for each day. However, there are days when I struggle to think of something to write, and I often overlook important aspects of my life, taking them for granted. To address this, I envisioned using ChatGPT to help me identify these overlooked elements and enhance my gratitude practice.

After completing the “Open Source Models with Hugging Face” course by DeepLearning.AI, I was inspired to create my first AI-powered application. This is how Gratitude Companion was born.

Gratitude Companion is a friendly chatbot designed to help you cultivate a daily gratitude practice. By asking engaging and thought-provoking questions, Gratitude Companion encourages you to reflect on various aspects of your life, helping you recognize and appreciate the many blessings you might otherwise miss. This AI-powered application makes practicing gratitude more enjoyable and impactful, ensuring you never run out of things to be thankful for.

---

## User Interface
![UI_1](/images/UI_1.png)
![UI_2](/images/UI_2.png)

---
## Features

- Generates unique greeting messages to welcome users.
- Engages users in meaningful conversations about gratitude.
- Stores conversation history for a personalized experience.
- Responsive web interface with real-time chat capabilities.
- Option to download conversation history as TXT or DOCX files.

---
## Installation

### Prerequisites

- Python 3.7 or higher
- Flask
- OpenAI API key


### Setup

1. Clone this repository or download the files.
```bash
git clone https://github.com/yourusername/gratitude-companion.git
cd gratitude-companion
```

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

5. Run the Flask app:
```bash
python app.py
```

6. Open your web browser and go to `http://127.0.0.1:5000` to interact with the chatbot.

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
          |── images/
              |── logo.png
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

- Thanks to OpenAI for providing the GPT-4o-mini API.
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
