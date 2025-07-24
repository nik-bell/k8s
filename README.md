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
   docker build -t k8s:v1 .
   ```

### Using Kubernetes
Apply the configuration using `kubectl`.

## Deploying to Kubernetes with Localhost Access

1. Apply the pod:
   ```bash
   kubectl apply -f pod.yml
   ```

2. Apply the deployment:
   ```bash
   kubectl apply -f deployment.yml
   ```


3. Apply the service:
   ```bash
   kubectl apply -f service.yml
   ```

### Access the Application
1. Find the NodePort assigned to the service:
   ```bash
   kubectl get service k8s-service
   ```
2. Access the application in your browser using `http://localhost:5000`.

## API Endpoint
- `GET /api/data`: Returns a JSON response with a message.

## License
This project is licensed under the MIT License.
