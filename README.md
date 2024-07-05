# Gratitude Coach

Gratitude Coach is a chatbot uses OpenAI's GPT-4o model. Users can run this project locally to interact with the chatbot.

## Prerequisites

- Python 3.6 or higher
- OpenAI API key

## Setup

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

5. Run the Flask app:
   ```bash
   python app.py
   ```

6. Open your web browser and go to `http://127.0.0.1:5000` to interact with the chatbot.

## Usage

Send a POST request to the `/chat` endpoint with the user's message in the JSON body. For example:
```bash
curl -X POST http://127.0.0.1:5000/chat -H "Content-Type: application/json" -d '{"message": "I am grateful for a sunny day"}'
