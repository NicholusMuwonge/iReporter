from api import mod
from api import creat_app

app = creat_app()
app.register_blueprint(mod)

if __name__ == "__main__":
    app.run(debug=True)