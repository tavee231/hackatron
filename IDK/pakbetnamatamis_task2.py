from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    numbers = list(range(1, 11))
    even_numbers = [num for num in numbers if num % 2 == 0]
    return render_template('pakbetnamatamis_task2.html', numbers=numbers, even_numbers=even_numbers)

if __name__ == '__main__':
    app.run(debug=True)
