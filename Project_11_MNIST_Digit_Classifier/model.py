from tensorflow.keras.datasets import mnist
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import joblib

# Load MNIST (real handwritten digits, 28x28)
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Flatten for SVM
X_train = X_train.reshape(-1, 28*28) / 255.0
X_test = X_test.reshape(-1, 28*28) / 255.0

# Train small SVM
model = SVC(kernel='linear', gamma='auto')
model.fit(X_train[:5000], y_train[:5000])  # Use subset for speed

# Save model
joblib.dump(model, "mnist_svm_model.joblib")

# Evaluate
pred = model.predict(X_test[:1000])
print(f"Test Accuracy: {accuracy_score(y_test[:1000], pred):.2f}")
