# ...existing code...
from flask import Flask, request

app = Flask(__name__)

@app.route('/oauth/callback')
def oauth_callback():
    full_url = request.url  # Gets the full URL including query parameters
    # Save full_url to a file for your Python app to read
    with open('auth_url.txt', 'w') as f:
        f.write(full_url)
    return f"Redirect URL: {full_url}"

if __name__ == '__main__':
    app.run()
# ...existing code...