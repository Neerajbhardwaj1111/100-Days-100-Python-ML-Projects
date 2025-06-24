🚢 Titanic Survival CLI Predictor

A command-line machine learning tool that predicts whether a passenger would survive the Titanic disaster based on their class, age, gender, fare, and boarding location.

This project uses the Titanic dataset and a trained Random Forest Classifier to make survival predictions through simple user input.

🧠 Features

Takes real-time passenger details as CLI input

Encodes and preprocesses categorical data safely

Predicts survival using a Random Forest model

Handles invalid inputs and missing data

Future-proof pandas usage (no chained assignment warnings)

📁 Dataset

This project uses the Kaggle Titanic dataset:

Place the train.csv file in the same directory as the script.

⚙️ How It Works

The script trains a model on the Titanic dataset using features like:

Pclass (Passenger class)

Sex

Age

SibSp (Siblings/Spouses aboard)

Parch (Parents/Children aboard)

Fare

Embarked (Boarding port)

You enter a new passenger’s details in the terminal.

The model predicts whether the passenger would survive.
