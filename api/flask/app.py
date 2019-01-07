from flask import Flask
from flask import request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello to Flask Authentication Server'


@app.route('/auth')
def auth():
	original_uri = request.headers.get('X-Original-URI')

	if original_uri is None or 'allow' not in original_uri:
		return "Not Authenticated", 401 
	else:
		return 'Authenticated'


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')