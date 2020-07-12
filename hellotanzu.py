#!/usr/bin/python
from time import sleep;
from flask import Flask, request;
app = Flask(__name__);
@app.route('/',methods=['GET','POST'])
def atroot():
    return """
    <h1 style='color: red;'>Hello. I am a Flask app written in python.</h1>
    <p>I was built into container by Buildpack using Tanzu Build Services</p>
    """; 
app.run(host='0.0.0.0',port='8080');
