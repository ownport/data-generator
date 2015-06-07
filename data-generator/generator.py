#!/usr/bin/env python
#
#   Data Generator service
#
__VERSION__ = '0.0.1'

DEFAULT_ROWS_PER_REQUEST=10
MAX_ROWS_PER_REQUEST=10000

import yaml
import json

from flask import Flask
from flask import request

from faker import Factory


class DataRequest(object):

    def __init__(self):

        self._data = list()


    def load_from_dict(self, **settings):

        try:
            self._dataset = settings['dataset']
        except:
            raise RuntimeError('Dataset is not specified')

        try:
            self._structure = settings['structure']
        except:
            raise RuntimeError('Structure is not specified')


    def load_from_yaml(self, settings):

        self.load_from_dict(**yaml.load(settings))


    def execute(self):

        if self._dataset.get('locale', None):
            fake = Factory.create()
        else:
            fake = Factory.create(self._dataset['locale'])

        rows = self._dataset.get('rows', DEFAULT_ROWS_PER_REQUEST)
        if rows > MAX_ROWS_PER_REQUEST:
            return 'Only %s rows are allowed per request' % MAX_ROWS_PER_REQUEST

        for _ in range(rows):
            row = dict()
            for field in self._structure:
                row[field['name']] = eval(field['type'])
            self._data.append(row)

    def to_json(self):

        return '\n'.join([json.dumps(r) for r in self._data])


    def to_csv(self):

        # data = list()
        # if ('headers' in self._dataset) and (self._dataset['headers']):
        #     data.append('|'.join([f['name'] for f in self._structure]))
        # return '\n'.join(data)
        raise NotImplemented()

app = Flask(__name__)

def handle_request():

    if request.method == 'POST':
        if not request.files.get('request', None):
            raise RuntimeError('The Request field is not defined')

        data_request = DataRequest()
        data_request.load_from_yaml(request.files['request'].read())
        data_request.execute()
        return data_request
    else:
        raise RuntimeError('Unknown HTTP Method: %s' ^ request.method)


@app.route("/version", methods=["GET",])
def version():
    return 'Data-Generator/%s' % __VERSION__


@app.route("/json", methods=["POST",])
def to_json():

    data_request = handle_request()
    return data_request.to_json()


@app.route("/csv", methods=["POST",])
def to_csv():

    data_request = handle_request()
    return data_request.to_csv()


if __name__ == "__main__":
    app.run(host='0.0.0.0')

