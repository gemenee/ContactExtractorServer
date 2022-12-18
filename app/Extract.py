from flask import jsonify, request
import pickle
import sys
from yargy.interpretation import fact

from app import app
from app.Extractor import extractor
from app.Extractor.person import Person


@app.route('/extract', methods=['GET', 'POST'])
def extract():
    if request.method == 'POST':
        text = request.data.decode(sys.stdout.encoding)
        facts = extractor.extract_facts(text)
        result = []
        for f in facts:
            result.append(f.as_json)
        return result
    else:
        return [{}]
