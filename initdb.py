from pymongo import MongoClient
aws_client = MongoClient('mongodb://test:test@192.32.19.21', 27017)
aws_db = aws_client.DBFINDA
local_client = MongoClient('localhost', 27017)
local_db = local_client.DBFINDA
local_movies = local_db.movie.find()
aws_db.movie.insert_many(local_movies)