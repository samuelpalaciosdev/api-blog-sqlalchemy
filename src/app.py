from flask import Flask, jsonify, request
from flask_migrate import Migrate
from models import db, Article

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db.init_app(app)
Migrate(app, db) # db init, db migrate, db upgrade

#### code inside this lines ####

@app.route('/api/articles', methods=['GET', 'POST']) 
def list_and_create_post():
    # returns all articles
    if request.method == ('GET'):
        articles = Article.query.all()
        articles = list(map(lambda article: article.serialize(), articles))

        return jsonify(articles), 200 

    # function to create post
    if request.method == ('POST'):
        data = request.get_json()

        article = Article()
        article.title = data['title']
        article.body = data['body']
        article.created_by = data['created_by']

        db.session.add(article)
        db.session.commit()

        return jsonify(article.serialize()), 201


#### code inside this lines ####
if __name__ == '__main__':
    app.run()
