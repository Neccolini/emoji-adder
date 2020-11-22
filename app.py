#app.py
from flask import Flask, request, session,render_template
import urllib
from flask import abort, redirect, url_for
import numpy as np


from io import BytesIO
import pandas as pd
from datetime import datetime, timedelta
from emoji_output import emoji_output
app = Flask(__name__)
@app.route("/calc",methods=["POST","GET"])
def index():
    if request.method=="POST":
        emoji_num=request.form["num"]
        text=request.form["text"]
        text_emoji=emoji_output(text,emoji_num)
        return render_template('result.html',text_emoji=text_emoji)
    else:return render_template("index.html")

if __name__ == "__main__":
    app.run(port=5005)
