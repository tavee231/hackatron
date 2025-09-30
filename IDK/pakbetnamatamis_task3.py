from flask import Flask, render_template
import random
from collections import Counter

app = Flask(__name__)

@app.route('/')
def home():
    # Roll two dice 10 times
    results = [random.randint(1, 6) + random.randint(1, 6) for _ in range(10)]
    frequency = Counter(results)

    return render_template('pakbetnamatamis_task3.html', results=results, frequency=frequency)

if __name__ == '__main__':
    app.run(debug=True)
