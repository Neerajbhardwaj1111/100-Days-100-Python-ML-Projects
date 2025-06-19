# Password Strength Analyzer & Manager

A web application that analyzes password strength, generates strong passwords, and securely stores credentials with encryption.

## Features

- **Password Strength Analysis**: Evaluates passwords based on length, character diversity, and complexity
- **Suggestions for Improvement**: Provides actionable feedback to strengthen weak passwords
- **Password Generation**: Creates secure, randomized passwords with all required character types
- **Secure Storage**: Encrypts and saves username/password combinations using Fernet encryption
- **Encrypted Storage**: All credentials are saved in `saved_password.txt` with strong encryption
- **Responsive Design**: Works well on both desktop and mobile devices

## Technologies Used

- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Python, Flask
- **Security**: Fernet symmetric encryption (from cryptography.fernet)
- **Password Analysis**: Regular expressions for pattern matching
