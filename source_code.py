from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "This is the first Assignment for Virtualization and Cloud Computing"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
