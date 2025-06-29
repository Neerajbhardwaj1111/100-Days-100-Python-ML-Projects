import pandas as pd
import re
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


df = pd.read_csv("spam_Emails_data.csv", encoding='latin-1')
df.columns = ['label', 'text']
df = df.dropna(subset=['text']) 

def clean_text(text):
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r'\\n', ' ', text)
    text = re.sub(r'escapenumber', '', text)
    text = re.sub(r'\W+', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text



df['clean_text'] = df['text'].apply(clean_text)

label_encoder = LabelEncoder()
df['label'] = label_encoder.fit_transform(df['label'])  # Ham=0, Spam=1


tfidf = TfidfVectorizer(stop_words='english', max_df=0.7)
X = tfidf.fit_transform(df['clean_text'])
y = df['label']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = LogisticRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("📊 Accuracy:", accuracy_score(y_test, y_pred))
print("\n📋 Classification Report:\n", classification_report(y_test, y_pred))
print("\n🧾 Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

def predict_spam(message):
    cleaned = clean_text(message)
    vector = tfidf.transform([cleaned])
    prediction = model.predict(vector)[0]
    return "Spam" if prediction == 1 else "Not Spam"


test_samples = [
    "Congratulations! You've won a $1000 Walmart gift card. Click here to claim now!",
    "Hey, can we reschedule our meeting to 3 PM tomorrow?",
    "Urgent! Your account has been suspended. Verify immediately.",
    "I'm running late, stuck in traffic. Will join soon.",
    "Buy 1 Get 1 Free!!! Limited time offer. Hurry up!",
    "Let's catch up for coffee this weekend!",
    "Lowest prices on medicines, only at spampharmacy.com!",
    "Reminder: Your doctor's appointment is tomorrow at 10 AM.",
    "Earn money from home. No investment. Start today!",
    "Good morning, just checking in. Have a great day!",
    "Your package is waiting for pickup. Confirm your address.",
    "We need your feedback. Complete our survey and win ₹500!",
    "Are you available for a quick call this afternoon?",
    "You've been selected for a free iPhone 15 Pro!",
    "Final notice! Renew your subscription to avoid service disruption."
]


print("\n🔮 Predictions:")
for msg in test_samples:
    print(f"{msg} => {predict_spam(msg)}")
