from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Example route for the homepage
@app.route('/')
def home():
    return "Welcome to the Flask App!"

# Example API route
@app.route('/api', methods=['GET'])
def api():
    data = {"message": "Hello from the Flask API!"}
    return jsonify(data)

if __name__ == '__main__':
    # Run the app with debug=True for local development
    app.run(debug=True)
