from flask import Flask

spark = Flask(__name__)
spark.api_secret = "ODIyOTJjZDA5ZWQ5NWU5MjVlOGMyNjgx"
spark.api_key = "86a20fef1c407cc12d999c28af5c1be9"

@spark.route('/chat/synthesis/')
def hello_world():
    return 'Hello, World!'
@spark.route('/chat/llm/')
def hello_world():
    return 'Hello, World!'
@spark.route('/chat/llm/basic/')
def hello_world():
    return 'Hello, World!'
@spark.route('/chat/recognize/')
def hello_world():
    return 'Hello, World!'