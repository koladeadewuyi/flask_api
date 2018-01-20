#!venv_flask/bin/python
from flask import Flask
import redis

app = Flask(__name__)

# Create conncetion pool
pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
# create redis client
r = redis.Redis(connection_pool = pool)

@app.route('/compute/<market>/<category>', methods = ['GET'])
def get_results(market, category):
    key = "%s_%s" % (market, category)
    result = r.get(key)
    return result

if __name__ == '__main__':
    app.run(debug=True)