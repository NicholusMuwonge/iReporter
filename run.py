
from flask import Flask,json,jsonify
from api.routes.operations_views import Routes
from api.models.database import DatabaseConnection

app = Flask(__name__)
app.env = 'development'
Routes.generate(app)



@app.before_first_request
def admin():
    data = DatabaseConnection()
    data.check_admin()


@app.route('/')
def index():
    return jsonify({'message': 'Welcome dear concerned citizen'}),200


if __name__ == '__main__':
    app.run(debug=True)
