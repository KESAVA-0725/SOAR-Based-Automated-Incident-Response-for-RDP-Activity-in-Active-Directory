from flask import Flask, request, jsonify
import subprocess
import json

app = Flask(__name__)

@app.route('/disable_user', methods=['POST'])
def disable_user():
    try:
        # Get incoming data
        data = request.get_json(force=True)

        # Debug logs
        print("RAW DATA:", request.data)
        print("JSON DATA:", data)

        # Fix double-encoded JSON from Tines
        if isinstance(data, str):
            data = json.loads(data)

        print("FIXED DATA:", data)

        # Extract username
        username = list(data.values())[0]

        print("USERNAME:", username)

        # Validate
        if not username:
            return jsonify({"error": "Username missing"}), 400

        # Run PowerShell script
        result = subprocess.run(
            f'powershell -ExecutionPolicy Bypass -Command "Disable-ADAccount -Identity {username}"',
            capture_output=True,
            text=True,
            shell=True
        )

        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)

        # Return result
        return jsonify({
            "output": result.stdout,
            "error": result.stderr
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Run Flask server
app.run(host='0.0.0.0', port=5000)
