from flask import Flask
from flask_mysqldb import MySQL
from .imageController import imageController

app = Flask(__name__)

mysql = MySQL(app)

app.register_blueprint(imageController, url_prefix='/api/v1/images')

@app.route('/')
def home():
  return 'Server is working', 200

if __name__ == "__main__":
  app.run(debug=True)