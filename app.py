from flask import Flask, render_template, request, abort

app = Flask(__name__)

# Hardcoded credentials (for demonstration purposes only)
VALID_USERNAME = "admin"
VALID_PASSWORD = "supersecurepassword123"

# Route for the homepage
@app.route('/')
def index():
    return render_template("index.html")

# Route for robots.txt
@app.route('/robots.txt')
def robots():
    return "VALID_USERNAME = "admin"
VALID_PASSWORD = "supersecurepassword123""

# Route for the vault (hidden flag)
@app.route('/vault')
def vault():
    # Check if the user is authenticated
    auth = request.authorization
    if auth and auth.username == VALID_USERNAME and auth.password == VALID_PASSWORD:
        # Return the flag if authenticated
        return "uacCTF{h1dden_vAulT_bypAssEd}"
    else:
        # Return a 401 Unauthorized response
        return abort(401, "Unauthorized: Access to the vault requires authentication.")

# Route for a fake admin page
@app.route('/admin')
def admin():
    return "Nothing to see here. Move along."

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4444)
