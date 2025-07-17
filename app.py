
from flask import Flask, request, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

# Mock database to track used serials (replace with real DB in production)
used_serials = set()

# API constants
PASSNINJA_API_URL = "https://api.passninja.com/v1/passes"
API_KEY = "8d1d0dbfa541062c2e13c829b96d20ff"
ACCOUNT_ID = "aid_0xb91"
PASS_TYPE_ID = "ptk_0x231"

@app.route('/redeem', methods=['GET'])
def redeem():
    serial = request.args.get('serial')

    if not serial:
        return jsonify({"error": "Missing serial"}), 400

    if serial in used_serials:
        return jsonify({"message": "Pass already expired or redeemed"}), 403

    # Mark serial as used
    used_serials.add(serial)

    # Prepare expiration time in ISO 8601 format (UTC now)
    expiration_time = datetime.utcnow().isoformat() + "Z"

    # PassNinja request
    url = f"{PASSNINJA_API_URL}/{PASS_TYPE_ID}/{serial}"
    headers = {
        "X-API-KEY": API_KEY,
        "X-ACCOUNT-ID": ACCOUNT_ID,
        "Content-Type": "application/json"
    }
    payload = {
        "pass": {
            "expiration-date": expiration_time,
            "barcode-alt": "This pass has expired"
        }
    }

    response = requests.put(url, headers=headers, json=payload)

    if response.status_code == 200:
        return jsonify({"message": "Pass successfully expired"}), 200
    else:
        return jsonify({"error": "Failed to expire pass", "details": response.text}), 500

if __name__ == "__main__":
    app.run(debug=True)
