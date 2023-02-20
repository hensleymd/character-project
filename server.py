from flask_app import app
from flask_app.controllers import users, characters # import all controllers

if __name__=="__main__":
    app.run(debug=True)