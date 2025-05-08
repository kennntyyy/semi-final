import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return ("<p>Kent Paul Vergara</p>"
            "<p>BSIT - 3</p>"
            "<p>System Integration</p>"
            "<p>Semi-Final Exam</p>")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)