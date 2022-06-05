from flask import Flask, redirect, render_template, request, url_for, flash, session, abort


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('login_screen.html')

  
if __name__ == "__main__":
    app.run(debug=True)