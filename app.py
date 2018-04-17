import os
from flask import Flask



app = Flask(__name__)

@app.route('/')
def homepage():
    username = os.environ['DB_USER']
    return "<h1>Hello heroku test commit username " + username + "</h1>"
    

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

