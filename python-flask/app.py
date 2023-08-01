from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_geek():
   return '<h1>Hello from Flask & Docker</h1>'
@app.route('/ms')
@app.route('/ps')
@app.route('/mps')
def mega():
   return '<h1>Welcome to MegaFamily!......</h1>'
@app.route('/ss')
def super():
   return '<h1>Welcome to SuperstarFamily</h1>'


if __name__ == "__main__":
   app.run(debug=True)