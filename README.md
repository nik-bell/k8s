# Flask Application with Docker and Kubernetes

This project contains a simple Flask application that is containerized using Docker and can be deployed to Kubernetes.

## Project Structure
- `app.py`: The main Flask application.
- `Dockerfile`: Docker configuration to containerize the application.
- `requirements.txt`: Python dependencies for the application.

## How to Run

### Using Docker
1. Build the Docker image:
   ```bash
   docker build -t flask-app .
   ```
2. Run the Docker container:
   ```bash
   docker run -p 5000:5000 flask-app
   ```

### Using Kubernetes
1. Create a Kubernetes deployment and service configuration.
2. Apply the configuration using `kubectl`.

## API Endpoint
- `GET /api/data`: Returns a JSON response with a message.

## License
This project is licensed under the MIT License.
