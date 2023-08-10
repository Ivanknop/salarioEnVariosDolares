from flask import Flask,redirect,url_for,render_template,request
from dolar_converter  import Dolar_converter

app=Flask(__name__)

@app.route("/")
def index():
    dolar_today = Dolar_converter()
    return render_template('index.html',data=dolar_today.show_quote())

@app.route("/calculate",methods=['POST'])
def calculate():
    salary = request.args.get('salary')
    salary_in_dolars = Dolar_converter(salary)
    salary_in_dolars.calculate()
    return render_template('conversion.html',data = salary_in_dolars.show_quote())

def run():
    app.run(host="3.15.183.16",port=5000,threaded=True)