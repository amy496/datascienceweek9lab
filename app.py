from flask import Flask, render_template, url_for

app = Flask()

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/base')
def base():
    return request.method

if __name__ == '__main__':
    app.run(debug=True)