"""Small demo service deployed through the GitOps pipeline."""
import os
import socket

from flask import Flask, jsonify

app = Flask(__name__)

APP_VERSION = os.getenv("APP_VERSION", "dev")
ENVIRONMENT = os.getenv("ENVIRONMENT", "local")


@app.get("/")
def index():
    return jsonify(
        message="Hello from the GitOps demo app",
        version=APP_VERSION,
        environment=ENVIRONMENT,
        pod=socket.gethostname(),
    )


@app.get("/healthz")
def healthz():
    """Liveness: the process is up."""
    return jsonify(status="ok")


@app.get("/readyz")
def readyz():
    """Readiness: the app can serve traffic."""
    return jsonify(status="ready")


@app.get("/version")
def version():
    return jsonify(version=APP_VERSION)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "8080")))
