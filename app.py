from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/home')
def index():
    return render_template('home.html')
    


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/base')
def base():
    return render_template('base.html')

if __name__ == "__main__":
    app.run(debug = True)