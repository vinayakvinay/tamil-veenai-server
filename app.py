import settings
from flask import Flask, jsonify, request
import datetime
from base import Session, engine, Base
from models.articles import Article

Base.metadata.create_all(engine)
session = Session()

app = Flask(__name__)


@app.route('/kings', methods=['GET'])
def get_kings():
    king = Article(title='Karikaalan', description='He is a greatest king of the world',
                   created_at=datetime.datetime.now())
    session.add(king)
    session.commit()
    session.close()
    return jsonify([{'name': 'chola'}, {'name': 'pandya'}])


@app.route('/siddhas', methods=['GET'])
def get_siddhas():
    return jsonify([{'name': 'Shivan'}, {'name': 'Murugan'}])


@app.route('/add_article', methods=['POST'])
def add_article():
    req_body = request.get_json()
    title = req_body['title']
    description = req_body['description']
    tag = req_body['tag']
    category = req_body['category']
    claps = req_body['claps']
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()

    article = Article(title=title, description=description, tag=tag, category=category, claps=claps,
                      created_at=created_at, updated_at=updated_at)
    session.add(article)
    session.commit()
    session.close()
    return 'done'


if __name__ == '__main__': app.run()
