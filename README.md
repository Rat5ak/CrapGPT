
# Crap GPT Setup Guide

In this repository, you'll find all the necessary files to set up and run the Crap GPT chatbot. The chatbot is a fun, cheeky, and mostly useless assistant that subtly mocks users while providing them with information. Follow these easy steps to set up the project and enjoy some Monty Python-esque banter with the chatbot.

## Prerequisites

- Python 3.6 or higher installed
- A sense of humor
- An OpenAI API key (visit [OpenAI](https://beta.openai.com/signup/) to sign up and get your key)

## Step 1: Clone the repository

First, clone the repository to your local machine using the command below:

git clone https://github.com/yourusername/crapgpt.git

## Step 2: Set up a virtual environment

Navigate to the project folder and create a virtual environment to keep all the dependencies for the project isolated:

cd crapgpt

python3 -m venv venv

Activate the virtual environment:

**On macOS and Linux:**
source venv/bin/activate

graphql
Copy code

**On Windows:**
.\venv\Scripts\activate

## Step 3: Install the required packages

Install the necessary packages listed in the `requirements.txt` file:

pip install -r requirements.txt

These packages include Flask, OpenAI, Gunicorn, and Flask-Session.

## Step 4: Set up the environment variables

Create a `.env` file in the root of the project folder to store your environment variables:

touch .env

Open the `.env` file and add the following lines:

OPENAI_API_KEY=your_openai_api_key_here
SECRET_KEY=a_random_string_for_your_secret_key

Replace `your_openai_api_key_here` with your actual OpenAI API key and `a_random_string_for_your_secret_key` with a randomly generated string for Flask's secret key.

## Step 5: Run the application

Run the Crap GPT chatbot locally using the following command:

python app.py

Your chatbot should now be up and running on `http://localhost:5000`. Open a web browser and navigate to the URL to start chatting with your very own cheeky, Monty Python-inspired assistant!

## Step 6: Deploying to a server (optional)

If you wish to deploy the chatbot to a web server, you can use the provided `Procfile` to deploy the application to a platform like [Heroku](https://www.heroku.com/). The `Procfile` contains the necessary commands for both `python app.py` and `gunicorn app:app`.

## And now for something completely different...

Enjoy your conversations with the Crap GPT chatbot and don't forget to share the experience with your friends and fellow Monty Python fans!

Remember, "Nobody expects the Spanish Inquisition!" or the Crap GPT chatbot for that matter. Happy chatting!
