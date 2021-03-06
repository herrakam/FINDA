from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient


app = Flask(__name__)
aws_client = MongoClient('mongodb://test:test@54.180.112.223', 27017)
db = aws_client.DBFINDA



@app.route('/')
def home():
    return render_template('main.html')

@app.route('/detail')
def return_result():
    return render_template('detail.html')

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
   iconurl_receive = request.form.getlist('iconUrl_give[]')
   desc_receive = request.form['desc_give']
   # reviews_receive = request.form.getlist('reviews_give[]')

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
    search_receive = request.args.get('search_give', '')
    page_receive = int(request.args.get('page_give', 1))
    size_receive = int(request.args.get('size_give', 30))
    n_skip = size_receive * (page_receive - 1)
    total = db.movie.count()
    search_list = list(db.movie.find({
        '$or': [{'title': {'$regex': search_receive}}]
    }, {
        '_id': False
    }).skip(n_skip).limit(size_receive))
    return jsonify({'result': 'success', 'data': search_list, 'total': total})

@app.route('/recommend/movie', methods=['GET'])
def get_recommend_data():
    recommend_receive = request.args.getlist('recommend_give[]')
    page_receive = int(request.args.get('page_give', 1))
    size_receive = int(request.args.get('size_give', 30))
    n_skip = size_receive * (page_receive - 1)
    total = db.movie.count()
    recommend_list = list(db.movie.find({
        '$and': [
            {'genre': {'$in': [recommend]}} for recommend in recommend_receive
        ]
    }, {
        '_id': False
    }).skip(n_skip).limit(size_receive))
    return jsonify({'result': 'success', 'data': recommend_list, 'total': total})

@app.route('/review', methods=['POST'])
def write_review():
    review_receive = request.form['review_give']
    title_receive = request.form['title_give']
    db.movie.update({'title':title_receive},{'$push' : {'reviews':review_receive}})
    return jsonify({'result': 'success', 'msg': '리뷰가 성공적으로 작성되었습니다.'})













if __name__ == '__main__':
    app.run('0.0.0.0',port=5000, debug=True)