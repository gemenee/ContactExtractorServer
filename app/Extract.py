from flask import jsonify, request
import pickle
from yargy.interpretation import fact

from app import app
from app.Extractor import extractor
from app.Extractor.person import Person

@app.route('/extract', methods=['GET', 'POST'])
def extract():

    if request.method == 'POST':
        text = request.data.decode('utf-8')
        facts = extractor.extract_facts(text)
        result = [{}]
        for f in facts:
            if f is not None:
                result.append(f.as_json)
        return jsonify(result)
    else:
        return [{}]
