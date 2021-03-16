import os
import base64
import time

from flask import Flask, render_template_string, request, redirect, url_for

from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/')
def home():
    html = requests.get('http://unkno.com/')
    parser = BeautifulSoup(html.content, 'html.parser')

    fact = parser.find('div', id='content').getText().strip()

    return render_template_string(fact)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
