from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! Your CI/CD pipeline deployed this Flask app "

@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return f"The sum of {a} and {b} is {a + b}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

