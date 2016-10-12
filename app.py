from flask import (Flask, render_template,
                   redirect,url_for,request)
import json
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('test.html')

@app.route('/save',methods=['POST'])
def save():
    return redirect(url_for('index'))

app.run(debug=True)