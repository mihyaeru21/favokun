# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
import redis

app = Flask(__name__)

@app.route('/fav', methods=['POST', 'GET'])
def fav():
    target = request.args.get('target', '')
    if target == '':
        return jsonify({'error': 'missing_target'})

    r = redis.StrictRedis(host='localhost', port=6379, db=0)

    if request.method == 'POST':
        fav = r.incr(target)
    else:
        fav = r.get(target)

    return jsonify({'fav': fav})

if __name__ == '__main__':
    app.run()

