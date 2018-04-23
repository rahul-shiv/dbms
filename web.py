from flask import Flask, render_template, request
import sqlite3 as sqlite3
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/animal')
def animal():
    return render_template('animal.html')

@app.route('/employee')
def employee():
    return render_template('employee.html')

@app.route('/tourist')
def tourist():
    return render_template('tourist.html')

@app.route('/bill')
def bill():
    return render_template('bill.html')

if __name__ == '__main__':
    app.run(debug=True)
