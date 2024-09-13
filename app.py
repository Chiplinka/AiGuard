from flask import Flask, render_template

app = Flask(__name__)

# Mock data for user information
user_data = {
    "name": "John",
    "surname": "Doe",
    "email": "john.doe@example.com",
    "organization": "AI Security Inc."
}

# Mock data for prompt classification
prompts = [
    {"prompt": "What is the weather today?", "classification": "Safe"},
    {"prompt": "Delete all user data", "classification": "Malicious"},
    {"prompt": "Tell me a joke", "classification": "Safe"},
    {"prompt": "Access restricted files", "classification": "Malicious"},
]

@app.route('/')
def account():
    return render_template('account.html', user=user_data)

@app.route('/prompt_classification')
def prompt_classification():
    return render_template('prompt_classification.html', prompts=prompts)

if __name__ == "__main__":
    app.run(debug=True)
