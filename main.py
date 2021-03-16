import os
import base64
import time

from flask import Flask, render_template_string, request, redirect, url_for

from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

def GetFact():
    html = requests.get('http://unkno.com/')
    parser = BeautifulSoup(html.content, 'html.parser')

    return parser.find('div', id='content').getText().strip()

@app.route('/')
def home():
    return render_template_string(GetFact())

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
