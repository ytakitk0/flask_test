# coding: utf-8

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def hello():
    # ここが hello.html のコンテンツになる
    # hello.html コンテンツの変数となる title, name を定義する
    title = "flask test"
    name = "Hello World, wise man"
    
    return render_template("hello.html", title=title, name=name)


"""
@app.route("/good")
def good():
    name = "Good"
    return name
"""

if __name__  == "__main__":
    app.run(debug=True)




