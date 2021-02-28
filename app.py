from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
import requests


app = Flask(__name__)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.DBFINDA

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/result')
def return_result():
    return render_template('result.html')

@app.route('/search')
def retrun_search():
    return render_template('search.html')

@app.route('/getdb')
def return_getdb():
    return render_template('scraping.html')

@app.route('/getdb',methods=['POST'])
def post_db():
   poster_receive = request.form['poster_give']
   title_receive = request.form['title_give']
   year_receive = request.form['year_give']
   director_receive = request.form['director_give']
   genre_receive = request.form.getlist('genre_give[]')
   actor_receive = request.form.getlist('actor_give[]')
   platformname_receive = request.form.getlist('platformName_give[]')
   iconurl_receive = request.form['iconUrl_give']
   desc_receive = request.form['desc_give']

   doc = {
       'poster': poster_receive,
       'title': title_receive,
       'year': year_receive,
       'director': director_receive,
       'genre': genre_receive,
       'actor': actor_receive,
       'platformname': platformname_receive,
       'iconurl': iconurl_receive,
       'desc': desc_receive
   }
   db.movie.insert_one(doc)

   return jsonify({'result': 'success', 'msg': 'db에 잘 들어감!'})

@app.route('/search/movie', methods=['GET'])
def get_search_data():
    search_receive = request.args.get('search_give')
    search_list = list(db.movie.find({'$or':[ {'title': {'$regex': search_receive}}]},{'_id': False}))
    return jsonify({'result': 'success', 'data': search_list})













if __name__ == '__main__':
    app.run('0.0.0.0',port=5000, debug=True)