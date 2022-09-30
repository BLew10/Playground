from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/play')
def play(color = 'blue', num = 3):
    return render_template("index.html", color = color, num = num)

@app.route('/play/<int:num>')
def playInt(num, color = 'blue'):
    return render_template("index.html", color = color, num = num)
    
@app.route('/play/<int:num>/<string:color>')
def playColorInt(num, color):
    return render_template("index.html", color = color, num = num)


if __name__ == "__main__":
    app.run(debug=True)
