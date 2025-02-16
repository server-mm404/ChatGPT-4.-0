from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# Define the strong password criteria
PASSWORD_REGEX = re.compile(
    r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
)

def is_strong_password(password):
    return PASSWORD_REGEX.match(password) is not None

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    if not is_strong_password(password):
        return jsonify({"error": "Password must be at least 8 characters long, "
                                 "contain at least one uppercase letter, one lowercase letter, "
                                 "one number, and one special character"}), 400

    # Here you would add code to save the user to your database
    # For now, we'll just return a success message
    return jsonify({"message": "User signed up successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)