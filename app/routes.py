from flask import Blueprint

hello_world_bp = Blueprint("hello_world", __name__)#1"hello_world_bp" is our local variable thats going to store a blueprint instance
#2 "Blueprint" is us creating a blueprint instance. Blueprint is the name of the class
#3"hello_world" is basically going to be some identifier or name for the blueprint
#4"__name__" is just what you use universally 

@hello_world_bp.route('/hello-world', methods=["GET"])#using a blueprint decorator. "@" is the decorator ".route" given is '/hello-world'. "methods" is for defining the method you want to design, which is "GET"
def get_hello_world():
    my_response="Hello, World!"
    return my_response

@hello_world_bp.route('/hello-world/JSON', methods=["GET"])
def hello_world_json():
    return {
        "name": "Alma",
        "message": "sup",
        "hobbies": ["reading", "laughing", "listen to music"],
    }, 200#"200" is the status code 