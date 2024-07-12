# from flask import Blueprint, request, jsonify, render_template, current_app, session
# import openai
# import uuid
# import logging
# import os

# main = Blueprint('main', __name__)
# main.secret_key = os.urandom(24)  # Add a secret key for session management

# # # Helper function to load or create a user ID
# # def get_user_id():
# #     user_id_file = "user_id.txt"
# #     if os.path.exists(user_id_file):
# #         with open(user_id_file, "r") as file:
# #             user_id = file.read().strip()
# #     else:
# #         user_id = str(uuid.uuid4())
# #         with open(user_id_file, "w") as file:
# #             file.write(user_id)
# #     return user_id

# @main.route('/')
# def index():
#     # user_id = get_user_id()
#     openai.api_key = current_app.config['OPENAI_API_KEY']
#     try:
#         logging.info("Sending request to OpenAI for initial greeting")
#         response = openai.ChatCompletion.create(
#             model="gpt-4o",  # Use gpt-4o model
#             messages=[
#                 {"role": "system", "content": "You are a friendly and supportive chatbot focused on helping people practice gratitude. Your goal is to encourage users to think about the positive aspects of their lives and help them build a habit of gratitude. Be empathetic, cheerful, and motivating in your responses."},
#                 {"role": "user", "content": "Greet the user and ask a unique gratitude-related question."}
#             ]
#         )
#         initial_message = response['choices'][0]['message']['content'].strip()
#         logging.info(f"Received initial message: {initial_message}")
#     except Exception as e:
#         logging.error(f"Error during initial greeting request: {e}")
#         initial_message = "Hello! What is something you're grateful for today?"

#     return render_template('index.html', initial_message=initial_message)

# @main.route('/chat', methods=['POST'])
# def chat():
#     openai.api_key = current_app.config['OPENAI_API_KEY']
#     try:
#         data = request.json
#         user_input = data.get('message')

#         # Retrieve conversation history from the session
#         conversation_history = session.get('conversation_history', [])

#         # Append the user's input to the conversation history
#         conversation_history.append({"role": "user", "content": user_input})

#         # Define the messages to send to the API
#         messages = [
#             {"role": "system", "content": "You are a friendly and supportive chatbot focused on helping people practice gratitude. Your goal is to encourage users to think about the positive aspects of their lives and help them build a habit of gratitude. Be empathetic, cheerful, and motivating in your responses."}
#         ] + conversation_history

#         logging.info(f"Sending conversation history to OpenAI: {messages}")
#         response = openai.ChatCompletion.create(
#             model="gpt-4o",  # Use gpt-4o model
#             messages=messages
#         )

#         message = response['choices'][0]['message']['content'].strip()
#         logging.info(f"Received response from OpenAI: {message}")

#         # Append the chatbot's response to the conversation history
#         conversation_history.append({"role": "assistant", "content": message})

#         # Store the updated conversation history in the session
#         session['conversation_history'] = conversation_history

#         return jsonify({'response': message})
#     except Exception as e:
#         logging.error(f"Error during /chat request: {e}")
#         return jsonify({'error': str(e)}), 500

from flask import Blueprint, request, jsonify, render_template, session, current_app
import logging
import pandas as pd
import random
import openai
import os

main = Blueprint('main', __name__)

# Load OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    raise ValueError("The OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable.")

# Load greeting messages from CSV
greeting_messages = pd.read_csv('greeting_messages.csv')['greeting_message'].tolist()

@main.route('/')
def index():
    try:
        logging.info("Fetching initial greeting message from CSV")
        initial_message = random.choice(greeting_messages)
        logging.info(f"Initial message: {initial_message}")
    except Exception as e:
        logging.error(f"Error fetching initial greeting message: {e}")
        initial_message = "Hello! What is something you're grateful for today?"

    return render_template('index.html', initial_message=initial_message)

@main.route('/greeting', methods=['GET'])
def greeting():
    try:
        greeting_message = random.choice(greeting_messages)
        return jsonify({'greeting': greeting_message})
    except Exception as e:
        logging.error(f"Error generating greeting: {e}")
        return jsonify({'error': str(e)}), 500

@main.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_input = data.get('message')

        # Retrieve conversation history from the session
        conversation_history = session.get('conversation_history', [])
        conversation_history.append({"role": "user", "content": user_input})

        # Prepare the tailored prompt
        system_message = {
            "role": "system",
            "content": """
            You are a friendly and supportive chatbot focused on helping people practice gratitude.
            
            Praise their thoughtful responses and relate to their answers by sharing similar incidents or 
            expressing understanding.
            
            Give a follow-up question to give a sense of friendly and deep conversation. The follow-up
            questions could be on the same subject or something relevant. Keep the practice exciting 
            and engaging. Maintain a friendly, conversational tone.

            If the user asks something unrelated to gratitude, gently redirect them back to 
            the topic and provide a new gratitude question. Decline any requests for tasks 
            outside the scope of gratitude.

            """
        }

        messages = [system_message] + conversation_history

        logging.info(f"Sending messages to OpenAI model: {messages}")

        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=messages
        )

        bot_response = response['choices'][0]['message']['content'].strip()
        logging.info(f"Received response from OpenAI: {bot_response}")

        # Append the chatbot's response to the conversation history
        conversation_history.append({"role": "assistant", "content": bot_response})

        # Store the updated conversation history in the session
        session['conversation_history'] = conversation_history

        return jsonify({'response': bot_response})
    except Exception as e:
        logging.error(f"Error during /chat request: {e}")
        return jsonify({'error': str(e)}), 500