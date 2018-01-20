sudo pip install virtualenv
mkdir flask-api
cd flask-api
virtualenv venv_flask
venv_flask/bin/pip install flask

# create file app.py
# START
#!venv_flask/bin/python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
# END

# Grant user permisions to execute app.py file
chmod 744 app.py

# run app.py
./app.py

000 0
001 1
010 2
011 3
100 4
101 5
110 6
111 7

rwx rwx r__
111 100 100
7   4   4
