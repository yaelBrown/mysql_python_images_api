from flask import Flask, Blueprint

imageController = Blueprint('imageController', __name__)

class imageController(): 
  @imageController.route('/test', )
  def test():
    return {'msg': 'this test works'}, 200

  @imageController.route('/add' methods=['POST'])
  def add():
    return {'msg': 'add route works'}, 200

  