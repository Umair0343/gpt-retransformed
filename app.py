from flask import Flask, request, render_template,jsonify
from openai import OpenAI

app = Flask(__name__)

# Set up OpenAI API key
client = OpenAI(api_key="YOUR_API_KEY")

# List of available models
models = ["gpt-3.5-turbo", "gpt-3.5-turbo-0125", "gpt-3.5-turbo-1106"]
# operation = ["Sentiment analysis (Positive, negative or neutral)", "Text classification", "Translate English to French", "Summarize text", "Text completion"]

@app.route("/results", methods=["GET"])
def results():
    if request.method == "GET":
        # Get the selected model and prompt from the form
        model = request.args.get('model')
        prompt = request.args.get('prompt')

        # Call the OpenAI API with the selected model and prompt
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        # result = response['choices'][0]['message']['content']
        result = response.choices[0].message.content

        # Render the results page with the response
        return render_template("results.html", response=result)

    # Render the main page with the list of models
    return render_template("prompt_design.html", models=models)

@app.route("/results_new", methods=["GET"])
def results_new():
    if request.method == "GET":
        # Get the selected model, prompt, and operation from the form
        model = request.args.get('model')
        prompt = request.args.get('prompt')
        operation = request.args.get('operation')

        # Call the OpenAI API with the selected model, prompt, and operation
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": f"Consider yourself as my helpful assistant. Provide a response based on the operation: {operation}"},
                {"role": "user", "content": prompt}
            ]
        )
        
        # Extract the result from the response
        result = response.choices[0].message.content

        # Render the results page with the response, model, prompt, and operation
        return render_template("results_new.html", response=result, model=model, prompt=prompt, operation=operation)

    # Render the main page with the list of models if the method is not GET
    return render_template("specific_tasks.html", models=models , prompt=prompt, operation=operation)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/prompt_design", methods=["GET"])
def prompt_design():
    return render_template("prompt_design.html", models=models)

@app.route("/specific_tasks", methods=["GET"])
def specific_tasks():
    return render_template("specific_tasks.html", models=models)

if __name__ == "__main__":
    app.run(debug=True)