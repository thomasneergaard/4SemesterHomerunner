from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify({'det virker': quueen})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)