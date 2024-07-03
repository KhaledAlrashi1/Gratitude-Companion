from flask import Flask, request, jsonify
import openai
import os
import uuid

app = Flask(__name__)

# Configure OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

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

@app.route('/chat', methods=['POST'])
def chat():
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

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=personality_prompt,
        max_tokens=150
    )

    message = response.choices[0].text.strip()
    return jsonify({'response': message})

if __name__ == '__main__':
    app.run(debug=True)