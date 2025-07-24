# Import necessary modules from Flask and Flask-CORS
from flask import Flask, jsonify
from flask_cors import CORS

# Create a Flask application instance
app = Flask(__name__)

# Enable Cross-Origin Resource Sharing (CORS) for the app
CORS(app)

# Define a route for the API endpoint '/api/data' with the GET method
@app.route('/api/data', methods=['GET'])
def hello():
    # Return a JSON response with a message
    return jsonify(message='K8s!')

# Run the application if this script is executed directly
if __name__ == '__main__':
    # Start the Flask development server on host 0.0.0.0 and port 5000 with debug mode enabled
    app.run(host='0.0.0.0', port=5000, debug=True)