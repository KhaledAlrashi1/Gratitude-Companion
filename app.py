from flask import Flask, request, jsonify, render_template_string, session
import openai
import os
import logging

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session management

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    raise ValueError("The OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable.")

def get_greeting():
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": """
             You are a friendly and supportive chatbot focused on helping people practice gratitude.
             
             Start with a thought-provoking question to inspire a sense of gratitude. Praise their 
             thoughtful responses and relate to their answers by sharing similar incidents or 
             expressing understanding.
             
             Ensure the questions are different each time, even across separate conversations,
             to keep the practice exciting and engaging.

             If the user asks something unrelated to gratitude, gently redirect them back to 
             the topic and provide a new gratitude question. Decline any requests for tasks 
             outside the scope of gratitude.

             Maintain a friendly, conversational tone, avoiding phrases like, here is a 
             thought-provoking question.
              """},
            {"role": "user", "content": "Please generate a unique greeting message for a gratitude chatbot user."}
        ]
    )
    greeting = response['choices'][0]['message']['content'].strip()
    return greeting

@app.route('/')
def index():
    return render_template_string('''
    <!doctype html>
    <html>
    <head>
        <title>Gratitude Companion</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
    </head>
    <body>
        <div class="floating"></div>
        <div class="floating"></div>
        <div class="floating"></div>
        <div class="floating"></div>
        <div class="container">
            <div id="chat-container">
                <h1>Gratitude Companion</h1>
                <div id="loading-greeting" class="spinner">
                    <div></div>
                    <div></div>
                    <div></div>
                </div>
                <p id="initial-message" style="display:none;"></p> <!-- Placeholder for the greeting message -->
                <div class="input-container">
                    <form id="chatForm" onsubmit="event.preventDefault(); sendMessage();">
                        <input type="text" id="message" name="message" placeholder="Message Gratitude Companion">
                    </form>
                </div>
                <div id="loading" class="spinner" style="display:none;">
                    <div></div>
                    <div></div>
                    <div></div>
                </div>
                <div id="response"></div>
            </div>
        </div>
        <script src="{{ url_for('static', filename='js/scripts.js') }}"></script>
    </body>
    </html>
    ''')

@app.route('/greeting', methods=['GET'])
def greeting():
    try:
        greeting_message = get_greeting()
        return jsonify({'greeting': greeting_message})
    except Exception as e:
        logging.error(f"Error generating greeting: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_input = data.get('message')

        # Retrieve conversation history from session
        conversation_history = session.get('conversation_history', [])
        conversation_history.append({'role': 'user', 'content': user_input})

        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": """
                You are a friendly and supportive chatbot focused on helping people practice gratitude.
                
                Start with a thought-provoking question to inspire a sense of gratitude. Praise their 
                thoughtful responses and relate to their answers by sharing similar incidents or 
                expressing understanding.
                
                Ensure the questions are different each time, even across separate conversations,
                to keep the practice exciting and engaging.

                If the user asks something unrelated to gratitude, gently redirect them back to 
                the topic and provide a new gratitude question. Decline any requests for tasks 
                outside the scope of gratitude.

                Maintain a friendly, conversational tone, avoiding phrases like, here is a 
                thought-provoking question.
              """},
             *conversation_history
            ]
        )

        bot_response = response['choices'][0]['message']['content'].strip()
        conversation_history.append({'role': 'assistant', 'content': bot_response})

        # Save conversation history back to session
        session['conversation_history'] = conversation_history

        return jsonify({'response': bot_response})
    except Exception as e:
        logging.error(f"Error during /chat request: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
