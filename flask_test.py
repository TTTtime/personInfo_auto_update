# encoding=gbk

from flask import Flask
from flask import render_template
from flask import request
import json

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

@app.route('/main/deal_request', methods = ['GET', 'POST'])
def deal_request():
    test = request
    return_dict = {}
    if request.method == "GET":
        get_q = request.args.get("q","")
        return render_template("result.html", result=get_q)
    elif request.method == "POST":
        return_dict['function'] = request.form["function"]
        return_dict['download_dir'] = request.form["download_dir"]
        return_dict['download_dir_start_num'] = request.form["download_dir_start_num"]
        return_dict['download_pic_group'] = request.form["download_pic_group"]
        return_dict['download_start'] = request.form["download_start"]
        return_dict['download_end'] = request.form["download_end"]
        return_dict['download_type'] = request.form["download_type"]
        return json.dumps(return_dict)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
