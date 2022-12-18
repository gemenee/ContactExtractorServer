from app import app
from flask import jsonify, request
import pymorphy2

morph = pymorphy2.MorphAnalyzer()

from app.Extractor import extractor


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/morphy/inflect')
def morphy():
    if request.method == 'GET':
        decodedRerquest = request.data.decode('utf-8')
        word = request.values.get('word')
        num = request.values.get('num') or 'sing'
        case = request.values.get('case') or 'nomn'
        inflectedWord = morph.parse(word)[0].inflect({num, case}).word
        return jsonify(inflected=inflectedWord)
