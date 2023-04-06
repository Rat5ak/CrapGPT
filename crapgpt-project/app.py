from flask import Flask, render_template, request
import openai

app = Flask(__name__)

openai.api_key = "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"
#comment1
def get_chatgpt_response(prompt, temperature=0.7, max_tokens=100):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301",
        messages=[
            {"role": "system", "content": "You are a crappy assistant that makes up bullshit answers that seem correct at face value but are infact cleverly crafted bullshit responses."},
            {"role": "user", "content": f"Answer comically incorrect: {prompt}"}
        ],
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=temperature,
    )

    return response.choices[0].message['content'].strip()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        prompt = request.form["prompt"]
        response = get_chatgpt_response(prompt, temperature=1.5, max_tokens=150)
        return render_template("index.html", response=response)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)


