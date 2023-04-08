# Import necessary modules and packages
from flask import Flask, render_template, request, session, url_for, redirect
from flask_session import Session
import openai
import os

# Initialize the Flask app
app = Flask(__name__)

# Set up Flask-Session for session management
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = 'your_secret_key'
Session(app)

# Set the OpenAI API key
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Function to get a response from ChatGPT based on the given prompt and existing messages
def get_chatgpt_response(prompt, messages, temperature=1, max_tokens=100):
    # Add the user's message to the list of messages
    messages.append({"role": "user", "content": f"{prompt}"})
    
    # Call the OpenAI API to get a response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301",
        messages=[{"role": "system", "content": "You are a cheeky and funny assistant that provides mostly useless information while subtly mocking users."}, *messages],
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=temperature,
    )

    # Add the assistant's response to the list of messages
    messages.append({"role": "assistant", "content": response.choices[0].message['content'].strip()})
    return messages

# Route for the landing page
@app.route("/", methods=["GET"])
def landing():
    return render_template("landing.html")

# Route for the chatbot page
@app.route("/chatbot", methods=["GET", "POST"])
def index():
    # Initialize messages in session if not already present
    if 'messages' not in session:
        session['messages'] = []

    # If the request method is POST, get the prompt and fetch a response from ChatGPT
    if request.method == "POST":
        prompt = request.form["prompt"]
        session['messages'] = get_chatgpt_response(prompt, session['messages'], temperature=0.7, max_tokens=150)
        
    return render_template("index.html", messages=session['messages'])

# Route for resetting the chat
@app.route("/reset", methods=["GET"])
def reset_chat():
    # Remove messages from the session
    session.pop('messages', None)
    return redirect(url_for('index'))

# Run the Flask app in debug mode
if __name__ == "__main__":
    app.run(debug=True)
