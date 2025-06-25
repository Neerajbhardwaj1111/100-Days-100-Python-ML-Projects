import tkinter as tk
from PIL import Image, ImageDraw, ImageOps
import numpy as np
import joblib

model = joblib.load("mnist_svm_model.joblib")

class DigitRecognizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MNIST Digit Recognizer")

        self.canvas_width = 200
        self.canvas_height = 200

        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack()

        self.image = Image.new("L", (self.canvas_width, self.canvas_height), color=255)
        self.draw = ImageDraw.Draw(self.image)

        self.canvas.bind("<B1-Motion>", self.paint)

        tk.Button(root, text="Predict", command=self.predict).pack()
        tk.Button(root, text="Clear", command=self.clear).pack()
        self.label = tk.Label(root, text="", font=("Helvetica", 20))
        self.label.pack()

    def paint(self, event):
        x, y = event.x, event.y
        r = 10
        self.canvas.create_oval(x - r, y - r, x + r, y + r, fill="black")
        self.draw.ellipse([x - r, y - r, x + r, y + r], fill=0)

    def clear(self):
        self.canvas.delete("all")
        self.draw.rectangle([0, 0, self.canvas_width, self.canvas_height], fill=255)
        self.label.config(text="")

    def predict(self):
        img = self.image.resize((28, 28), Image.Resampling.LANCZOS)
        img = ImageOps.invert(img)
        img_array = np.array(img).reshape(1, -1) / 255.0  # Normalize

        pred = model.predict(img_array)[0]
        self.label.config(text=f"Predicted: {pred}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DigitRecognizerApp(root)
    root.mainloop()
