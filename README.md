# Magneto HR system

This project is a Flask-based API that analyzes DNA sequences to determine if they belong to a mutant or a human.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Docker
- Docker Compose
- Kubernetes cluster (for deployment)
- Helm (for Kubernetes deployment)

### Running the Application with Docker Compose

1. Clone the repository:
```
git clone https://github.com/ioudkerk/ml-genai.git
cd ml-genai
```

2. Build and run the application using Docker Compose:
```
docker compose up --build
```

3. The application will be available at `http://localhost:5000`

### Running Tests

To run the tests, execute the following command in the project root directory:

```
docker compose run --rm web python -m unittest tests/*
```

This command will run all the tests in the `tests` directory.

### API Endpoints

- POST `/mutant`: Analyze a DNA sequence
  - Request body: `{"dna": ["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]}`
  - Response: `{"mutant": true}` or `{"mutant": false}`

- GET `/stats`: Get statistics about analyzed DNA sequences
  - Response: `{"count_mutant_dna": 40, "count_human_dna": 100, "ratio": 0.4}`


---
## Deployment with GitOps

We use GitOps methodology for deploying and managing our application in Kubernetes. The setup includes ArgoCD, ArgoCD Image Updater, and an ingress controller (Traefik).

### Prerequisites

- Kubernetes cluster
- ArgoCD installed in the cluster
- ArgoCD Image Updater installed
- Traefik Ingress Controller installed

### Repository Structure

```
/
├── deployment/
│   ├── magneto-hr/
│   │   ├── Chart.yaml
│   │   ├── values.yaml
│   │   ├── values-production.yaml
│   │   ├── values-staging.yaml
│   │   └── templates/
│   └── app-of-apps/
│       ├── Chart.yaml
│       ├── values.yaml
│       └── templates/
```

### ArgoCD Setup

1. Create two ArgoCD applications:
   - `magneto-hr-production`
   - `magneto-hr-staging`

2. Create an "App of Apps" to manage both applications:
   - `magneto-hr-apps`

### ArgoCD Image Updater Configuration

Configure ArgoCD Image Updater to watch for new images in the GitHub Container Registry:

- For production: Use semantic versioning (e.g., v1.2.3)
- For staging: Use image digest (e.g., sha256:abc123...)

### Deployment Process

1. Changes are pushed to the `/deploymet` directory in the repository.
2. ArgoCD detects changes and syncs the Kubernetes cluster with the desired state.
3. ArgoCD Image Updater detects new images and updates the Helm values files.
4. ArgoCD syncs the updated configuration to the cluster.

### Environments

- Staging: `https://staging.magneto-hr.meli.com`
- Production: `https://magneto-hr.meli.com`

### Monitoring and Logging

Consider adding monitoring and logging solutions such as Prometheus, Grafana, and LOKI.