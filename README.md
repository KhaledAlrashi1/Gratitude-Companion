# Gratitude Companion [(App)](https://gratitude-companion-8017c39a85f8.herokuapp.com/)
![Gratitude](/images/Gratitude.png)

## Overview
Gratitude Companion is a friendly and supportive chatbot designed to help users practice gratitude. The chatbot encourages users to think about the positive aspects of their lives and helps them build a habit of gratitude through thought-provoking questions and empathetic interactions.


## Backgorund
For some time, I’ve been practicing gratitude daily, and it has been life-transformative. However, I often struggle to find new things to write about. I realized that asking unique questions could help uncover overlooked aspects of my life. So, I started using LLMs like Groq and ChatGPT to generate thought-provoking questions, leading to more meaningful gratitude sessions. This idea blossomed into the creation of Gratitude Companion after completing the DeepLearning.AI course.

After completing the “Open Source Models with Hugging Face” course by DeepLearning.AI, I used the inspiration and knowledge gained to develop my first AI-powered application: Gratitude Companion.

Gratitude Companion is a chatbot designed to enhance your gratitude practice by asking engaging questions. It integrates the recently developed GPT-4o mini for better text processing and understanding. What sets it apart is its training on online blogs shared by people, turning relevant blog content into live conversations. This allows users to share important memories and experiences, creating a sense of connection and realizing the commonality of human experiences.

Why should we practice gratitude? It helps us see the positive aspects of life, reminds us what’s truly important, encourages us to live in the present moment, reduces social comparison, and strengthens our relationships.

Gratitude: A big thank you to the DeepLearning.AI and Hugging Face teams for developing such an amazing course that led to the creation of this application.

---

## User Interface
![UI_1](/images/UI_1.png)
![UI_2](/images/UI_2.png)

---
## Features

- Engages users in meaningful conversations about gratitude.
- Stores conversation history for a personalized experience.
- Responsive web interface with real-time chat capabilities.

---
## Installation

### Prerequisites

- Python 3.11 or higher
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
