from flask import Flask, request
app = Flask(__name__)

# for test
@app.route("/")
def hello():
    return "Hello World!"

# echo server
@app.route("/token")
def token():
    return request.args.get('text', '')

if __name__ == "__main__":
    app.run(port=8080)
