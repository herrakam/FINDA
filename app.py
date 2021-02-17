from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/main')
def return_main():
    return render_template('main.html')

@app.route('/result')
def return_result():
    return render_template('result.html')

@app.route('/search')
def retrun_search():
    return render_template('search.html')

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000, debug=True)