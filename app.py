from flask import Flask, jsonify
import sqlalchemy as db

engine = db.create_engine('postgresql://scott:tiger@localhost/mydatabase')

app = Flask(__name__)

@app.route('/kings', methods=['GET'])
def get_kings():
    return jsonify([{'name': 'chola'}, {'name': 'pandya'}])

@app.route('/siddhas', methods=['GET'])
def get_siddhas():
    return jsonify([{'name': 'Shivan'}, {'name': 'Murugan'}])


if __name__ == '__main__': app.run()