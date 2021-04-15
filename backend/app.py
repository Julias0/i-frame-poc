from flask import Flask, send_from_directory, request

app = Flask(__name__, static_url_path='')

@app.route('/<path:path>')
def home():
    return send_from_directory('js', path)

@app.route('/sign_up', methods=['POST'])
def signUpUserForNewsletter():
    body = request.get_json()
    print(body)
    return "<h1>Success!</h1>"