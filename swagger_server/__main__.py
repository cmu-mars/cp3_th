#!/usr/bin/env python3

import connexion

from swagger_server import encoder

from flask import Flask, request, send_from_directory

app = connexion.App(__name__, specification_dir='./swagger/', static_url_path='')

app.app.json_encoder = encoder.JSONEncoder
app.add_api('swagger.yaml', arguments={'title': 'cmu mars brass th: phase 2, cp3'})
@app.route('/<path:path>')
def send_file(path):
    return send_from_directory('../client', path)
app.run(port=8080)
