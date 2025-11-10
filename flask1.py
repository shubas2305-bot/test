from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello Social Eagles, I'm Shuba and this is my first API!"

if __name__ == '__main__':
    app.run(debug=True)




