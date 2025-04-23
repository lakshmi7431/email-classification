from flask import Flask, request, jsonify
from api import classify_email

app = Flask(__name__)

@app.route('/classify', methods=['POST'])
def classify():
    email_body = request.json.get('email_body')
    result = classify_email(email_body)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)