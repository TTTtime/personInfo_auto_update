# encoding=gbk

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/main/')
def login():
    return 'hello,world'

@app.route('/main/get/')
def get_html():
    return render_template('get.html')

@app.route('/main/post/')
def post_html():
    return render_template('post.html')

@app.route('/main/deal_request/', methods = ['GET', 'POST'])
def deal_request():
    if request.method == "GET":
        test = request
        get_q = request.args.get("q","")
        return render_template("result.html", result=get_q)
    elif request.method == "POST":
        post_q = request.form["q"]
        return render_template("result.html", result=post_q)

if __name__ == '__main__':
    app.run(host='172.16.231.220', port=5000, debug=True)
