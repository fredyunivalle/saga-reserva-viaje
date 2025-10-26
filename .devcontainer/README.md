# Codespaces instructions for saga-reserva-viaje

This folder contains the Codespaces / devcontainer configuration that makes it easy to run the Docker Compose stack inside a Codespace.

What the devcontainer does
- Installs Docker-in-Docker so `docker` and `docker compose` are available inside the Codespace container.
- Forwards service ports: 5000 (orchestrator), 5001 (flight), 5002 (hotel), 5003 (car).
- Runs `docker compose up -d --build` automatically after the Codespace starts.

How to use
1. In GitHub, click **Code → Open with Codespaces** and create a new Codespace for this repo/branch.
2. Wait for the devcontainer build to complete. The stack will be started automatically.
3. Use the forwarded ports to access services from the Codespace.

Manual commands (inside the Codespace terminal)

```bash
# Start services manually
docker compose up --build

# Stop services
docker compose down
```

Notes
- Codespaces runs the devcontainer inside a container; the `docker-in-docker` feature is used to provide Docker inside that environment.
- Organization policies or Codespaces plan limits may affect Docker/privileged operations; consult your GitHub admin if you encounter permission issues.
