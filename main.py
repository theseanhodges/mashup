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

def Piglatinize(text):
    html = requests.post(
        'https://hidden-journey-62459.herokuapp.com/piglatinize/',
        data={'input_text': text}
    )
    url = html.url

    parser = BeautifulSoup(html.content, 'html.parser')
    return url, parser.find('h2').nextSibling.strip()

@app.route('/')
def home():
    # When you said 'clickable link' I took that to mean presenting the piglatinized fact and
    # linking that back to the piglatinizer, so that's what this is doing.
    return render_template_string('<a href="{}">{}</a>'.format(
        *Piglatinize(GetFact())
    ))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
