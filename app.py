import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/v1/secret', methods=['GET'])
def get_secret():
    server_name = request.args.get('server')  
    secret_file = f'secret_{server_name}.txt' 
    secret = ""

    if os.path.exists(secret_file):
        with open(secret_file, 'r') as file:
            secret = file.read().strip()

    return jsonify({"server": server_name, "secret": secret})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
