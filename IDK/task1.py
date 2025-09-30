from flask import Flask, render_template

app = Flask(__name__)

def greet(name1, name2):
    return f"Welcome {name1} and {name2} to python world"

@app.route('/')
def home():
    message = greet("Thristan", "Steven")
    return render_template('task1.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)