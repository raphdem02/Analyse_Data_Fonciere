from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
@app.route('/about/')
def index():
    return render_template('about.html')

@app.route('/2018/')
def data2017():
    return render_template('2018.html')

@app.route('/2019/')
def data2018():
    return render_template('2019.html')

@app.route('/2020/')
def data2019():
    return render_template('2020.html')

@app.route('/2021/')
def data2020():
    return render_template('2021.html')

@app.route('/2022/')
def data2021():
    return render_template('2022.html')

@app.route('/comparaison/')
def datacomp():
    return render_template('comp.html')