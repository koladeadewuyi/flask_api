```bash
sudo pip install virtualenv
mkdir flask-api
cd flask-api
virtualenv venv_flask
venv_flask/bin/pip install flask
```

```python
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
```

```bash
# Grant user permisions to execute app.py file
chmod 744 app.py
```

```bash
# run app.py
./app.py
```

1. 000 0
1. 001 1
1. 010 2
1. 011 3
1. 100 4
1. 101 5
1. 110 6
1. 111 7

1. rwx rwx r__
1. 111 100 100
1. 7   4   4
