# app.py

from flask import Flask, request, jsonify

app = Flask(__name__)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

@app.route('/is_prime_number', methods=['POST'])
def check_prime():
    data = request.get_json()
    number = data.get('number')
    if not isinstance(number, int):
        return jsonify({'error': 'Invalid input, please enter an integer'}), 400
    result = is_prime(number)
    return jsonify({'number': number, 'is_prime_number': result})

if __name__ == '__main__':
    app.run(debug=True)
