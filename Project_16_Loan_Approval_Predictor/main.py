import pandas as pd
import xgboost as xgb
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

MODEL_FILE = "model.pkl"
ENCODER_FILE = "encoders.pkl"

def train_model():
    print("\n📚 Loading and training on loan.csv...")
    df = pd.read_csv("data.csv")

    # Drop unnecessary column
    if 'Loan_ID' in df.columns:
        df.drop('Loan_ID', axis=1, inplace=True)

    df.fillna(method='ffill', inplace=True)

    # Encode all object columns with separate LabelEncoders
    encoders = {}
    for col in df.select_dtypes(include='object').columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        encoders[col] = le

    # Split into features and target
    X = df.drop("Loan_Status", axis=1)
    y = df["Loan_Status"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss')
    model.fit(X_train, y_train)

    # Save model and encoders
    joblib.dump((model, X.columns.tolist()), MODEL_FILE)
    joblib.dump(encoders, ENCODER_FILE)

    # Evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"✅ Model trained and saved ({MODEL_FILE}, {ENCODER_FILE})")
    print(f"🎯 Accuracy on test set: {accuracy:.2f}")

def predict_from_input():
    if not os.path.exists(MODEL_FILE) or not os.path.exists(ENCODER_FILE):
        print("⚠️ Model or encoders not found. Training now...")
        train_model()

    model, feature_names = joblib.load(MODEL_FILE)
    encoders = joblib.load(ENCODER_FILE)

    # Example values for user reference
    example_values = {
        "Gender": "Male / Female",
        "Married": "Yes / No",
        "Dependents": "0 / 1 / 2 / 3+",
        "Education": "Graduate / Not Graduate",
        "Self_Employed": "Yes / No",
        "ApplicantIncome": "e.g. 5000",
        "CoapplicantIncome": "e.g. 1500",
        "LoanAmount": "e.g. 120",
        "Loan_Amount_Term": "e.g. 360",
        "Credit_History": "1.0 (good) / 0.0 (bad)",
        "Property_Area": "Urban / Semiurban / Rural"
    }

    print("\n📝 Enter loan application details below:")

    input_data = []
    for feature in feature_names:
        ex = example_values.get(feature, "")
        prompt = f"{feature} ({ex}): " if ex else f"{feature}: "

        val = input(prompt).strip()
        try:
            val = float(val)
        except:
            if feature in encoders:
                le = encoders[feature]
                if val in le.classes_:
                    val = le.transform([val])[0]
                else:
                    print(f"⚠️ Unknown value '{val}' for '{feature}'. Defaulting to '{le.classes_[0]}'")
                    val = le.transform([le.classes_[0]])[0]
            else:
                print(f"⚠️ Unknown feature '{feature}', defaulting to 0.")
                val = 0
        input_data.append(val)

    prediction = model.predict([input_data])[0]
    result = "✅ Approved" if prediction == 1 else "❌ Rejected"
    print(f"\n📌 Loan Status Prediction: {result}")

if __name__ == "__main__":
    print("\n🎯 === Loan Approval Predictor === 🎯\n")
    print("Select an option:")
    print("1. Train the model on data.csv")
    print("2. Predict loan status for a new applicant\n")

    while True:
        choice = input("🔢 Enter your choice (1 or 2): ").strip()

        if choice == "1":
            train_model()
            break

        elif choice == "2":

            predict_from_input()

            again = input("\n🔁 Do you want to predict another? (y/n): ").lower()
            if again != 'y':
                print("👋 Exiting. Thank you!")
                break
        else:
            print("❌ Invalid choice. Please enter either 1 or 2.\n")

 


