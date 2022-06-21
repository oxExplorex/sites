from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
 return " <html><head></head> <body> Hello World! </body></html>"

if __name__ == "__main__":
 app.run()


'''
pip install waitress
waitress-serve --listen=127.0.0.1:5000 wsgi:app

gunicorn --bind 127.0.0.1:5000 wsgi:app
'''