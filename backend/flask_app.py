from flask import Flask, request, jsonify, render_template
import git
app = Flask(__name__)


# GitHub Webhook Route
@app.route("/release_created", methods=["POST"])
def release_created():
    data = request.json  # Get JSON payload from GitHub webhook
    if not data:
        return jsonify({"error": "Invalid payload"}), 400

    # Extract relevant data
    release_name = data.get("release", {}).get("name", "Unknown Release")
    repository = data.get("repository", {}).get("full_name", "Unknown Repo")

    print(f"New release created: {release_name} in {repository}")

    # Return a success response
    return jsonify({"message": "Release received", "release": release_name, "repository": repository}), 200

@app.route("/live_demo")
def home():
    return render_template("index.html")

@app.route("/")
def home():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
