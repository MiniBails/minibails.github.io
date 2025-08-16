# Example Flask endpoint for OAuth2 redirect
from flask import Flask, request

app = Flask(__name__)

@app.route('/oauth/callback')
def oauth_callback():
    code = request.args.get('code')
    state = request.args.get('state')
    # Store/send code to your Python app here
    return f"Code: {code}, State: {state}"

if __name__ == '__main__':
    app.run()