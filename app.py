from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/sum', methods=['GET'])
def sum_numbers():
    try:
        num1 = float(request.args.get('num1', 0))
        num2 = float(request.args.get('num2', 0))
        return jsonify({
            'result': num1 + num2,
            'status': 'success'
        })
    except (TypeError, ValueError):
        return jsonify({
            'error': 'Invalid input. Please provide valid numbers.',
            'status': 'error'
        }), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6001)
