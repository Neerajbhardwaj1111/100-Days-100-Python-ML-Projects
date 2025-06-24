import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

def load_and_prepare_data():
    df = pd.read_csv("train.csv").copy()

    # Safe missing value filling (FutureWarning-proof)
    df = df.fillna({
        "Age": df["Age"].median(),
        "Embarked": df["Embarked"].mode()[0]
    })

    # Drop unnecessary columns
    df = df.drop(columns=["PassengerId", "Name", "Ticket", "Cabin"])

    # Encode categorical columns properly
    le_sex = LabelEncoder()
    le_embarked = LabelEncoder()

    df["Sex"] = le_sex.fit_transform(df["Sex"].astype(str))
    df["Embarked"] = le_embarked.fit_transform(df["Embarked"].astype(str))

    X = df.drop("Survived", axis=1)
    y = df["Survived"]

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)

    return model, le_sex, le_embarked

def predict_survival(model, le_sex, le_embarked):
    print("\n🎫 Enter passenger details:")
    pclass = int(input("Passenger Class (1, 2, 3): "))
    sex = input("Sex (male/female): ").strip().lower()
    age = float(input("Age: "))
    sibsp = int(input("Siblings/Spouses aboard: "))
    parch = int(input("Parents/Children aboard: "))
    fare = float(input("Fare £3-£500: £"))
    embarked = input("Embarked or boarding (Cherbourg, Queenstown, Southampton)(C, Q, S): ").strip().upper()

    try:
        sex_encoded = le_sex.transform([sex])[0]
        embarked_encoded = le_embarked.transform([embarked])[0]
    except ValueError:
        print("❌ Error: Invalid input for sex or embarked.")
        return

    passenger = pd.DataFrame([{
        "Pclass": pclass,
        "Sex": sex_encoded,
        "Age": age,
        "SibSp": sibsp,
        "Parch": parch,
        "Fare": fare,
        "Embarked": embarked_encoded
    }])

    prediction = model.predict(passenger)[0]
    print("\n🧾 Prediction: ", "🟢 Survived" if prediction == 1 else "🔴 Did Not Survive")

if __name__ == "__main__":
    print("🚢 Titanic Survival CLI Predictor")
    model, le_sex, le_embarked = load_and_prepare_data()
    predict_survival(model, le_sex, le_embarked)
