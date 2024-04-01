from flask import Flask, render_template, request
from cryptography.fernet import Fernet

app = Flask(__name__)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    message = request.form['message']
    encrypted_message = encrypt_message(message)
    return render_template('result.html', message=encrypted_message, action='Encrypted')

@app.route('/decrypt', methods=['POST'])
def decrypt():
    encrypted_message = request.form['encrypted_message']
    decrypted_message = decrypt_message(encrypted_message)
    return render_template('result.html', message=decrypted_message, action='Decrypted')

def encrypt_message(message):
    encrypted_text = cipher_suite.encrypt(message.encode())
    return encrypted_text.decode()

def decrypt_message(encrypted_message):
    decrypted_text = cipher_suite.decrypt(encrypted_message.encode())
    return decrypted_text.decode()

if __name__ == '__main__':
    app.run(debug=True)
