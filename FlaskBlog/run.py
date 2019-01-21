from ethirio import app 
from werkzeug.serving import WSGIRequestHandler

if __name__ == '__main__':
	app.debug=True
	WSGIRequestHandler.protocol_version = "HTTP/1.1"
	app.run(host="0.0.0.0", port=80)