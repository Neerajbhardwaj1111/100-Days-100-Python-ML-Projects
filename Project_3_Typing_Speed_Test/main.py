from flask import Flask, render_template, request, jsonify
import random
from quote import quotes

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/get_text')
def get_text():
    # Return 10 random quotes joined as a paragraph
    selected_quotes = random.sample(quotes, min(10, len(quotes))) if quotes else ["Sample text for typing test."]*10
    return ' '.join(selected_quotes)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    if not data or 'typedText' not in data or 'originalText' not in data or 'time' not in data:
        return jsonify({"error": "Invalid request data"}), 400
    
    try:
        typed_text = data['typedText'].strip()
        original_text = data['originalText'].strip()
        elapsed_time = float(data['time'])
        
        if elapsed_time <= 0:
            return jsonify({"error": "Time must be positive"}), 400

        # Character-level comparison
        correct_chars = 0
        min_length = min(len(typed_text), len(original_text))
        for i in range(min_length):
            if typed_text[i] == original_text[i]:
                correct_chars += 1
        
        # Word-level comparison
        typed_words = typed_text.split()
        original_words = original_text.split()
        correct_words = 0
        min_word_length = min(len(typed_words), len(original_words))
        for i in range(min_word_length):
            if typed_words[i] == original_words[i]:
                correct_words += 1

        # Calculate metrics
        gross_wpm = (len(typed_words) / (elapsed_time / 60)) if elapsed_time > 0 else 0
        net_wpm = ((correct_chars / 5) / (elapsed_time / 60)) if elapsed_time > 0 else 0
        cpm = (correct_chars / elapsed_time * 60) if elapsed_time > 0 else 0
        accuracy = (correct_words / len(typed_words) * 100) if original_words else 0

        return jsonify({
            "wpm": round(net_wpm, 2),
            "cpm": round(cpm, 2),
            "accuracy": round(accuracy, 2),
            "gross_wpm": round(gross_wpm, 2),
            "correct_words": correct_words,
            "total_words": len(original_words)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)