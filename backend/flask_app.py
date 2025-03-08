import hashlib
import hmac
import os

import git
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


def verify_signature(payload_body, secret_token, signature_header):
    hash_algorithm, github_signature = signature_header.split('=', 1)
    algorithm = hashlib.__dict__.get(hash_algorithm)
    encoded_key = bytes(secret_token, 'latin-1')
    mac = hmac.new(encoded_key, msg=payload_body, digestmod=algorithm)
    return hmac.compare_digest(mac.hexdigest(), github_signature)


# GitHub Webhook Route
@app.route("/release_created", methods=["POST"])
def release_created():
    """
    This route is used to receive GitHub webhook events for new releases.
    :return:
    """
    data = request.json  # Get JSON payload from GitHub webhook
    headers = request.headers
    if not verify_signature(data, os.getenv("WEBHOOK_SECRET"), headers.get("X-Hub-Signature")):
        return jsonify({"error": "Invalid payload"}), 400
    if not data:
        return jsonify({"error": "Invalid payload"}), 400

    # Extract relevant data
    print(f"Data received: {data}")
    release_name = data.get("release", {}).get("name", "Unknown Release")
    repository = data.get("repository", {}).get("full_name", "Unknown Repo")

    print(f"New release created: {release_name} in {repository}")

    repo = git.Repo('/home/pratyusha792/pratyusha972.github.io')
    origin = repo.remotes.origin
    origin.pull()

    print(f"Updated repository")

    # Return a success response
    return jsonify({"message": "Release received", "release": release_name, "repository": repository}), 200


@app.route("/live_demo")
def live_demo():
    return render_template("index.html")


@app.route("/")
def home():
    return render_template("index.html")

# if __name__ == '__main__':
#     app.run()
