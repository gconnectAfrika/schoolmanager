"""
Views for GFAST websites.

The development paradigm is meant to support multiple websites. To ease your development
pain, please add your site-specific code below the asciiart.

"""

import datetime
# import ldap3
import logging
import json
import os

from random import randrange

from flask import flash, g, jsonify, render_template, request, session, send_from_directory

from app import app

@app.route("/")
@app.route("/index/")
def index():
    return render_template('base.html')

#@app.route("/")
#def home():
#    return "Hello, Genius Connect!"
	
	
# @app.route('/')
# @app.route('/doc/build/index')
# def serve_sphinx_docs(path='index.html'):
    # return app.send_static_file(path)
	

@app.route('/unittest')
def unittest():
    return 'test worked'


@app.errorhandler(404)
def not_found_error(error):
    favourite_sites = ['https://xkcd.com/353',
                       'http://python-history.blogspot.ca/2010/06/import-antigravity.html',
                       'https://python.org',
                       'http://pandas.pydata.org',
                       'http://scikit-learn.org/stable',
                       'http://xxx.lanl.gov/',
                       'https://www.continuum.io/downloads',
                       'https://google.github.io/styleguide/pyguide.html',
                       'https://www.python.org/dev/peps/pep-0008',
                       'https://en.wikipedia.org/wiki/Untouchable_number']
    pageName = request.path
    this_link = favourite_sites[randrange(len(favourite_sites))]
    return render_template('404.html', page=pageName, this_link=this_link), 404


@app.errorhandler(500)
def internal_error(error):

    return render_template('500.html'), 500


#######################################################################
#     _____ _ _              _____                 _  __ _          
#    / ____(_) |            / ____|               (_)/ _(_)         
#   | (___  _| |_ ___ _____| (___  _ __   ___  ___ _| |_ _  ___ ___ 
#    \___ \| | __/ _ \______\___ \| '_ \ / _ \/ __| |  _| |/ __/ __|
#    ____) | | ||  __/      ____) | |_) |  __/ (__| | | | | (__\__ \
#   |_____/|_|\__\___|     |_____/| .__/ \___|\___|_|_| |_|\___|___/
#                                 | |                               
#                                 |_|                               

