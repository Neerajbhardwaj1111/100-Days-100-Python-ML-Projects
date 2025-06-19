from flask import Flask,render_template,request,jsonify
from password_utils import analyze_password_strength, generate_password, save_credentials, get_saved_credentials

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check_strength',methods=['POST'])
def check_strength():
    password= request.json['password']
    strength,suggestions = analyze_password_strength(password)
    return jsonify({'strength':strength,'suggestions':suggestions})

@app.route('/generate_password')
def generate_strong_password():
    password = generate_password()
    return jsonify({'password': password})

@app.route('/save_password', methods=['POST'])
def save_password():
    data = request.json
    username = data['username']
    password = data['password']
    save_credentials(username, password)
    return jsonify({'status': 'success'})

@app.route('/get_passwords')
def get_passwords():
    credentials = get_saved_credentials()
    return jsonify({'credentials': credentials})

if __name__ == '__main__':
    app.run(debug=True)