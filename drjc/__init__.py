#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
from flask import Flask, render_template
from .markov import Markov

with open(sys.argv[1], "rb") as f:
	drjc_facts = map(str, f)

app = Flask(__name__)
drjc = Markov(drjc_facts)

@app.route("/")
def index():
	return "<b>{0}</b> #drjcfacts".format(drjc.markov_gen())
