
from flask import Flask
from datetime import datetime
import time

app = Flask(__name__)
cache = {}
cache_timeout = 60

@app.route('/ping')
def ping():
    return 'Aplicação Flask viva!'

@app.route('/time')
def time_route():
    now = time.time()
    if 'value' in cache and now - cache['time'] < cache_timeout:
        return cache['value']

    current_time = datetime.utcnow().isoformat()
    cache['value'] = current_time
    cache['time'] = now
    return current_time

app.run(port=5000)
