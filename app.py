from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Lakshay Extractor'


if __name__ == "Lakshay Extractor":
    app.run()
