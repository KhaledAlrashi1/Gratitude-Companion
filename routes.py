from flask import Blueprint, request, jsonify, render_template, current_app
import openai
import uuid
import logging
import os

main = Blueprint('main', __name__)

# Helper function to load or create a user ID
def get_user_id():
    user_id_file = "user_id.txt"
    if os.path.exists(user_id_file):
        with open(user_id_file, "r") as file:
            user_id = file.read().strip()
    else:
        user_id = str(uuid.uuid4())
        with open(user_id_file, "w") as file:
            file.write(user_id)
    return user_id

@main.route('/')
def index():
    user_id = get_user_id()
    openai.api_key = current_app.config['OPENAI_API_KEY']
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a friendly and supportive chatbot focused on helping people practice gratitude. Your goal is to encourage users to think about the positive aspects of their lives and help them build a habit of gratitude. Be empathetic, cheerful, and motivating in your responses."},
                {"role": "user", "content": "Greet the user and ask a unique gratitude-related question."}
            ]
        )
        initial_message = response['choices'][0]['message']['content'].strip()
    except Exception as e:
        logging.error(f"Error during initial greeting request: {e}")
        initial_message = "Hello! What is something you're grateful for today?"

    return render_template('index.html', initial_message=initial_message)

@main.route('/chat', methods=['POST'])
def chat():
    openai.api_key = current_app.config['OPENAI_API_KEY']
    try:
        data = request.json
        user_input = data.get('message')
        user_id = get_user_id()

        # Define the personality prompt
        personality_prompt = (
            "You are a friendly and supportive chatbot focused on helping people practice gratitude. "
            "Your goal is to encourage users to think about the positive aspects of their lives and help them "
            "build a habit of gratitude. Be empathetic, cheerful, and motivating in your responses.\n"
            "User: {user_input}\nGPT-4o: "
        ).format(user_input=user_input)

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a friendly and supportive chatbot focused on helping people practice gratitude. Your goal is to encourage users to think about the positive aspects of their lives and help them build a habit of gratitude. Be empathetic, cheerful, and motivating in your responses."},
                {"role": "user", "content": user_input}
            ]
        )

        message = response['choices'][0]['message']['content'].strip()
        return jsonify({'response': message})
    except Exception as e:
        logging.error(f"Error during /chat request: {e}")
        return jsonify({'error': str(e)}), 500