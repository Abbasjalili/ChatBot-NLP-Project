from flask import Flask, render_template, url_for

app = Flask(__name__, static_folder="C:/Users/AJALI/OneDrive/Documents/GitHub/ChatBot NLP Project/static")

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)