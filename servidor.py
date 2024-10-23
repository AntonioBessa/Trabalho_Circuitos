from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Bem vindos"

@app.route('/data', methods=['POST'])
def handle_client():
    data = request.json
    if data is None:
        return jsonify({"error": "No data provided"}), 400
    
    # Processa os dados aqui (atualmente apenas imprimindo)
    print("Received data:", data)
    
    return jsonify({"message": "Data received successfully!"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
