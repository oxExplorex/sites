from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/data_to")
def data_to():
  some_pars = {'user': 'Ivan', 'color': 'red'}
  some_str = 'Hello my dear friends!'
  some_value = 10
  return render_template('simple.html', some_str=some_str, some_value=some_value, some_pars=some_pars)


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