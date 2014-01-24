#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
from flask import (Flask, render_template, jsonify)
from .markov import Markov

with open(sys.argv[1], "rb") as f:
	drjc_facts = map(str, f)

app = Flask(__name__)
drjc = Markov(drjc_facts)

@app.route("/")
def index():
	return render_template("index.html", fact=drjc.markov_gen())

@app.route("/drjc.json")
def drjc_json():
	return jsonify({"fact": drjc.markov_gen()})
