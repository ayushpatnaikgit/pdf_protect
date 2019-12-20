from flask import Flask, make_response, request, redirect , jsonify, render_template      
import os, json 
import flask as fl
import sys, zipfile, io , pathlib

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/', methods=["POST"])
def transform_view():
    request_file = request.files['data_file']

    if not request_file:
        return "No file"

    request_file.save('file.pdf')
    os.system('bash killer.sh')
    data = open('output.pdf', 'rb')

    os.system('rm *.png')
    os.system('rm *.pdf')

    data.seek(0)

    return fl.send_file(
        data,
        mimetype='application/pdf',
        as_attachment=True,
        attachment_filename='protected.pdf'
    ) 
 

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8888)