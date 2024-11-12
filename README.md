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

I deploy it in a personal k8s cluster running in hetzner, here you have all the config of the cluster:

https://github.com/ioudkerk/workshop-k8s

This is the endpoint to test the API:

URL: https://magneto-hr.aivandrago.me/

```
curl --location 'https://magneto-hr.aivandrago.me/stats'
```

```
curl --location 'https://magneto-hr.aivandrago.me/mutant' \
--header 'Content-Type: application/json' \
--data '{
    "dna": ["ATCAT", "TCATG", "TTATG", "AGAGG", "CCCTA", "TCACT"]
}'
```