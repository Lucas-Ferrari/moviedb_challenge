from flask import jsonify, request

USERS = {
    "1": {"token": "abcdef1234567890", "role": "ADMIN"},
    "2": {"token": "1234567890", "role": "USER"},
}


def check_token():
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        return jsonify({"error": "Missing token"}), 401

    token = auth_header.split()[1]
    user = next((u for u in USERS.values() if u["token"] == token), None)
    if not user:
        return jsonify({"error": "Invalid token"}), 401

    return user
